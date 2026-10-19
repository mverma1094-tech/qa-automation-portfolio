from pathlib import Path
from log_parser import find_alerts, parse

SAMPLE = (Path(__file__).parent / "sample_auth.log").read_text().splitlines()


def kinds(alerts):
    return [(kind, ip) for kind, ip, _ in alerts]


def test_counts_failed_logins_per_ip():
    failed, _, _ = parse(SAMPLE)
    assert failed["203.0.113.45"] == 6
    assert failed["198.51.100.7"] == 5
    assert failed["10.0.0.22"] == 1


def test_flags_brute_force_ips():
    alerts = kinds(find_alerts(SAMPLE))
    assert ("BRUTE_FORCE", "203.0.113.45") in alerts
    assert ("BRUTE_FORCE", "198.51.100.7") in alerts


def test_single_typo_is_not_flagged():
    # jsmith mistyped once, then logged in: normal behavior
    alerts = kinds(find_alerts(SAMPLE))
    assert all(ip != "10.0.0.22" for _, ip in alerts)


def test_flags_username_guessing():
    alerts = kinds(find_alerts(SAMPLE))
    assert ("USER_GUESSING", "198.51.100.7") in alerts


def test_flags_success_after_brute_force():
    alerts = kinds(find_alerts(SAMPLE))
    assert ("POSSIBLE_BREACH", "203.0.113.45") in alerts


# Boundary value analysis on the brute-force threshold (5)
def make_failures(n, ip="192.0.2.1"):
    return [f"sshd[1]: Failed password for root from {ip} port 1 ssh2"] * n


def test_threshold_minus_one_not_flagged():
    assert find_alerts(make_failures(4)) == []


def test_threshold_exactly_flagged():
    assert kinds(find_alerts(make_failures(5))) == [("BRUTE_FORCE", "192.0.2.1")]


def test_empty_log_has_no_alerts():
    assert find_alerts([]) == []
