import copy
import logging
from i18n_catalogs import CATALOGS

logger = logging.getLogger("app.i18n")

SUPPORTED_LANGS = {"en", "fr", "de", "it", "es", "pt"}


def normalise_lang(lang):
    lang = (lang or "en").lower().strip()
    return lang if lang in SUPPORTED_LANGS else "en"


def load_catalog(lang):
    lang = normalise_lang(lang)

    if lang == "en":
        return {}

    catalog = CATALOGS.get(lang, {})

    logger.info(
        "[I18N] lang=%s catalog_entries=%s title_lookup=%s",
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

    def walk(value):
        if isinstance(value, dict):
            return {k: walk(v) for k, v in value.items()}

        if isinstance(value, list):
            return [walk(v) for v in value]

        if isinstance(value, str):
            return catalog.get(value, value)

        return value

    return walk(copy.deepcopy(obj))