from __future__ import annotations

from collections import defaultdict, deque
from typing import Any


class ContextManager:
    """
    Хранилище контекста AI Studio Framework.
    """

    def __init__(self, history_size: int = 20) -> None:
        self._history = defaultdict(lambda: deque(maxlen=history_size))
        self._shared = {}

    def add_message(self, session_id: str, message: str) -> None:
        """Добавляет сообщение в историю сессии."""
        self._history[session_id].append(message)

    def get_history(self, session_id: str) -> list[str]:
        """Возвращает историю сообщений."""
        return list(self._history[session_id])

    def set(self, key: str, value: Any) -> None:
        """Сохраняет общее значение."""
        self._shared[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Возвращает общее значение."""
        return self._shared.get(key, default)

    def clear(self) -> None:
        """Полностью очищает память."""
        self._history.clear()
        self._shared.clear()
