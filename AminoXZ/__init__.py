"""
Author: Xsarz

Enjoy using!
"""


from os import system as s
from .client import Client
from .lib.util import generator, helpers, exceptions, headers
from colored import fore
from json import loads
from requests import get

def init():
	s('cls || clear')

init()
