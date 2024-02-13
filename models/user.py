#!/usr/bin/python3
"""
User Class from Models Module
"""

import os
from models.base_model import BaseModel


class User(BaseModel):
    """
        User class handles all application users
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
