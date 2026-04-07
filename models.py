from openenv.core.env_server.types import Action, Observation
from pydantic import Field
from typing import Optional


class EmailTriageAction(Action):
    """Action: submit an email for triage."""

    email_subject: str = Field(..., description="Subject line of the email")
    email_body: str = Field(..., description="Body content of the email")
    sender: str = Field(..., description="Email address of the sender")


class EmailTriageObservation(Observation):
    """Observation: result of triaging the email."""

    is_spam: bool = Field(default=False, description="Whether the email is spam")
    department: Optional[str] = Field(default=None, description="Department to route to: billing, support, sales, hr, other")
    urgency: Optional[str] = Field(default=None, description="Urgency level: low, medium, high")
    confidence: float = Field(default=0.0, description="Confidence score of the triage decision")
    reasoning: str = Field(default="", description="Explanation of the triage decision")