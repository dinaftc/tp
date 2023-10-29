import pytest
from src.model import row_to_list

def test_for_clean_row():
  assert row_to_list.row_to_list("2,081\t314,942\n") == \ ["2,081","314,942"]

def test_for_missing_area():
  assert row_to_list.row_to_list("\t293,410\n") is None
 
def test_for_missing_tab():
  assert row_to_list.row_to_list("1,463438,756\n") is None
 
