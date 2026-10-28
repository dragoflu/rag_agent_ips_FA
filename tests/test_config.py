from pathlib import Path

from rag_ips.config import Settings


def test_settings_read_env(monkeypatch):
    monkeypatch.setenv("LLM_MODEL", "some-model")
    monkeypatch.setenv("LLM_API_KEY", "secret")
    monkeypatch.setenv("DATA_DIR", "/tmp/docs")

    settings = Settings(_env_file=None)

    assert settings.llm_model == "some-model"
    assert settings.llm_api_key.get_secret_value() == "secret"
    assert settings.data_dir == Path("/tmp/docs")
