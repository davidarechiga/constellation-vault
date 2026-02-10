#!/usr/bin/env python3
"""
TaskNotes Migration Script
Converts inline checkbox tasks to individual TaskNotes files with YAML frontmatter
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from datetime import datetime

# Configuration
VAULT_PATH = "/Users/davidarechiga/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain (iCloud)"
TASK_FOLDER = "0 📡 Signal Relay/Tasks"
SOURCE_FILES = [
    "1 🔨 The Foundry/1 Baby Prep - Cyrus/1 Baby Prep - Cyrus.md",
    "1 🔨 The Foundry/6 Career Transition 2026/6 Career Transition 2026.md",
]

# Priority mapping
PRIORITY_MAP = {
    "⏫": "high",
    "🔼": "normal",
    "🔽": "low",
}

# Project mapping for task categorization
PROJECT_FOLDERS = {
    "1 Baby Prep - Cyrus": "Baby Prep",
    "6 Career Transition 2026": "Career Transition",
}


class TaskMetadata:
    """Represents extracted task metadata"""
    def __init__(self):
        self.title: str = ""
        self.owner: Optional[str] = None
        self.due: Optional[str] = None
        self.priority: str = "normal"
        self.status: str = "open"
        self.completed_date: Optional[str] = None
        self.contexts: List[str] = []
        self.tags: List[str] = ["task"]
        self.project_link: str = ""
        self.body_content: str = ""
        self.subtasks: List[str] = []
        self.context_notes: List[str] = []


def slugify(text: str) -> str:
    """Convert text to URL-friendly slug"""
    # Remove special characters, convert to lowercase
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def extract_task_metadata(task_line: str) -> TaskMetadata:
    """Parse inline task line and extract metadata"""
    metadata = TaskMetadata()

    # Determine status
    if task_line.strip().startswith("- [x]"):
        metadata.status = "done"
    elif task_line.strip().startswith("- [ ]"):
        metadata.status = "open"
    else:
        return None

    # Extract owner
    owner_match = re.search(r'\[owner:: ([^\]]+)\]', task_line)
    if owner_match:
        metadata.owner = owner_match.group(1).strip()

    # Extract due date
    due_match = re.search(r'📅 (\d{4}-\d{2}-\d{2})', task_line)
    if due_match:
        metadata.due = due_match.group(1)

    # Extract completion date
    completed_match = re.search(r'✅ (\d{4}-\d{2}-\d{2})', task_line)
    if completed_match:
        metadata.completed_date = completed_match.group(1)

    # Extract priority
    for emoji, priority in PRIORITY_MAP.items():
        if emoji in task_line:
            metadata.priority = priority
            break

    # Extract contexts (e.g., @home, @work)
    context_matches = re.findall(r'@(\w+)', task_line)
    metadata.contexts = context_matches

    # Extract task title (clean)
    # Remove everything after first metadata marker
    title_match = re.search(r'- \[.\] (.+?)(?:\[owner|📅|⏫|🔼|🔽|✅|\[migrated\]|$)', task_line)
    if title_match:
        title = title_match.group(1).strip()
        # Remove wikilinks from title
        title = re.sub(r'\[\[([^\]]+)\]\]', r'\1', title)
        metadata.title = title

    return metadata


def parse_task_body(lines: List[str], start_index: int) -> Tuple[List[str], List[str], int]:
    """
    Parse lines following a task to extract subtasks and context
    Returns: (subtasks, context_notes, next_line_index)
    """
    subtasks = []
    context_notes = []
    i = start_index + 1

    while i < len(lines):
        line = lines[i]

        # Stop if we hit a non-indented line (next top-level item)
        if line and not line.startswith('  '):
            break

        # Skip empty lines
        if not line.strip():
            i += 1
            continue

        # Remove indentation for processing
        content = line[2:] if line.startswith('  ') else line

        # Check if it's a subtask
        if content.strip().startswith('- [ ]') or content.strip().startswith('- [x]'):
            subtasks.append(content)
        # Check if it's context (bold markers like **Done when**, **Why critical**)
        elif content.strip().startswith('**') or content.strip().startswith('-'):
            context_notes.append(content)

        i += 1

    return subtasks, context_notes, i


def generate_frontmatter(metadata: TaskMetadata) -> str:
    """Generate YAML frontmatter for TaskNote"""
    frontmatter = "---\n"
    frontmatter += f"tags:\n"
    for tag in metadata.tags:
        frontmatter += f"  - {tag}\n"

    frontmatter += f'title: "{metadata.title}"\n'
    frontmatter += f"status: {metadata.status}\n"

    if metadata.priority != "normal":
        frontmatter += f"priority: {metadata.priority}\n"

    if metadata.due:
        frontmatter += f'due: "{metadata.due}"\n'

    if metadata.owner:
        frontmatter += f"owner: {metadata.owner}\n"

    if metadata.completed_date:
        frontmatter += f'completedDate: "{metadata.completed_date}"\n'

    if metadata.project_link:
        frontmatter += f"projects:\n"
        frontmatter += f'  - "[[{metadata.project_link}]]"\n'

    if metadata.contexts:
        frontmatter += f"contexts:\n"
        for context in metadata.contexts:
            frontmatter += f"  - {context}\n"

    frontmatter += "---\n\n"
    return frontmatter


def generate_task_body(metadata: TaskMetadata) -> str:
    """Generate task note body content"""
    body = ""

    # Add subtasks section if present
    if metadata.subtasks:
        body += "## Action Steps\n\n"
        for subtask in metadata.subtasks:
            body += f"{subtask}\n"
        body += "\n"

    # Add context notes
    if metadata.context_notes:
        body += "## Context\n\n"
        for note in metadata.context_notes:
            body += f"{note}\n"
        body += "\n"

    return body.strip()


def create_unique_filename(base_slug: str, folder_path: Path) -> str:
    """Ensure filename is unique by appending number if needed"""
    filename = f"{base_slug}.md"
    filepath = folder_path / filename

    if not filepath.exists():
        return filename

    # File exists, append number
    counter = 2
    while True:
        filename = f"{base_slug}-{counter}.md"
        filepath = folder_path / filename
        if not filepath.exists():
            return filename
        counter += 1


def migrate_file(file_path: str, project_name: str) -> int:
    """
    Migrate tasks from a source file to TaskNotes format
    Returns number of tasks migrated
    """
    full_path = Path(VAULT_PATH) / file_path

    if not full_path.exists():
        print(f"⚠️  Source file not found: {file_path}")
        return 0

    # Determine target folder
    subfolder = PROJECT_FOLDERS.get(project_name, "")
    if subfolder:
        task_folder = Path(VAULT_PATH) / TASK_FOLDER / subfolder
    else:
        task_folder = Path(VAULT_PATH) / TASK_FOLDER

    task_folder.mkdir(parents=True, exist_ok=True)

    # Read source file
    with open(full_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    migrated_count = 0
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if line is a top-level task (not indented)
        if re.match(r'^- \[.\]', line):
            # Extract metadata
            metadata = extract_task_metadata(line)

            if not metadata or not metadata.title:
                i += 1
                continue

            # Set project link
            metadata.project_link = project_name

            # Parse task body (subtasks and context)
            subtasks, context_notes, next_i = parse_task_body(lines, i)
            metadata.subtasks = subtasks
            metadata.context_notes = context_notes

            # Generate filename
            slug = slugify(metadata.title)
            filename = create_unique_filename(slug, task_folder)
            task_path = task_folder / filename

            # Generate task content
            frontmatter = generate_frontmatter(metadata)
            body = generate_task_body(metadata)
            task_content = frontmatter + body

            # Write task file
            with open(task_path, 'w', encoding='utf-8') as f:
                f.write(task_content)

            print(f"✅ Migrated: {metadata.title} -> {subfolder}/{filename}")
            migrated_count += 1

            # Move to next task
            i = next_i
        else:
            i += 1

    return migrated_count


def main():
    """Main migration execution"""
    print("=" * 60)
    print("TaskNotes Migration Script")
    print("=" * 60)
    print()

    total_migrated = 0

    for source_file in SOURCE_FILES:
        # Extract project name from file path
        project_name = Path(source_file).stem

        print(f"\n📁 Processing: {source_file}")
        print(f"   Project: {project_name}")

        count = migrate_file(source_file, project_name)
        total_migrated += count

        print(f"   → {count} tasks migrated")

    print()
    print("=" * 60)
    print(f"✅ Migration Complete!")
    print(f"   Total tasks migrated: {total_migrated}")
    print("=" * 60)


if __name__ == "__main__":
    main()
