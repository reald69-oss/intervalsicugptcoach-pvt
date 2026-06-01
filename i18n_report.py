# i18n_report.py

import json
import os
import copy

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

    if not os.path.exists(path):
        return {}

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def translate_report_values(obj, lang="en"):
    lang = normalise_lang(lang)

    if lang == "en":
        return obj

    catalog = load_catalog(lang)

    def walk(value):
        if isinstance(value, dict):
            # keys unchanged
            return {k: walk(v) for k, v in value.items()}

        if isinstance(value, list):
            return [walk(v) for v in value]

        if isinstance(value, str):
            return catalog.get(value, value)

        return value

    return walk(copy.deepcopy(obj))