#!/usr/bin/python3
"""
Review Class from Models Module
"""
import os
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class handles all application reviews"""
    place_id = ''
    user_id = ''
    text = ''
