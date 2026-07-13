from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello! My FastAPI app is running on Vercel."}