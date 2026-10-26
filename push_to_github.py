#!/usr/bin/env python
"""
Script to push code to GitHub
"""
import os
from git import Repo
from git.exc import InvalidGitRepositoryError

# Project directory
project_dir = r"c:\Users\saksh\Desktop\Ai_chatbot_saksham\AI_Student_Support_Groq"

# GitHub details
github_username = "saksham1819negi"
repo_name = "AI-Student-Support-Bot"
github_url = f"https://github.com/{github_username}/{repo_name}.git"

print("=" * 60)
print("AI Student Support Bot - GitHub Push Script")
print("=" * 60)

try:
    # Try to initialize or open existing repo
    try:
        repo = Repo(project_dir)
        print("✓ Found existing git repository")
    except InvalidGitRepositoryError:
        print("✓ Initializing new git repository...")
        repo = Repo.init(project_dir)

    # Configure git
    print("✓ Configuring git...")
    with repo.config_writer() as git_config:
        git_config.set_value("user", "name", "Saksham Negi")
        git_config.set_value("user", "email", "saksham@example.com")

    # Add all files
    print("✓ Adding all files...")
    repo.git.add(".")

    # Check if there are changes to commit
    if repo.is_dirty(untracked_files=True):
        print("✓ Creating commit...")
        repo.index.commit("Initial commit: AI Student Support Chatbot with Groq API")
        print("✓ Commit created successfully")
    else:
        print("✓ No changes to commit")

    # Add remote
    print("✓ Adding remote repository...")
    try:
        origin = repo.remote("origin")
        origin.set_url(github_url)
        print(f"✓ Remote updated: {github_url}")
    except ValueError:
        origin = repo.create_remote("origin", github_url)
        print(f"✓ Remote created: {github_url}")

    # Set default branch to main
    if repo.active_branch.name != "main":
        repo.heads.main.checkout()
    
    print("\n" + "=" * 60)
    print("NEXT STEPS:")
    print("=" * 60)
    print("1. Go to https://github.com/new")
    print("2. Create a NEW repository named: AI-Student-Support-Bot")
    print("3. Make it PUBLIC")
    print("4. DO NOT initialize with README or .gitignore")
    print("5. Click 'Create repository'")
    print("6. Run this script again: python push_to_github.py")
    print("\nOR use GitHub Desktop:")
    print("1. Download: https://desktop.github.com")
    print("2. Sign in with your GitHub account")
    print("3. File > Clone Repository")
    print("4. https://github.com/saksham1819negi/AI-Student-Support-Bot")
    print("5. Select this folder")
    print("=" * 60)

except Exception as e:
    print(f"✗ Error: {str(e)}")
    print("\nIMPORTANT: Make sure the repository exists on GitHub first!")
    print("Create it at: https://github.com/new")
