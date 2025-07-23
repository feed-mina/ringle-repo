from pydantic import BaseModel

class MockPaymentRequest(BaseModel):
    user_id: str
    membership_id: str

