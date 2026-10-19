"""Run every validation check and print a pass/fail report."""
from db import build_database, run_check
from validation_queries import CHECKS


def main():
    conn = build_database()
    failed = 0
    for name, query in CHECKS.items():
        rows = run_check(conn, query)
        status = "PASS" if not rows else f"FAIL ({len(rows)} row(s))"
        print(f"{name:<38} {status}")
        for row in rows:
            print(f"    -> {row}")
        failed += bool(rows)
    print(f"\n{len(CHECKS) - failed} passed, {failed} failed out of {len(CHECKS)} checks")


if __name__ == "__main__":
    main()
