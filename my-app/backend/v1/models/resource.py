#!/usr/bin/env python3
"""
Defines the Resource model for mapping community resources.
"""

import models
from models.found_model import BaseModel
from sqlalchemy import Column, String, Text


class Resource(BaseModel):
    """
    Resource model class for mapping community resources.

    Attributes:
        id (int): Primary key for the resource.
        created_at (DateTime): Timestamp indicating when the resource was created.
        updated_at (DateTime): Timestamp indicating when the resource was last updated.
        name (str): Name of the resource.
        category (str): Category of the resource (e.g., hospital, school).
        description (str): Description of the resource.

    Methods:
        __repr__(): Returns a string representation of the Resource instance.
    """

    __tablename__ = 'resources'

    name = Column(String(255), nullable=False)
    category = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        """
        Returns a string representation of the Resource instance.

        Returns:
            str: String representation of the Resource instance.
        """
        return f"<Resource {self.id}: {self.name}>"