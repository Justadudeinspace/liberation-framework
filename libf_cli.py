#!/usr/bin/env python3
import os
import click
import json
from datetime import datetime

LIBF_DIR = os.path.expanduser("~/blux-memory")
SNAPSHOT_LOG = os.path.join(LIBF_DIR, "snapshot_history.json")

def ensure_dirs():
    os.makedirs(LIBF_DIR, exist_ok=True)
    if not os.path.exists(SNAPSHOT_LOG):
        with open(SNAPSHOT_LOG, 'w') as f:
            json.dump([], f)

@click.group()
def cli():
    """🔧 Liberation Framework CLI – .libf memory toolkit"""
    ensure_dirs()

@cli.command()
@click.option("--name", prompt="Snapshot name", help="Unique name for this .libf state")
@click.option("--desc", prompt="Short description", help="Description of the current task")
@click.option("--tasks", prompt="Comma-separated task list", help="What are you working on?")
def snapshot(name, desc, tasks):
    tasks_list = [t.strip() for t in tasks.split(",")]
    cwd = os.getcwd()
    files = os.listdir(cwd)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    snapshot_data = {
        "name": name,
        "timestamp": timestamp,
        "description": desc,
        "tasks": tasks_list,
        "project": {
            "name": os.path.basename(cwd),
            "cwd": cwd,
            "files": files
        }
    }

    filename = f"{name}.libf"
    path = os.path.join(LIBF_DIR, filename)
    with open(path, 'w') as f:
        f.write(generate_libf(snapshot_data))

    with open(SNAPSHOT_LOG, 'r+') as log:
        data = json.load(log)
        data.append(snapshot_data)
        log.seek(0)
        json.dump(data, log, indent=2)

    click.echo(f"✅ Snapshot created: {path}")

def generate_libf(data):
    return f"""# Liberation Interface Base File
# Snapshot: {data['name']}
# Timestamp: {data['timestamp']}

[PROJECT]
Name: {data['project']['name']}
Location: {data['project']['cwd']}
Files: {", ".join(data['project']['files'])}

[STATE]
Description: {data['description']}
Pending Tasks:
{chr(10).join(['- ' + task for task in data['tasks']])}

[COMMANDS]
Sol.load(.libf)
Sol.snapshot("current")
Sol.flow("continue")
"""

@cli.command()
def list():
    with open(SNAPSHOT_LOG) as f:
        data = json.load(f)
    for snap in data:
        click.echo(f"[{snap['timestamp']}] {snap['name']} - {snap['description']}")

@cli.command()
@click.argument("keyword")
def search(keyword):
    with open(SNAPSHOT_LOG) as f:
        data = json.load(f)
    found = [s for s in data if keyword.lower() in s['name'].lower() or keyword.lower() in s['description'].lower()]
    if not found:
        click.echo("⚠️ No results.")
    else:
        for snap in found:
            click.echo(f"🔸 {snap['name']} – {snap['description']}")

@cli.command()
@click.argument("name")
def show(name):
    path = os.path.join(LIBF_DIR, f"{name}.libf")
    if not os.path.exists(path):
        click.echo("❌ Snapshot not found.")
        return
    with open(path) as f:
        click.echo(f.read())

if __name__ == "__main__":
    cli()
