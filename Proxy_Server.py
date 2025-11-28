from fastmcp import FastMCP


##Create a proxy to your remote FastMCP Cloud server
##FastMCP Cloud use Streamable HTTP (default), so just use the /mp URL

mcp = FastMCP.as_proxy(
    "https://RemoteMcpServer.fastmcp.app/mcp",
    name="Maryam Server Proxy"
)


if __name__ == "__main__":
    ##This runs via STDIO ,which Claude Destop can connect to
    mcp.run()