#!/usr/bin/env python3
"""setup_hierarchy.py

A tiny helper that creates the folder & file structure described in the
AI Information Hierarchy for Cybertraining EU B.V.

Usage:
    python3 setup_hierarchy.py               # creates hierarchy in the current directory
    python3 setup_hierarchy.py /path/to/dir   # creates hierarchy at a custom location

The script is deliberately dependency‑free – it only uses the Python stdlib.
"""

import sys
import os
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuration – adjust only if you want different default names
# ---------------------------------------------------------------------------
DEFAULT_BASE = Path.cwd()
BUSINESS_FOLDER = "My Business"
PROJECT_NAME = "CyberPulse Platform"  # default project folder name

BUSINESS_FILES = [
    "About Me.md",
    "About My Business.md",
    "About My Voice.md",
    "My Offers.md",
]

PROJECT_SUBFOLDERS = ["Instructions", "Voice", "References", "Examples", "Notes"]

INSTRUCTIONS_FILE = "Instructions.md"

# ---------------------------------------------------------------------------
def create_folder(path: Path):
    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")

def create_file(path: Path, content: str = ""):
    if not path.exists():
        path.write_text(content, encoding="utf-8")
        print(f"Created file: {path}")
    else:
        print(f"File already exists: {path}")

def main():
    # Determine base directory
    if len(sys.argv) > 1:
        base_dir = Path(sys.argv[1]).expanduser().resolve()
    else:
        base_dir = DEFAULT_BASE

    print(f"Initialising AI Information Hierarchy in: {base_dir}")

    # 1️⃣ Create the "My Business" folder and core files
    business_dir = base_dir / BUSINESS_FOLDER
    create_folder(business_dir)
    for fname in BUSINESS_FILES:
        file_path = business_dir / fname
        # placeholder heading – the interview prompt will replace the content later
        placeholder = f"# {fname.replace('.md', '')}\n\n*Add your content here using Prompt 2.*\n"
        create_file(file_path, placeholder)

    # 2️⃣ Create a sample project folder (CyberPulse Platform)
    project_dir = base_dir / PROJECT_NAME
    create_folder(project_dir)
    for sub in PROJECT_SUBFOLDERS:
        sub_path = project_dir / sub
        create_folder(sub_path)
        # create empty README for each sub‑folder (optional)
        # create_file(sub_path / "README.md", f"# {sub} folder – leave empty for now\n")
    # Create an empty Instructions.md inside the Instructions sub‑folder
    instr_path = project_dir / "Instructions" / INSTRUCTIONS_FILE
    create_file(instr_path, "# Instructions\n\n*Add project‑specific instructions using Prompt 3.*\n")

    # 3️⃣ Create a minimal .gitignore (ignore temporary files)
    gitignore_path = base_dir / ".gitignore"
    if not gitignore_path.exists():
        gitignore_content = "# Ignore Python byte‑code\n__pycache__/\n*.pyc\n\n# Editor swap files\n*~\n*.swp\n"
        create_file(gitignore_path, gitignore_content)
    else:
        print(".gitignore already exists – skipping.")

    print("\nSetup complete! 🎉")
    print("Next steps:")
    print("  1. Open the generated markdown files and fill them using the prompt templates.")
    print("  2. Initialise a Git repo if you want version control: `git init && git add . && git commit -m \"Initial hierarchy\"`.")
    print("  3. When starting a new AI chat, point the model to this folder so it has all context.")

if __name__ == "__main__":
    main()
