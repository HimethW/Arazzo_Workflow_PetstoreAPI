from fastmcp import FastMCP
from arazzo_runner import ArazzoRunner

# Initialize FastMCP server
mcp = FastMCP("Petstore-Multi-Dep", stateless_http=True)

# Load the Arazzo file that contains 3 dependent workflows
runner = ArazzoRunner.from_arazzo_path("./multi_workflow_dep.yaml")

# ── Tool 1: lookupPet workflow (base) ────────────────────────────
@mcp.tool()
async def lookup_pet(id: int) -> str:
    """Look up a pet by its ID using the lookupPet workflow."""
    try:
        result = runner.execute_workflow("lookupPet", {"petId": id})
        if result.outputs:
            return f"Workflow Success. Outputs: {result.outputs}"
        return f"Workflow Result: {result}"
    except Exception as e:
        return f"Workflow Error: {str(e)}"

# ── Tool 2: createAndVerifyPet workflow (calls lookupPet) ────────
@mcp.tool()
async def create_and_verify_pet(id: int, name: str) -> str:
    """Create a new pet and verify it exists. Internally calls the lookupPet workflow."""
    try:
        result = runner.execute_workflow(
            "createAndVerifyPet", {"petId": id, "petName": name}
        )
        if result.outputs:
            return f"Workflow Success. Outputs: {result.outputs}"
        return f"Workflow Result: {result}"
    except Exception as e:
        return f"Workflow Error: {str(e)}"

# ── Tool 3: ensurePetUpdated workflow (calls createAndVerifyPet if needed)
@mcp.tool()
async def ensure_pet_updated(id: int, name: str) -> str:
    """Ensure a pet is updated. Creates the pet first (via createAndVerifyPet) if it doesn't exist."""
    try:
        result = runner.execute_workflow(
            "ensurePetUpdated", {"petId": id, "newName": name}
        )
        if result.outputs:
            return f"Workflow Success. Outputs: {result.outputs}"
        return f"Workflow Result: {result}"
    except Exception as e:
        return f"Workflow Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8003)
