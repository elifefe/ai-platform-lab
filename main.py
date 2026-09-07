from fastapi import FastAPI

app = FastAPI(
    title="AI Platform Lab",
    description="My first containerized API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {"Hello": "World"}