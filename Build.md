# 🏗️ Building and Using the AI Context System: From Zero to Hero

This guide explains how to set up your local environment to maximize AI autonomy while minimizing API costs (via OpenRouter), and how to execute the workflow daily.

---

## Phase 1: Global Setup (Do this once)

1. **Clone this repository** to a permanent location on your machine (e.g., `~/Projects/ai-workflow-config`).
2. **Set up a global alias** (optional but recommended) so you can call the initialization script from anywhere.
   * *Linux/macOS:* Add `alias init-ai="python ~/Projects/ai-workflow-config/init_ai_universal_project.py"` to your `.bashrc` or `.zshrc`.
3. **Connect to Obsidian:** Open Obsidian and click "Open folder as vault". Select the root folder of your newly initialized project (or your main projects directory) to visualize the Markdown links in the Graph View.

---

## Phase 2: Choose Your Client Option

Depending on your current task and environment, you can interface with this system using one of two methods.

### Option A: "Vibe Coding" (GUI Agents)
Best for visual development, frontend/backend integration, and reading through complex directory structures.

* **The Tool:** [Roo Code](https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline) (VS Code Extension) or [Cursor IDE](https://www.cursor.com/).
* **The Setup:**
  1. Install Roo Code in VS Code.
  2. Set the API Provider to **OpenRouter** and paste your API key.
  3. Configure the MCP Filesystem Server. In Roo Code settings -> MCP Servers, add:
     ```json
     {
       "mcpServers": {
         "filesystem": {
           "command": "npx",
           "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/your/projects/dir"]
         }
       }
     }
     ```
* **How it works:** The agent lives in your sidebar. It uses MCP to silently read your `docs/ai/00_Project_Hub.md` and autonomously opens/edits the FastAPI routes or Dockerfiles you need.

### Option B: The CLI Agent
Best for headless servers, SSH sessions over Tailscale (e.g., working directly on your local Mini PC server), or pure backend logic implementation.

* **The Tool:** [Aider](https://aider.chat/)
* **The Setup:**
  1. Install Aider globally: `pip install aider-chat`
  2. Export your OpenRouter key: `export OPENROUTER_API_KEY="your-key"`
* **How it works:** You run Aider directly in the terminal of your project folder. 
  * Command: `aider --model openrouter/anthropic/claude-3.5-sonnet`
  * Instead of MCP, Aider manages context by adding files to the chat. You simply add the context file: `/add docs/ai/03_current_task.md` and tell it to execute the task.

---

## Phase 3: The Daily Workflow

Regardless of whether you use the GUI or CLI client, you must follow this 3-step loop to prevent hallucinations and token waste.

### Step 1: "Step Zero" (Manual Brain Dump)
*After running the Python initialization script, the files are empty templates.*
Before asking the AI to write a single line of code, open the `docs/ai/` files.
* Write your core stack in `02_architecture.md`.
* Write your immediate goal in `03_current_task.md` (e.g., *"Set up the initial SQLAlchemy models for the inventory system"*).

### Step 2: The Action Prompt
Do not dump your entire codebase into the prompt. Use a small, deterministic instruction.
* **In Roo Code:** "Use your MCP tool to read `docs/ai/00_Project_Hub.md`, navigate to the current task, and execute it."
* **In Aider:** "/add docs/ai/03_current_task.md \n Read this task and implement the required changes in `src/models.py`."

### Step 3: The Save State (Crucial)
When the feature works, you must explicitly tell the AI to update its own memory before you close the editor or end the terminal session.
* **Prompt:** "Update `docs/ai/03_current_task.md`. Document the models we just built in the 'Context' section, and set the 'Immediate Goal' for tomorrow to building the FastAPI endpoints for these models."