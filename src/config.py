from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    bot_token: str
    pay_token: str
    webapp_url: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


conf = Config()
