from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..database import SessionLocal
from .. import schemas, crud


router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_interaction(
    interaction: schemas.InteractionCreate,
    db: Session = Depends(get_db)
):
    return crud.create_interaction(
        db,
        interaction
    )


@router.get("/{interaction_id}")
def get_interaction(
    interaction_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_interaction(
        db,
        interaction_id
    )


@router.get("/hcp/{hcp_name}")
def get_history(
    hcp_name: str,
    db: Session = Depends(get_db)
):
    return crud.get_hcp_interaction_history(
        db,
        hcp_name
    )


@router.put("/{interaction_id}")
def update_interaction(
    interaction_id: int,
    interaction: schemas.InteractionUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_interaction(
        db,
        interaction_id,
        interaction
    )