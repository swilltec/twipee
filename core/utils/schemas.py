#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 03:59:48 2021

@author: devparrot
"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl

# constr(min_length=6, max_length=100)
class Link(BaseModel):
    url: Optional[HttpUrl]
    name: Optional[str]


class Tweet(BaseModel):
    timestamp: Optional[datetime]
    tip: Optional[str]
    link: Optional[]
    author: Optional[str]
