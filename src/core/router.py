from __future__ import annotations


class Router:
    """
    Определяет, какому агенту передать задачу.
    """

    def route(self, task: str) -> str:
        text = task.lower()

        developer_keywords = (
            "код",
            "python",
            "класс",
            "функция",
            "метод",
            "рефакторинг",
            "bug",
            "ошибка",
        )

        if any(keyword in text for keyword in developer_keywords):
            return "developer"

        return "pm"
