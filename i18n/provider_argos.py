# i18n/provider_argos.py

import logging

logger = logging.getLogger("app.i18n.argos")

_READY = set()


def ensure_argos_model(source="en", target="fr"):
    """
    Lazy install Argos model if missing.
    Start narrow: en→fr first.
    """
    pair = (source, target)

    if pair in _READY:
        return

    import argostranslate.package
    import argostranslate.translate

    installed = argostranslate.translate.get_installed_languages()

    src = next((l for l in installed if l.code == source), None)
    tgt = next((l for l in installed if l.code == target), None)

    if src and tgt:
        try:
            translation = src.get_translation(tgt)
            if translation:
                _READY.add(pair)
                logger.info("[I18N] Argos model already installed %s→%s", source, target)
                return
        except Exception:
            pass

    logger.info("[I18N] Installing Argos model %s→%s", source, target)

    argostranslate.package.update_package_index()
    packages = argostranslate.package.get_available_packages()

    package = next(
        (
            p for p in packages
            if p.from_code == source and p.to_code == target
        ),
        None
    )

    if not package:
        raise RuntimeError(f"No Argos package found for {source}->{target}")

    path = package.download()
    argostranslate.package.install_from_path(path)

    _READY.add(pair)
    logger.info("[I18N] Argos model installed %s→%s", source, target)


def translate_with_argos(text: str, lang: str) -> str:
    if lang == "en":
        return text

    # Start with French only. Add others once fr is stable.
    if lang not in {"fr"}:
        return text

    try:
        ensure_argos_model("en", lang)

        import argostranslate.translate

        translated = argostranslate.translate.translate(text, "en", lang)

        return translated or text

    except Exception as e:
        logger.warning("[I18N] Argos translation failed lang=%s error=%s", lang, e)
        return text