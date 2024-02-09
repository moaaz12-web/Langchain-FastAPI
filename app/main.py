from fastapi import FastAPI
from langserve import add_routes
from langchain.chains import ConversationChain
from memory import vectorstore_as_memory
from prompt import PROMPT
from llm import llm

app = FastAPI(title="Retrieval App")

# Initialize the conversation chain with a default memory
memory = vectorstore_as_memory("USER1")
final_chain = ConversationChain(
    llm=llm,
    prompt=PROMPT,
    memory=memory,
    verbose=False
)

# Define a function to update the memory associated with the final_chain
def update_memory(username):
    memory = vectorstore_as_memory(username)
    final_chain.memory = memory

# Define a route to handle API calls
@app.post("/api/{username}")
async def api_endpoint(username: str):
    update_memory(username)
    return {"message": f"Memory updated successfully with username: {username}"}

# Add routes to the FastAPI app
add_routes(app, final_chain)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
