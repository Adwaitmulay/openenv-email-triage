"""
Email Triage Environment Implementation.
Handles spam detection, department routing, and urgency classification.
"""

from uuid import uuid4
from openenv.core.env_server.interfaces import Environment
from openenv.core.env_server.types import State

try:
    from ..models import EmailTriageAction, EmailTriageObservation
except ImportError:
    from models import EmailTriageAction, EmailTriageObservation


class EmailTriageEnvironment(Environment):
    """Email Triage Environment that classifies emails."""

    SUPPORTS_CONCURRENT_SESSIONS: bool = True

    def __init__(self):
        self._state = State(episode_id=str(uuid4()), step_count=0)

    def reset(self) -> EmailTriageObservation:
        self._state = State(episode_id=str(uuid4()), step_count=0)
        return EmailTriageObservation(
            is_spam=False,
            department=None,
            urgency=None,
            confidence=1.0,
            reasoning="Environment ready. Submit an email to triage.",
            done=False,
            reward=0.0,
        )

    def step(self, action: EmailTriageAction) -> EmailTriageObservation:
        self._state.step_count += 1

        subject = action.email_subject.lower()
        body = action.email_body.lower()
        sender = action.sender.lower()
        text = subject + " " + body + " " + sender

        # --- Spam Detection ---
        spam_keywords = [
            "win", "winner", "prize", "lottery", "free money", "click here",
            "congratulations", "nigerian", "inheritance", "viagra", "casino",
            "make money fast", "earn $", "limited offer", "act now", "urgent offer",
            "no risk", "guaranteed", "million dollars", "you have been selected"
        ]
        spam_score = sum(1 for kw in spam_keywords if kw in text)
        is_spam = spam_score >= 2

        if is_spam:
            return EmailTriageObservation(
                is_spam=True,
                department=None,
                urgency=None,
                confidence=min(0.5 + spam_score * 0.1, 1.0),
                reasoning=f"Detected as spam. Found {spam_score} spam indicators.",
                done=True,
                reward=1.0,
            )

        # --- Department Routing ---
        department = "other"
        dept_confidence = 0.6

        if any(kw in text for kw in ["invoice", "payment", "bill", "charge", "refund", "subscription", "pricing"]):
            department = "billing"
            dept_confidence = 0.9
        elif any(kw in text for kw in ["bug", "error", "crash", "broken", "not working", "issue", "problem", "help", "support"]):
            department = "support"
            dept_confidence = 0.9
        elif any(kw in text for kw in ["buy", "purchase", "demo", "trial", "interested", "quote", "sales", "pricing plan"]):
            department = "sales"
            dept_confidence = 0.85
        elif any(kw in text for kw in ["job", "career", "resume", "hiring", "apply", "hr", "employee", "leave", "salary"]):
            department = "hr"
            dept_confidence = 0.85

        # --- Urgency Classification ---
        urgency = "low"
        urgency_confidence = 0.7

        if any(kw in text for kw in ["urgent", "asap", "immediately", "critical", "emergency", "right now", "server down", "data loss"]):
            urgency = "high"
            urgency_confidence = 0.95
        elif any(kw in text for kw in ["soon", "today", "this week", "follow up", "waiting", "pending"]):
            urgency = "medium"
            urgency_confidence = 0.8

        final_confidence = round((dept_confidence + urgency_confidence) / 2, 2)

        return EmailTriageObservation(
            is_spam=False,
            department=department,
            urgency=urgency,
            confidence=final_confidence,
            reasoning=f"Routed to {department} department with {urgency} urgency.",
            done=True,
            reward=1.0,
        )

    @property
    def state(self) -> State:
        return self._state