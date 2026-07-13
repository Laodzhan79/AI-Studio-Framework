from src.agents.base import BaseAgent


class EchoAgent(BaseAgent):
    """
    Простейший агент для проверки работы архитектуры.
    """

    def execute(self, task: str, context: dict | None = None) -> str:
        return f"[{self.name}] {task}"
