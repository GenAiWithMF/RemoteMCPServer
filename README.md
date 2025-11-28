# ExpenseTracker FastMCP Project

This is an **Expense Tracker** built using [FastMCP]((https://RemoteMcpServer.fastmcp.app/mcp)) and `aiosqlite`. It supports **proxy connections** for remote clients like Claude, as well as local and cloud deployments.

---

## Features

* Add, list, and summarize expenses
* Asynchronous SQLite database
* Default categories with optional custom categories
* Proxy support for connecting remote clients
* Fully compatible with FastMCP tools and resources

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/ExpenseTracker.git
cd ExpenseTracker
```

2. **Install dependencies:**

```bash
pip install fastmcp aiosqlite
```

3. **Optional:** Make sure Python >= 3.13 is installed.

---

2️⃣ Run Server Locally
# Development mode (hot reload)
uv run fastmcp dev Main.py

# Normal run
uv run fastmcp run Main.py

Server will start on http://0.0.0.0:8000 by default.

---

3️⃣ Connect Claude Desktop or Other Clients via Proxy
# Start proxy to connect remote clients like Claude
uv run fastmcp install claude-desktop proxyfile.py

Or use Python:

from fastmcp import FastMCP

# Connect to your FastMCP Cloud server
mcp = FastMCP.as_proxy(
    "https://Maryams.fastmcp.app/mcp",
    name="Maryam Server Proxy"
)
```

### Example CLI for connecting a local proxy to Claude Desktop

```bash
# Run proxy server to connect Claude
uv run fastmcp install claude-desktop proxy-server.py
```

* This allows Claude (or other clients) to connect without needing FastMCP Pro.
* Use the `/mcp` URL from FastMCP Cloud if your server is deployed remotely.

---

## FastMCP Tool Commands

### Add Expense

```python
await add_expense(date="2025-11-28", amount=100.5, category="Food & Dining")
```

### List Expenses

```python
await list_expenses(start_date="2025-11-01", end_date="2025-11-28")
```

### Summarize Expenses

```python
await summarize(start_date="2025-11-01", end_date="2025-11-28", category="Food & Dining")
```

### Categories Resource

```python
categories()  # Returns JSON of default or custom categories
```

---

## Deployment on FastMCP Cloud

1. Sign in to [FastMCP Cloud](https://fastmcp.app/).
2. Create a new project and upload `MCPServer.py`.
3. Choose **public** for open access or **private** with API token.
4. Use the `/mcp` URL for remote connections.

---

## Notes

* Database is stored in a temporary folder for write access.
* Default categories used if `categories.json` does not exist.
* Fully compatible with Claude and other FastMCP clients.


