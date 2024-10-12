"""
This module sets the env configs for our WhatsApp app.
"""

from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
import os


# Store configurations for the app
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    meta_api_version: str
    meta_app_id: str
    meta_app_secret: SecretStr
    whatsapp_cloud_number_id: str
    whatsapp_verify_token: SecretStr
    whatsapp_api_token: SecretStr
    daily_message_limit: int


class LLMSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
        env_nested_delimiter="__",
    )

    # OpenAI settings
    openai_api_key: Optional[SecretStr] = None
    openai_org: Optional[str] = None
    twiga_openai_assistant_id: Optional[str] = None

    # GROQ settings
    groq_api_key: Optional[SecretStr] = None


# Function to determine if we're running on Render
def is_running_on_render():
    return os.environ.get("RENDER") == "true"


# Initialize settings
if is_running_on_render():
    # On Render, rely solely on environment variables
    settings = Settings(_env_file=None)
    llm_settings = LLMSettings(_env_file=None)
else:
    # Locally, use .env file
    settings = Settings()
    llm_settings = LLMSettings()
