from fastapi import FastAPI

app = FastAPI(
    title="RazorGaurd API",
    description="AI Payment State Consistency & Revenue Recovery Agent",
    version="0.1.0",
)

@app.get("/")
def root():
    return {"name": "RazorGuard",
            "status": "running"
            }

@app.get("/health")
def health():
    return {
        "status": "SAB THEEK HAI"
        }