This code uses python 3.13 as arazzo-runner needs python 3.11 or higher
the environment is at C:\venvs
packages:
pip install arazzo-runner
python -m pip install httpx fastmcp

PS: keep in mind that use from fastmcp import FastMCP and not from mcp.server.fast mcp import FastMCP
because in the second case the endpoint has to be localhost:8000/mcp/mcp (an extra mcp is added) and hence will not work during the connection process

Use the petstore_workflow2.yaml to handle both the success and failure operations