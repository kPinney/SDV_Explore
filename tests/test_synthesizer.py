import pandas as pd
import pytest
from src.synthesizer import generate_single_table_data

@pytest.fixture
def real_data():
    """
    Provides a sample DataFrame for testing.
    """
    data = {
        'id': range(10),
        'age': [20 + i for i in range(10)],
        'city': ['A', 'B'] * 5
    }
    return pd.DataFrame(data)

@pytest.mark.parametrize('synthesizer_type', ['gaussian_copula', 'ctgan', 'tvae'])
def test_generate_single_table_data(real_data, synthesizer_type):
    """
    Tests the generation of single table synthetic data with different synthesizers.
    """
    num_rows = 50
    synthetic_data = generate_single_table_data(real_data, num_rows=num_rows, synthesizer_type=synthesizer_type)

    # Assertions
    assert isinstance(synthetic_data, pd.DataFrame)
    assert len(synthetic_data) == num_rows
    assert list(synthetic_data.columns) == list(real_data.columns)

def test_generate_single_table_data_unknown_synthesizer(real_data):
    """
    Tests that a ValueError is raised for an unknown synthesizer type.
    """
    with pytest.raises(ValueError):
        generate_single_table_data(real_data, synthesizer_type='unknown')
