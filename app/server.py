from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes

app = FastAPI()

from pirate_speak.chain import chain as pirate_speak_chain
from csv_agent import agent_executor as csv_agent_chain

 

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, pirate_speak_chain, path="/pirate-speak")
add_routes(app, csv_agent_chain, path="/csv-agent")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
