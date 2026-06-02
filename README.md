# AI_Context_System
# 🧠 AI Context Ecosystem & Universal Initializer

This repository holds the central configuration, scripts, and documentation for a zero-waste, high-efficiency AI coding workflow. It is designed to bridge the gap between static knowledge bases (like Obsidian) and autonomous AI coding agents via the Model Context Protocol (MCP).

## 🎯 Purpose
To eliminate "Context Inflation" and token waste when using LLMs for software development. By scaffolding a standardized `docs/ai/` directory in every new project, we provide AI agents with a deterministic map of the codebase, preventing them from blindly scanning thousands of files.

## 📦 Repository Contents
* `init_ai_universal_project.py`: The core Python script that generates the AI context templates (`.cursorrules`, `01_overview.md`, `02_architecture.md`, `03_current_task.md`).
* `BUILD_AND_USE_GUIDE.md`: The complete step-by-step manual on how to configure your IDE, choose your AI clients, and execute the daily workflow.

## 🚀 Quick Start
To initialize the AI context in any new project, run the script from your terminal:

```bash
# For a standard module or small project
python init_ai_universal_project.py my_new_module --size mid

# For a large system (adds roadmap templates)
python init_ai_universal_project.py my_startup_core --size large
