"""
SSH log parser: reads a Linux auth log and flags suspicious activity.

Flags:
  1. Brute force    - an IP with THRESHOLD or more failed logins
  2. User guessing  - an IP trying usernames that don't exist
  3. Possible breach - a successful login from an IP that was flagged for brute force

Usage:
    python log_parser.py sample_auth.log
"""
import re
import sys
from collections import defaultdict

THRESHOLD = 5

FAILED = re.compile(
    r"Failed password for (?P<invalid>invalid user )?(?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)
ACCEPTED = re.compile(
    r"Accepted password for (?P<user>\S+) from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})"
)


def parse(lines):
    failed = defaultdict(int)
    invalid_users = defaultdict(set)
    accepted = []

    for line in lines:
        if m := FAILED.search(line):
            failed[m["ip"]] += 1
            if m["invalid"]:
                invalid_users[m["ip"]].add(m["user"])
        elif m := ACCEPTED.search(line):
            accepted.append((m["user"], m["ip"]))

    return failed, invalid_users, accepted


def find_alerts(lines, threshold=THRESHOLD):
    failed, invalid_users, accepted = parse(lines)
    alerts = []

    brute_force_ips = {ip for ip, count in failed.items() if count >= threshold}
    for ip in sorted(brute_force_ips):
        alerts.append(("BRUTE_FORCE", ip, f"{failed[ip]} failed logins"))

    for ip, users in sorted(invalid_users.items()):
        if len(users) >= 3:
            alerts.append(("USER_GUESSING", ip, f"tried {len(users)} nonexistent users"))

    for user, ip in accepted:
        if ip in brute_force_ips:
            alerts.append(("POSSIBLE_BREACH", ip, f"successful login as '{user}' after brute force"))

    return alerts


def main(path):
    with open(path) as f:
        alerts = find_alerts(f)
    if not alerts:
        print("No suspicious activity found.")
        return
    for kind, ip, detail in alerts:
        print(f"[{kind:<15}] {ip:<15} {detail}")
    print(f"\n{len(alerts)} alert(s) found.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sample_auth.log")
