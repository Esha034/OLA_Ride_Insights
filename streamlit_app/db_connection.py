from sqlalchemy import create_engine
import os
import streamlit as st
from urllib.parse import quote_plus

def get_engine():
    DB_USER = os.getenv("DB_USER", "postgres")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "5433")
    DB_NAME = os.getenv("DB_NAME", "ola_rides_db")

    if not DB_PASSWORD:
        st.error("DB_PASSWORD environment variable not set")
        st.stop()

    # ✅ URL encode password
    encoded_password = quote_plus(DB_PASSWORD)

    DATABASE_URL = (
        f"postgresql+psycopg2://{DB_USER}:{encoded_password}"
        f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    engine = create_engine(DATABASE_URL)
    return engine
