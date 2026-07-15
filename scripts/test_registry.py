from src.core.registry import AgentRegistry
from src.core.orchestrator import Orchestrator
from src.core.router import Router
from src.memory.context_manager import ContextManager

from src.agents.pm_agent import PMAgent
from src.agents.developer_agent import DeveloperAgent

from src.providers.gigachat_provider import GigaChatProvider


def main():
    registry = AgentRegistry()

    provider = GigaChatProvider()

    registry.register(
        PMAgent(
            name="pm",
            role="Project Manager",
            provider=provider,
        )
    )

    registry.register(
        DeveloperAgent(
            name="developer",
            role="Developer",
            provider=provider,
        )
    )

    context = ContextManager()

    router = Router(registry)

    orchestrator = Orchestrator(
        registry=registry,
        context_manager=context,
        router=router,
    )

    print(
        orchestrator.execute(
            task="Составить план разработки проекта.",
            session_id="session_1",
        )
    )

    print("-" * 60)

    print(
        orchestrator.execute(
            task="Написать Python класс ContextManager.",
            session_id="session_1",
        )
    )

    print("-" * 60)

    print("История сессии:")

    for message in context.get_history("session_1"):
        print(message)


if __name__ == "__main__":
    main()
