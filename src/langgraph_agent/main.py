from .graph.builder import build_graph
from rich.console import Console
from rich.panel import Panel
from rich.rule import Rule

console = Console()


def main():
    console.print(Rule("[bold cyan]AI Agent[/bold cyan]"))

    graph = build_graph()

    config = {
        "configurable": {
            "thread_id": "user-2",
        }
    }

    # First message
    result = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "My name is Sajid.",
                }
            ]
        },
        config,
    )

    # Second message - same thread
    result2 = graph.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is my name?",
                }
            ]
        },
        config,
    )

    # Get last AI message
    response = result["messages"][-1]
    response2 = result2["messages"][-1]

    # Extract content
    if hasattr(response, "content"):
        response = response.content

    if hasattr(response2, "content"):
        response2 = response2.content

    console.print(
        Panel(
            response,
            title="[bold green]🤖 Response 1[/bold green]",
            border_style="green",
            padding=(1, 2),
        )
    )

    console.print(
        Panel(
            response2,
            title="[bold green]🤖 Response 2[/bold green]",
            border_style="green",
            padding=(1, 2),
        )
    )

    console.print(Rule("[dim]Done[/dim]"))


if __name__ == "__main__":
    main()
