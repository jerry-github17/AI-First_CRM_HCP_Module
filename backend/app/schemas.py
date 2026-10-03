from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class InteractionCreate(BaseModel):
    hcp_name: str
    interaction_type: str
    interaction_date: Optional[datetime] = None
    attendees: Optional[str] = None
    summary: str
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: Optional[str] = None
    outcome: Optional[str] = None
    follow_up_action: Optional[str] = None
    follow_up_date: Optional[datetime] = None


class InteractionUpdate(BaseModel):
    hcp_name: Optional[str] = None
    interaction_type: Optional[str] = None
    interaction_date: Optional[datetime] = None
    attendees: Optional[str] = None
    summary: Optional[str] = None
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: Optional[str] = None
    outcome: Optional[str] = None
    follow_up_action: Optional[str] = None
    follow_up_date: Optional[datetime] = None

    class Config:
        extra = "ignore"


class InteractionResponse(BaseModel):
    id: int
    hcp_name: str
    interaction_type: str
    interaction_date: Optional[datetime] = None
    attendees: Optional[str] = None
    summary: str
    materials_shared: Optional[str] = None
    samples_distributed: Optional[str] = None
    sentiment: Optional[str] = None
    outcome: Optional[str] = None
    follow_up_action: Optional[str] = None
    follow_up_date: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True