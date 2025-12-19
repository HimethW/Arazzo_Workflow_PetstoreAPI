from fastmcp import FastMCP
from arazzo_runner import ArazzoRunner

# Initialize FastMCP server
mcp = FastMCP("Petstore-Workflow", stateless_http=True)

# Need to ensure petstore_workflow.yaml and openapi.yaml are in this directory or else need to provide the path
runner = ArazzoRunner.from_arazzo_path("./petstore_workflow2.yaml")

@mcp.tool()
async def run_upsert_workflow(id: int, name: str) -> str:  #here it was pet_id and new_name earlier
    """Executes the Arazzo 'ensurePetExists' workflow logic."""
    try:
        result = runner.execute_workflow(
            "ensurePetExists", 
            {"petId": id, "newName": name}      #here it was pet_id and new_name earlier
        )
        return f"Workflow Result: {result}"
    except Exception as e:
        return f"Workflow Error: {str(e)}"

if __name__ == "__main__":
    # Run as http on port 8000. if streamable-http was used then host and port arguments cannot be passed
    mcp.run(transport="http",host="127.0.0.1", port=8000)