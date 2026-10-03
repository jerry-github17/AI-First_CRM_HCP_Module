# from sqlalchemy import Column, Integer, String, Text, DateTime
# from sqlalchemy.sql import func

# from app.database import Base


# class Interaction(Base):
#     __tablename__ = "interactions"

#     id = Column(Integer, primary_key=True, index=True)

#     hcp_name = Column(String(255), nullable=False)
#     interaction_type = Column(String(100), nullable=True)
#     interaction_date = Column(DateTime, nullable=True)

#     topics_discussed = Column(Text, nullable=True)
#     sentiment = Column(String(50), nullable=True)
#     outcome = Column(Text, nullable=True)
#     follow_up_action = Column(Text, nullable=True)

#     created_at = Column(
#         DateTime(timezone=True),
#         server_default=func.now()
#     )

#     updated_at = Column(
#         DateTime(timezone=True),
#         server_default=func.now(),
#         onupdate=func.now()
#     )


from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base


class Interaction(Base):

    __tablename__ = "interactions"

    id = Column(Integer, primary_key=True, index=True)

    hcp_name = Column(String, nullable=False)
    interaction_type = Column(String)

    interaction_date = Column(DateTime, nullable=True)

    attendees = Column(Text, nullable=True)
    summary = Column(Text)
    materials_shared = Column(Text, nullable=True)
    samples_distributed = Column(Text, nullable=True)
    sentiment = Column(String, nullable=True)
    outcome = Column(Text, nullable=True)
    follow_up_action = Column(Text, nullable=True)

    follow_up_date = Column(DateTime, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )