from typing import Any

import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("pdl-sre-agent")

@mcp.tool()
async def get_alerts(service: str) -> str:
    """Get alerts for a service

    Args:
        state: valid service name
    """
    return "No active alerts for this service: " + service

def main():
    # Initialize and run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()