# i18n/cache_sqlite.py

import os
import sqlite3
import hashlib
from datetime import datetime

DB_PATH = os.getenv("I18N_CACHE_DB", "/app/data/i18n_cache.sqlite3")


def init_cache():
    db_dir = os.path.dirname(DB_PATH)

    if db_dir:
        os.makedirs(db_dir, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS translation_cache (
                cache_key TEXT PRIMARY KEY,
                lang TEXT NOT NULL,
                source_text TEXT NOT NULL,
                translated_text TEXT NOT NULL,
                provider TEXT NOT NULL,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)

        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx_translation_cache_lang
            ON translation_cache(lang)
        """)


def make_cache_key(text: str, lang: str) -> str:
    raw = f"{lang}|{text}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def get_cached_translation(text: str, lang: str):
    key = make_cache_key(text, lang)

    try:
        with sqlite3.connect(DB_PATH) as conn:
            row = conn.execute(
                "SELECT translated_text FROM translation_cache WHERE cache_key = ?",
                (key,)
            ).fetchone()

        return row[0] if row else None

    except Exception:
        return None


def set_cached_translation(text: str, lang: str, translated: str, provider: str):
    if not translated:
        return

    key = make_cache_key(text, lang)
    now = datetime.utcnow().isoformat()

    try:
        init_cache()

        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("""
                INSERT INTO translation_cache (
                    cache_key,
                    lang,
                    source_text,
                    translated_text,
                    provider,
                    created_at,
                    updated_at
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(cache_key) DO UPDATE SET
                    translated_text = excluded.translated_text,
                    provider = excluded.provider,
                    updated_at = excluded.updated_at
            """, (
                key,
                lang,
                text,
                translated,
                provider,
                now,
                now,
            ))

    except Exception:
        return