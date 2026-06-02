# i18n/translator.py

import copy
import logging
import re

from i18n.controlled_terms import CONTROLLED_TERMS

logger = logging.getLogger("app.i18n")

SUPPORTED_LANGS = {"en", "fr", "de", "it", "es", "pt", "nl"}
ACTIVE_TRANSLATION_LANGS = {"fr"}

PROTECTED_PATHS = {
    "renderer_instructions",
    "event_targets",
    "meta.athlete.identity.notes",
    "meta.athlete.profiles",
}

PROTECTED_VALUES = {
    # phases
    "base",
    "build",
    "peak",
    "recovery",
    "taper",
    "transition",

    # alignment / ADE
    "aligned",
    "misaligned",
    "increasing",
    "decreasing",
    "reduced",

    # sports
    "ride",
    "run",
    "swim",
    "walk",
    "hike",

    # common states
    "high",
    "moderate",
    "low",
    "balanced",
    "unknown",
    "none",

    # ADE / PI states
    "load_accepting",
    "productive_fatigue",
    "recovery_priority",
    "mixed_adaptation",
    "overreached",
    "fresh",
    "neutral",
}


def normalise_lang(lang):
    lang = (lang or "en").lower().strip()
    return lang if lang in SUPPORTED_LANGS else "en"


def is_protected_path(path: str) -> bool:
    if not path:
        return False

    return any(x in path for x in PROTECTED_PATHS)


def looks_technical(text: str) -> bool:

    if not text:
        return True

    text = text.strip()

    if not text:
        return True

    if text.startswith(("http://", "https://")):
        return True

    if re.match(r"^\d+(\.\d+)?$", text):
        return True

    if re.match(r"^\d{4}-\d{2}-\d{2}", text):
        return True

    if "_" in text:
        return True

    return False


def should_translate(text: str) -> bool:

    if not isinstance(text, str):
        return False

    if looks_technical(text):
        return False

    if text.lower() in PROTECTED_VALUES:
        return False

    # sentence / coaching prose
    if len(text) >= 20 and " " in text:
        return True

    return False


def translate_text(text: str, lang: str) -> str:

    controlled = CONTROLLED_TERMS.get(lang, {})

    if text in controlled:
        return controlled[text]

    return text


def translate_semantic_graph(obj, lang="en"):

    lang = normalise_lang(lang)

    if lang == "en":
        return obj

    if lang not in ACTIVE_TRANSLATION_LANGS:
        return obj

    def walk(value, path=""):

        if is_protected_path(path):
            return value

        if isinstance(value, dict):
            return {
                k: walk(
                    v,
                    path=f"{path}.{k}" if path else k,
                )
                for k, v in value.items()
            }

        if isinstance(value, list):
            return [walk(v, path=path) for v in value]

        if isinstance(value, str):

            if should_translate(value):
                return translate_text(value, lang)

            return value

        return value

    return walk(copy.deepcopy(obj))