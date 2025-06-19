import pytest
from ingestor.config import REDDIT_CONFIG, KAFKA_CONFIG, SUBREDDITS


def test_reddit_config_keys_exist():
    required_keys = ["client_id", "client_secret", "user_agent"]
    for key in required_keys:
        assert key in REDDIT_CONFIG, f"{key} is missing in REDDIT_CONFIG"
        assert REDDIT_CONFIG[key], f"{key} should not be empty"


def test_kafka_config_keys_exist():
    required_keys = ["bootstrap_servers", "topic"]
    for key in required_keys:
        assert key in KAFKA_CONFIG, f"{key} is missing in KAFKA_CONFIG"
        assert KAFKA_CONFIG[key], f"{key} should not be empty"


def test_subreddits_not_empty():
    assert isinstance(SUBREDDITS, list), "SUBREDDITS should be a list"
    assert len(SUBREDDITS) > 0, "SUBREDDITS list should not be empty"
    for sub in SUBREDDITS:
        assert isinstance(sub, str) and sub.strip(), f"Invalid subreddit: '{sub}'"
