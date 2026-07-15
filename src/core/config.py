from __future__ import annotations

import os


class Config:
    """
    Конфигурация AI Studio Framework.
    """

    GIGACHAT_CLIENT_ID = os.getenv("GIGACHAT_CLIENT_ID", "")
    GIGACHAT_CLIENT_SECRET = os.getenv("GIGACHAT_CLIENT_SECRET", "")
    GIGACHAT_AUTH_URL = os.getenv(
        "GIGACHAT_AUTH_URL",
        "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
    )
    GIGACHAT_API_URL = os.getenv(
        "GIGACHAT_API_URL",
        "https://gigachat.devices.sberbank.ru/api/v1/chat/completions",
    )
