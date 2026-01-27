
# SRE Agent MCP Server

This MCP server is demonstrating how we can utilize the Agents

## Deployment

To deploy this project run

```bash
# clone this repo in home directory
git clone 

cd sre-agent-mcp-server

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx
```

## Use Claude Desktop (MAC) to start the MCP server

Download claude Desktop: https://claude.com/download

```bash
vi ~/Library/Application\ Support/Claude/claude_desktop_config.json

{
  "mcpServers": {
    "sre-agent-mcp-server": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/PARENT/FOLDER/sre-agent-mcp-server",
        "run",
        "agent.py"
      ]
    }
  }
}
```

## Test with Connector

Restart the claude Application

Let’s make sure Claude for Desktop is picking up the tool we’ve exposed in our sre-agent-mcp-server.

Click on + sign here:

After clicking on the plus icon, hover over the “Connectors” menu. You should see the weather servers listed:

Make sure you uncheck web search to avoid searching out side sre-agent mcp server
