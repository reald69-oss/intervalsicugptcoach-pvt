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
from i18n.provider_argos import translate_with_argos

logger = logging.getLogger("app.i18n")

SUPPORTED_LANGS = {"en", "fr", "de", "it", "es", "pt"}


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
    # Internal instructions / contracts
    "renderer_instructions",
    "hard_rules",
    "list_rules",
    "tone_rules",
    "card_rules",
    "required_fields",
    "preferred_markdown_shape",
    "contract",
    "report_contract",

    # Identity / technical
    "id",
    "uid",
    "athlete_id",
    "event_id",
    "activity_id",
    "paired_event_id",
    "activity_link",
    "url",
    "website",
    "email",

    # Usually semantic contract values
    "key",
    "source",
    "framework",
    "formula",
    "methodology",
    "version",

    # Preserve stable machine-readable fields
    "type",
    "category",
    "status",
    "classification",
    "semantic_state",
    "operational_state",
    "adaptation_state",
    "risk_flag",
    "phase_alignment",
    "resolution",
    "context_window",
    "load_order",
    "tiz_order",
    "gap_model",
    "pace_units",

    # Names are risky: activity names / athlete names / race names
    "name",
    "athlete_name",
    "event_name",
    "notes",
    "type",
    "types",
    "category",
    "priority",
    "status",
    "classification",
    "semantic_state",
    "metric_confidence",
    "confidence",
    "thermal_source_confidence",
    "fatigue_class",
    "load_trend",
    "taper_state",
    "form_status",
    "readiness_label",
    "readiness_modifier",
    "training_bias",
    "race_type",
    "adaptation_focus",
    "risk_flag",
    "nutrition_status",
    "nutrition_confidence",
    "operational_state",
    "adaptation_state",
    "system_state",
    "system_status",
    "system_status_timeline",
    "adaptation_bias",
    "curve_profile",
    "curve_quality",
    "model_quality",
    
}

DO_NOT_TRANSLATE_PATH_CONTAINS = {
    "meta.athlete.identity.notes",
    "meta.athlete.profiles",
}

def normalise_lang(lang):
    lang = (lang or "en").lower().strip()
    return lang if lang in SUPPORTED_LANGS else "en"


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

    # Preserve likely IDs/codes with no spaces
    if " " not in v and re.match(r"^[A-Za-z0-9_\-:.]+$", v) and len(v) >= 8:
        return True

    # Preserve screaming enum-like values with underscores
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

    translated = translate_with_argos(value, lang)

    if translated and translated != value:
        set_cached_translation(
            text=value,
            lang=lang,
            translated=translated,
            provider="argos",
        )

    return translated or value


def should_translate(key, value: str, path: str | None = None) -> bool:
    if not isinstance(value, str):
        return False

    if key in DO_NOT_TRANSLATE_KEYS:
        return False

    if looks_technical(value):
        return False

    controlled = CONTROLLED_TERMS.get("fr", {})

    # Controlled terms are safe even if key is not explicitly allowed.
    if value in controlled:
        return True

    if key in TRANSLATABLE_KEYS:
        return True

    if path and any(p in path for p in DO_NOT_TRANSLATE_PATH_CONTAINS):
        return False

    return False


def translate_semantic_graph(obj, lang="en", key=None, path=""):
    lang = normalise_lang(lang)

    if lang == "en":
        return obj

    try:
        init_cache()
    except Exception as e:
        logger.warning("[I18N] Cache init failed: %s", e)

    def walk(value, current_key=None, current_path=""):
        if isinstance(value, dict):
            return {
                k: walk(v, current_key=k, current_path=f"{current_path}.{k}" if current_path else k)
                for k, v in value.items()
            }

        if isinstance(value, list):
            return [
                walk(v, current_key=current_key, current_path=current_path)
                for v in value
            ]

        if isinstance(value, str):
            if not should_translate(current_key, value, current_path):
                return value

            return translate_text(value, lang)

        return value

    translated = walk(copy.deepcopy(obj), current_key=key, current_path=path)

    logger.info("[I18N] semantic_graph translated lang=%s", lang)

    return translated