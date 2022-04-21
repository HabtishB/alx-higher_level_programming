#!/usr/bin/python3
"""
This class contains the class definition of a state and an
instance Base = declarative_base():
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Representation of a state for a mySQL database

    __tabelname__(str): The name of the MySQL table to store States
    id (sqlalchemy.Integer): The state's id
    name (sqlalchemy.String): The state's name
    """
    __table__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
