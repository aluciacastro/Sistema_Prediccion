from sqlalchemy import Column, Integer, String, Float
from app.infrastructure.database.connection import Base

class Child(Base):
    __tablename__ = "children"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age_months = Column(Integer)
    weight_kg = Column(Float)
    height_cm = Column(Float)

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    child_id = Column(Integer)
    nutritional_status = Column(String)
