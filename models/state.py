#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sat November 26 13:56:43 2022
@authors: Salihu Abduljawwad
          Gideon Wangui
"""

from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel
    Attribute:
        name (str): Public class attribute for State's name
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """init method for State class
        Attributes:
            args (list): The list with arguments
            kwargs (dict): A dictionary with arguments
        """
        super().__init__(*args, **kwargs)
