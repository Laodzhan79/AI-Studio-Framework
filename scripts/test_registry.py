from src.core.registry import AgentRegistry
from src.core.orchestrator import Orchestrator
from src.core.router import Router
from src.memory.context_manager import ContextManager
from src.agents.pm_agent import PMAgent
from src.agents.developer_agent import DeveloperAgent
from src.providers.base_provider import BaseProvider


class MockProvider(BaseProvider):
    @property
    def name(self) -> str:
        return "MockProvider"

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.7,
    ) -> str:
        return user_prompt


def main():
    registry = AgentRegistry()
    context = ContextManager()
    router = Router()

    provider = MockProvider()

    pm = PMAgent(
        name="pm",
        role="Project Manager",
        provider=provider,
    )

    developer = DeveloperAgent(
        name="developer",
        role="Developer",
        provider=provider,
    )

    registry.register(pm)
    registry.register(developer)

    orchestrator = Orchestrator(
        registry=registry,
        context_manager=context,
        router=router,
    )

    print(orchestrator.execute(
        task="Составить план разработки проекта.",
        session_id="session_1",
    ))

    print("-" * 50)

    print(orchestrator.execute(
        task="Написать Python класс ContextManager.",
        session_id="session_1",
    ))

    print("-" * 50)

    print("История сессии:")

    for message in context.get_history("session_1"):
        print(message)


if __name__ == "__main__":
    main()
