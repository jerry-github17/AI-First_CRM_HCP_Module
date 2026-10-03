from langchain_core.tools import tool
from sqlalchemy.orm import Session

from .. import crud, schemas
from ..database import SessionLocal


def validate_interaction_id(interaction_id):
    try:
        return int(interaction_id)
    except (ValueError, TypeError):
        return None


def interaction_to_dict(result):
    return {
        "id": result.id,
        "hcp_name": result.hcp_name,
        "interaction_type": result.interaction_type,
        "interaction_date": str(result.interaction_date),
        "attendees": result.attendees,
        "summary": result.summary,
        "materials_shared": result.materials_shared,
        "samples_distributed": result.samples_distributed,
        "sentiment": result.sentiment,
        "outcome": result.outcome,
        "follow_up_action": result.follow_up_action,
        "follow_up_date": str(result.follow_up_date)
    }


@tool
def log_interaction(
    hcp_name: str,
    interaction_type: str,
    summary: str,
    interaction_date: str = None,
    attendees: str = None,
    materials_shared: str = None,
    samples_distributed: str = None,
    sentiment: str = None,
    outcome: str = None,
    follow_up_action: str = None,
    follow_up_date: str = None
):
    """
    Logs a new interaction with an HCP.
    Use this when the user wants to create a new interaction.
    """

    db: Session = SessionLocal()

    try:
        interaction = schemas.InteractionCreate(
            hcp_name=hcp_name,
            interaction_type=interaction_type,
            summary=summary,
            interaction_date=interaction_date,
            attendees=attendees,
            materials_shared=materials_shared,
            samples_distributed=samples_distributed,
            sentiment=sentiment,
            outcome=outcome,
            follow_up_action=follow_up_action,
            follow_up_date=follow_up_date
        )

        result = crud.create_interaction(
            db,
            interaction
        )

        return {
            "status": "success",
            "message": "Interaction logged successfully",
            "interaction": interaction_to_dict(result)
        }

    finally:
        db.close()


@tool
def get_interaction(interaction_id: str):
    """
    Retrieve a specific interaction.

    interaction_id must be a numeric ID only.
    """

    numeric_id = validate_interaction_id(interaction_id)

    if numeric_id is None:
        return {
            "message": "Invalid interaction ID. Please provide a numeric ID."
        }

    db: Session = SessionLocal()

    try:
        result = crud.get_interaction(
            db,
            numeric_id
        )

        if result:
            return interaction_to_dict(result)

        return {
            "message": "Interaction not found"
        }

    finally:
        db.close()


@tool
def get_hcp_interaction_history(hcp_name: str):
    """
    Retrieve previous interactions for an HCP by name.
    """

    db: Session = SessionLocal()

    try:
        results = crud.get_hcp_interaction_history(
            db,
            hcp_name
        )

        return [
            interaction_to_dict(item)
            for item in results
        ]

    finally:
        db.close()


@tool
def edit_interaction(
    interaction_id: str,
    hcp_name: str = None,
    interaction_type: str = None,
    interaction_date: str = None,
    attendees: str = None,
    summary: str = None,
    materials_shared: str = None,
    samples_distributed: str = None,
    sentiment: str = None,
    outcome: str = None,
    follow_up_action: str = None,
    follow_up_date: str = None
):
    """
    Modify an existing interaction.

    interaction_id MUST be numeric.
    """

    numeric_id = validate_interaction_id(interaction_id)

    if numeric_id is None:
        return {
            "message": "Invalid interaction ID. Please provide a numeric ID."
        }

    db: Session = SessionLocal()

    try:
        update_dict = {
            "hcp_name": hcp_name,
            "interaction_type": interaction_type,
            "interaction_date": interaction_date,
            "attendees": attendees,
            "summary": summary,
            "materials_shared": materials_shared,
            "samples_distributed": samples_distributed,
            "sentiment": sentiment,
            "outcome": outcome,
            "follow_up_action": follow_up_action,
            "follow_up_date": follow_up_date
        }

        update_dict = {
            key: value
            for key, value in update_dict.items()
            if value is not None
        }

        update_data = schemas.InteractionUpdate(
            **update_dict
        )

        result = crud.update_interaction(
            db,
            numeric_id,
            update_data
        )

        if result:
            return {
                "status": "success",
                "message": "Interaction updated",
                "interaction": interaction_to_dict(result)
            }

        return {
            "message": "Interaction not found"
        }

    finally:
        db.close()


@tool
def schedule_follow_up(
    interaction_id: str,
    follow_up_date: str
):
    """
    Schedule a follow-up date for an existing interaction.
    """

    numeric_id = validate_interaction_id(interaction_id)

    if numeric_id is None:
        return {
            "message": "Invalid interaction ID. Please provide a numeric ID."
        }

    db: Session = SessionLocal()

    try:
        update_data = schemas.InteractionUpdate(
        **{
            "follow_up_date": follow_up_date
        }
        )

        result = crud.update_interaction(
            db,
            numeric_id,
            update_data
        )

        if result:
            return {
                "status": "success",
                "message": "Follow-up scheduled",
                "interaction": interaction_to_dict(result)
            }

        return {
            "message": "Interaction not found"
        }

    finally:
        db.close()