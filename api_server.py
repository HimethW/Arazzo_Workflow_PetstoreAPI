from fastmcp import FastMCP
import httpx

# Initialize FastMCP server
mcp = FastMCP("Petstore-APIs", stateless_http=True)
PETSTORE_BASE = "https://petstore3.swagger.io/api/v3"

@mcp.tool()
async def get_pet(id: int) -> str:
    """Fetch a pet by ID."""
    async with httpx.AsyncClient() as client:
        resp = await client.get(f"{PETSTORE_BASE}/pet/{id}")
        return resp.text if resp.status_code == 200 else f"Error {resp.status_code}"

@mcp.tool()
async def add_pet(id: int, name: str) -> str:
    """Add a new pet."""
    payload = {"id": id, "name": name, "photoUrls": ["http://example.com/pet.jpg"]}
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{PETSTORE_BASE}/pet", json=payload)
        return "Pet added" if resp.status_code == 200 else "Failed to add pet"

@mcp.tool()
async def update_pet(id: int, name: str) -> str:
    """Update a pet's name via query parameters."""
    async with httpx.AsyncClient() as client:
        resp = await client.post(f"{PETSTORE_BASE}/pet/{id}", params={"name": name})
        return "Pet updated" if resp.status_code == 200 else f"Update failed: {resp.status_code}"

if __name__ == "__main__":
    # Run as streamable-http on port 8000
    mcp.run(transport="http",host="127.0.0.1", port=8001)