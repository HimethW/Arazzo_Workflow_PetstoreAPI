from fastmcp import FastMCP
from arazzo_runner import ArazzoRunner

# Initialize FastMCP server
mcp = FastMCP("Petstore-Multi-Indep", stateless_http=True)

# Load the Arazzo file that contains 3 independent workflows
runner = ArazzoRunner.from_arazzo_path("./multi_workflow_indep.yaml")

# ── Tool 1: lookupPet workflow ───────────────────────────────────
@mcp.tool()
async def lookup_pet(pet_id: int) -> str:
    """Look up a pet by its ID using the lookupPet workflow."""
    try:
        result = runner.execute_workflow("lookupPet", {"petId": pet_id})
        if result.outputs:
            return f"Workflow Success. Outputs: {result.outputs}"
        return f"Workflow Result: {result}"
    except Exception as e:
        return f"Workflow Error: {str(e)}"

# ── Tool 2: createNewPet workflow ────────────────────────────────
@mcp.tool()
async def create_new_pet(pet_id: int, new_name: str) -> str:
    """Create a new pet and verify it was added using the createNewPet workflow."""
    try:
        result = runner.execute_workflow(
            "createNewPet", {"petId": pet_id, "petName": new_name}
        )
        if result.outputs:
            return f"Workflow Success. Outputs: {result.outputs}"
        return f"Workflow Result: {result}"
    except Exception as e:
        return f"Workflow Error: {str(e)}"

# ── Tool 3: updatePetInfo workflow ───────────────────────────────
@mcp.tool()
async def update_pet_info(pet_id: int, new_name: str) -> str:
    """Update an existing pet's name using the updatePetInfo workflow."""
    try:
        result = runner.execute_workflow(
            "updatePetInfo", {"petId": pet_id, "newName": new_name}
        )
        if result.outputs:
            return f"Workflow Success. Outputs: {result.outputs}"
        return f"Workflow Result: {result}"
    except Exception as e:
        return f"Workflow Error: {str(e)}"

if __name__ == "__main__":
    mcp.run(transport="http", host="127.0.0.1", port=8004)
