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


def load_catalog(lang):
    lang = normalise_lang(lang)

    if lang == "en":
        return {}

    path = os.path.join(I18N_DIR, f"{lang}.json")

    logger.info("[I18N] dir=%s", I18N_DIR)
    logger.info("[I18N] path=%s exists=%s", path, os.path.exists(path))

    if not os.path.exists(path):
        return {}

    with open(path, "r", encoding="utf-8") as f:
        catalog = json.load(f)

    logger.info(
        "[I18N] lang=%s entries=%s title_lookup=%s",
        lang,
        len(catalog),
        catalog.get("Weekly Training Report")
    )

    return catalog


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