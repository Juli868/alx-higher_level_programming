#!/usr/bin/python3
"""sql alchmeny in cahrge."""
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
mine = MetaData()
Base = declarative_base(metadata=mine)


class State(Base):
    """Define a class related to table states."""

    __tablename__ = 'states'
    id = Column('id', Integer, primary_key=True, unique=True, nullable=False)
    name = Column('name', String(128), nullable=False)
