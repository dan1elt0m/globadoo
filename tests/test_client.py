import pytest

from globadoo.client import get_openai_client


def test_get_openai_client(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "test")
    client = get_openai_client()
    assert client.api_key == "test"


def test_get_openai_client_no_api_key():
    with pytest.raises(ValueError, match="API key not found. Please set OPENAI_API_KEY environment variable."):
        get_openai_client()
