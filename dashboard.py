from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
import time
import datetime

console = Console()
layout = Layout()

layout.split_column(
    Layout(name="header", size=3),
    Layout(name="main")
)
layout["main"].split_row(
    Layout(name="leads"),
    Layout(name="arbitrage_alerts")
)

def generate_hud():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    layout["header"].update(Panel(f"[bold cyan]JARVIS SYSTEM PROTOCOL ACTIVE[/bold cyan] | Time: {current_time}"))
    layout["leads"].update(Panel("[bold green]Inbound Lead Traffic[/bold green]\n- Fremantle Roofers: 2 calls\n- Perth Emergency Plumbing: 1 call", title="B2B Lead Nodes"))
    layout["arbitrage_alerts"].update(Panel("[bold red]Live Market Scraper[/bold red]\n- Awaiting Gumtree data pulse...\n- Marketplace feed: Active", title="Asset Arbitrage"))
    return layout

with Live(generate_hud(), refresh_per_second=1):
    while True:
        time.sleep(1)
