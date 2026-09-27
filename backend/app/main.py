from fastapi import FastAPI
from app.core.database import engine
from app.models.base import Base
from app.models.payment import Payment
from app.models.payment_event import PaymentEvent

app = FastAPI(
    title="RazorGaurd API",
    description="AI Payment State Consistency & Revenue Recovery Agent",
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)

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