from fastapi import FastAPI
import router
import uvicorn

app = FastAPI()

@app.get('/')
async def Home():
    return "Welcom,eblan"

app.include_router(router.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)