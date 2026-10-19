import sqlite3
from pathlib import Path

HERE = Path(__file__).parent


def build_database():
    """Create a fresh in-memory database from schema.sql and seed_data.sql."""
    conn = sqlite3.connect(":memory:")
    conn.executescript((HERE / "schema.sql").read_text())
    conn.executescript((HERE / "seed_data.sql").read_text())
    return conn


def run_check(conn, query):
    return conn.execute(query).fetchall()
