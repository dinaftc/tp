import pytest
from src.model import module
#from src.module.module import serve_beer
def test_serve_beer_legal():
  adult = 25
  assert module.serve_beer(adult) == "Have beer"
 
def test_serve_beer_illegal():
  child = 10
  assert module.serve_beer(child) == "No beer"