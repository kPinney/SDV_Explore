import os
import pandas as pd
from src.data_loader import load_single_table_data

def test_load_single_table_data_from_csv():
    """
    Tests loading data from a CSV file.
    """
    # Create a dummy CSV for testing
    data = {'col1': [1, 2], 'col2': ['A', 'B']}
    df = pd.DataFrame(data)
    test_csv_path = 'test_data.csv'
    df.to_csv(test_csv_path, index=False)

    # Test loading the CSV
    loaded_df = load_single_table_data(test_csv_path)
    assert isinstance(loaded_df, pd.DataFrame)
    assert not loaded_df.empty
    assert loaded_df.shape == (2, 2)

    # Clean up the dummy CSV
    os.remove(test_csv_path)

def test_load_single_table_data_dummy_data():
    """
    Tests the generation of dummy data when the CSV is not found.
    """
    # Test dummy data generation
    dummy_df = load_single_table_data('non_existent_file.csv')
    assert isinstance(dummy_df, pd.DataFrame)
    assert not dummy_df.empty
    assert 'salary' in dummy_df.columns
