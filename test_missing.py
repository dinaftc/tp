import csv
from src.model.row_2_list import row_to_list  
import pytest

dataset = []
with open('data/house_price.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        dataset.append(row)

# Test if the function correctly handles rows with missing values
# Parametrize the test function to iterate through each row in the dataset
@pytest.mark.parametrize("input_row", dataset)
def test_row_to_list_with_missing_values(input_row):
 # Convert the input row to a string without leading/trailing whitespace
    input_string = ' '.join(input_row).strip()

    # Split the input string using multiple spaces as a separator
    elements = input_string.split('  ')  # Note the double space

    # Check for missing values (empty strings) in the elements
    missing_values = [element for element in elements if not element.strip()]

    # Assert that there are no missing values in the input_string
    assert not missing_values, f"Missing values found: {missing_values}"