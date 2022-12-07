#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base
import models
from models.city import City


class State(BaseModel):
    """ State class """
    name = ""
