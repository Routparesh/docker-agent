from agent.planner import is_dockerfile_request, plan_devops_action, is_question
from agent.executor import execute
from agent.dockerfile_generator import generate_dockerfile
from agent.qa import answer_question
from rich.console import Console

console = Console()

console.print("[bold green]DevOps Agent (Local LLM + Docker MCP) Ready[/bold green]")

while True:
    user_input = console.input("\n[bold cyan]>> [/bold cyan]")

    if user_input.lower() in ["exit", "quit"]:
        break

    # 1️⃣ QUESTIONS → ANSWER
    if is_question(user_input):
        answer = answer_question(user_input)
        console.print(answer)
        continue

    # Dockerfile generation
    if is_dockerfile_request(user_input):
        app_type = console.input("App type (node/python/java/go/static): ")
        port = console.input("Port: ")
        start_cmd = console.input("Start command (optional): ")

        dockerfile = generate_dockerfile(app_type, port, start_cmd)

        console.print("\n[bold yellow]Generated Dockerfile:[/bold yellow]\n")
        console.print(dockerfile)

        save = console.input("\nSave as Dockerfile? (yes/no): ")
        if save.lower() == "yes":
            with open("Dockerfile", "w") as f:
                f.write(dockerfile)
            console.print("[green]Dockerfile saved successfully[/green]")
        continue

    # Docker MCP actions
    steps, container = plan_devops_action(user_input)

    if not steps:
        console.print("[red]No safe actions identified[/red]")
        continue

    console.print(f"[bold]Execution Plan:[/bold] {steps}")
    approve = console.input("Approve execution? (yes/no): ")

    if approve.lower() != "yes":
        console.print("[yellow]Execution cancelled[/yellow]")
        continue

    execute(steps, container)
    console.print("[green]Execution completed[/green]")
