# i18n/translator.py

import re
import copy
import logging

from i18n.controlled_terms import CONTROLLED_TERMS
from i18n.cache_sqlite import (
    init_cache,
    get_cached_translation,
    set_cached_translation,
)

logger = logging.getLogger("app.i18n")

SUPPORTED_LANGS = {"en", "fr", "de", "it", "es", "pt", "nl"}


TRANSLATABLE_KEYS = {
    "title",
    "subtitle",
    "scope",
    "intended_use",
    "label",
    "display_label",
    "display_name",
    "description",
    "summary",
    "meaning",
    "interpretation",
    "coaching_implication",
    "recommendation",
    "recommended_adjustment",
    "reason",
    "message",
    "directive",
    "guidance",
    "training_guidance",
    "readiness_signal",
    "adaptation_signal",
    "system_guidance",
    "question",
    "descriptor",
    "basis",
    "note",
    "notes",
    "warning",
    "verdict",
    "headline",
}


DO_NOT_TRANSLATE_KEYS = {
    # ---------------------------------------------------------
    # Internal instructions / renderer contracts
    # ---------------------------------------------------------
    "renderer_instructions",
    "hard_rules",
    "list_rules",
    "tone_rules",
    "card_rules",
    "required_fields",
    "preferred_markdown_shape",
    "contract",
    "report_contract",
    "section_handling",
    "interpretation_rules",
    "stack_section_map",
    "phase_required",
    "phase_constraint",
    "forecast_context",
    "load_recovery_state",
    "temporal_pattern",
    "dominant_pattern",
    "target_event",
    "race_profile",
    "targets",
    "durability_bounds",
    "readiness_governance",
    "taper_governance",

    # ---------------------------------------------------------
    # Identity / links / technical IDs
    # ---------------------------------------------------------
    "id",
    "uid",
    "athlete_id",
    "event_id",
    "activity_id",
    "paired_event_id",
    "paired_activity_id",
    "activity_link",
    "url",
    "website",
    "email",
    "profile_image",

    # ---------------------------------------------------------
    # Names are risky:
    # athlete names, race names, activity names, workout names
    # ---------------------------------------------------------
    "name",
    "athlete_name",
    "event_name",
    "firstname",
    "lastname",

    # ---------------------------------------------------------
    # Athlete/user notes should not be machine translated
    # because they may contain embedded render instructions
    # ---------------------------------------------------------
    "notes",

    # ---------------------------------------------------------
    # Stable semantic contract / metadata
    # ---------------------------------------------------------
    "key",
    "source",
    "framework",
    "formula",
    "methodology",
    "version",
    "model",
    "method",
    "mode",
    "basis",
    "scope",
    "context_window",

    # ---------------------------------------------------------
    # Core machine-readable classification fields
    # ---------------------------------------------------------
    "type",
    "types",
    "category",
    "priority",
    "status",
    "classification",
    "semantic_state",
    "state",
    "state_key",
    "risk_flag",
    "resolution",

    # ---------------------------------------------------------
    # Phase fields MUST remain stable for UI/code branching
    # ---------------------------------------------------------
    "phase",
    "required_phase",
    "phase_context",
    "phase_alignment",
    "last_phase",
    "current_phase",
    "taper_state",

    # ---------------------------------------------------------
    # Forecast / readiness / event governance enums
    # ---------------------------------------------------------
    "fatigue_class",
    "load_trend",
    "form_status",
    "readiness_label",
    "readiness_modifier",
    "training_bias",
    "race_type",
    "event_demand",

    # ---------------------------------------------------------
    # ADE / PI / ESPE machine states
    # ---------------------------------------------------------
    "operational_state",
    "adaptation_state",
    "adaptation_focus",
    "system_state",
    "system_status",
    "system_status_timeline",
    "adaptation_bias",
    "dominant_shift",
    "curve_profile",
    "curve_quality",
    "model_quality",
    "nutrition_status",
    "nutrition_confidence",

    # ---------------------------------------------------------
    # Confidence fields should stay contract-stable
    # ---------------------------------------------------------
    "metric_confidence",
    "confidence",
    "thermal_source_confidence",

    # ---------------------------------------------------------
    # Ordering / unit / model constants
    # ---------------------------------------------------------
    "load_order",
    "tiz_order",
    "gap_model",
    "pace_units",
    "pace_load_type",
    "mmp_model",
}

DO_NOT_TRANSLATE_PATH_CONTAINS = {
    "meta.athlete.identity.notes",
    "meta.athlete.profiles",
    "event_targets",
}


ACTIVE_TRANSLATION_LANGS = {"fr"}


def normalise_lang(lang):
    lang = (lang or "en").lower().strip()
    return lang if lang in SUPPORTED_LANGS else "en"


def is_blocked_path(path: str | None) -> bool:
    if not path:
        return False

    return any(
        protected in path
        for protected in DO_NOT_TRANSLATE_PATH_CONTAINS
    )


def looks_technical(value: str) -> bool:
    if not value:
        return True

    v = value.strip()

    if not v:
        return True

    if v.startswith(("http://", "https://")):
        return True

    if re.match(r"^\d{4}-\d{2}-\d{2}", v):
        return True

    if re.match(r"^\d{4}-\d{2}-\d{2}T", v):
        return True

    if re.match(r"^[+-]?\d+(\.\d+)?$", v):
        return True

    if " " not in v and re.match(r"^[A-Za-z0-9_\-:.]+$", v) and len(v) >= 8:
        return True

    if "_" in v and v.upper() == v:
        return True

    return False


def translate_text(value: str, lang: str) -> str:
    controlled = CONTROLLED_TERMS.get(lang, {})

    if value in controlled:
        return controlled[value]

    cached = get_cached_translation(value, lang)

    if cached:
        return cached

    return value


def should_translate(key, value: str, path: str | None = None, lang: str = "fr") -> bool:
    if not isinstance(value, str):
        return False

    # Hard stop before controlled terms
    if key in DO_NOT_TRANSLATE_KEYS:
        return False

    if is_blocked_path(path):
        return False

    if looks_technical(value):
        return False

    controlled = CONTROLLED_TERMS.get(lang, {})

    # Controlled terms are only safe on user-facing keys
    if value in controlled and key in TRANSLATABLE_KEYS:
        return True

    if key in TRANSLATABLE_KEYS:
        return True

    return False


def translate_semantic_graph(obj, lang="en", key=None, path=""):
    lang = normalise_lang(lang)

    if lang == "en":
        return obj

    if lang not in ACTIVE_TRANSLATION_LANGS:
        logger.info(
            "[I18N] lang=%s accepted but translation not active; returning English",
            lang,
        )
        return obj

    try:
        init_cache()
    except Exception as e:
        logger.warning("[I18N] Cache init failed: %s", e)

    def walk(value, current_key=None, current_path=""):
        # Hard stop: preserve entire protected subtree
        if current_key in DO_NOT_TRANSLATE_KEYS:
            return value

        if is_blocked_path(current_path):
            return value

        if isinstance(value, dict):
            return {
                k: walk(
                    v,
                    current_key=k,
                    current_path=f"{current_path}.{k}" if current_path else k,
                )
                for k, v in value.items()
            }

        if isinstance(value, list):
            return [
                walk(
                    v,
                    current_key=current_key,
                    current_path=current_path,
                )
                for v in value
            ]

        if isinstance(value, str):
            if not should_translate(current_key, value, current_path, lang=lang):
                return value

            return translate_text(value, lang)

        return value

    translated = walk(copy.deepcopy(obj), current_key=key, current_path=path)

    logger.info("[I18N] semantic_graph translated lang=%s", lang)

    return translated