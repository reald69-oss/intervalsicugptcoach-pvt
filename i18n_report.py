# i18n_report.py

import json
import os
import copy
import logging

logger = logging.getLogger("app.i18n")

SUPPORTED_LANGS = {"en", "fr", "de", "it", "es", "pt"}

I18N_DIR = os.path.join(os.path.dirname(__file__), "i18n")


def normalise_lang(lang):
    lang = (lang or "en").lower().strip()
    return lang if lang in SUPPORTED_LANGS else "en"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_catalog(lang):
    lang = normalise_lang(lang)

    if lang == "en":
        return {}

    filename = f"{lang}.json"

    candidates = [
        os.path.join(BASE_DIR, "i18n", filename),
        os.path.join(os.getcwd(), "i18n", filename),
        os.path.join("/app", "i18n", filename),
    ]

    try:
        logger.info("[I18N] __file__=%s", __file__)
        logger.info("[I18N] cwd=%s", os.getcwd())
        logger.info("[I18N] /app files=%s", os.listdir("/app"))
    except Exception as e:
        logger.info("[I18N] listing failed=%s", e)

    for path in candidates:
        logger.info("[I18N] trying path=%s exists=%s", path, os.path.exists(path))

        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                catalog = json.load(f)

            logger.info("[I18N] loaded=%s entries=%s", path, len(catalog))
            return catalog

    return {}


def translate_report_values(obj, lang="en"):
    lang = normalise_lang(lang)

    if lang == "en":
        return obj

    catalog = load_catalog(lang)

    logger.info("[I18N] active_lang=%s catalog_entries=%s", lang, len(catalog))

    def walk(value):
        if isinstance(value, dict):
            return {k: walk(v) for k, v in value.items()}

        if isinstance(value, list):
            return [walk(v) for v in value]

        if isinstance(value, str):
            translated = catalog.get(value, value)

            if value == "Weekly Training Report":
                logger.info("[I18N] title_match=%s -> %s", value, translated)

            return translated

        return value

    return walk(copy.deepcopy(obj))