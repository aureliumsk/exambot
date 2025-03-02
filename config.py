"""Загрузчик конфигурации бота.
Пример конфигурации смотрите в example-config.toml."""

import tomllib
from enum import StrEnum
from pydantic import BaseModel


class Scope(StrEnum):
    personal = "personal"
    b2b = "b2b"
    corp = "corp"


class TelegramAPIConfig(BaseModel):
    """Значения, специфические для Telegram."""
    api_key: str


class GigachatAPIConfig(BaseModel):
    """Значения, специфические для Gigachat."""
    client_id: str
    client_secret: str
    scope: Scope = Scope.personal


class Config(BaseModel):
    """Общая конфигурацию бота."""
    telegram: TelegramAPIConfig
    gigachat: GigachatAPIConfig

    
def load() -> Config:
    with open("config.toml", "rb") as config_file:
        raw_config = tomllib.load(config_file)
    return Config.model_validate(raw_config)
