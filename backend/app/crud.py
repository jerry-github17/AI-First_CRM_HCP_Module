from sqlalchemy.orm import Session

from . import models, schemas


def create_interaction(
    db: Session,
    interaction: schemas.InteractionCreate
):
    db_interaction = models.Interaction(
        **interaction.model_dump()
    )

    db.add(db_interaction)
    db.commit()
    db.refresh(db_interaction)

    return db_interaction


def get_interaction(
    db: Session,
    interaction_id: int
):
    return db.query(models.Interaction).filter(
        models.Interaction.id == interaction_id
    ).first()


def get_hcp_interaction_history(
    db: Session,
    hcp_name: str
):
    return db.query(models.Interaction).filter(
        models.Interaction.hcp_name == hcp_name
    ).all()


def update_interaction(
    db: Session,
    interaction_id: int,
    updated_data: schemas.InteractionUpdate
):
    interaction = db.query(models.Interaction).filter(
        models.Interaction.id == interaction_id
    ).first()

    if interaction:
        update_fields = updated_data.model_dump(
            exclude_unset=True,
            exclude_none=True
        )

        for field, value in update_fields.items():
            setattr(interaction, field, value)

        db.commit()
        db.refresh(interaction)

    return interaction