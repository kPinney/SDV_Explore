import pandas as pd
import pytest
from unittest.mock import patch, MagicMock
from src.selection import select_best_synthesizer

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

@patch('src.selection.generate_single_table_data')
@patch('src.selection.get_quality_report')
def test_select_best_synthesizer(mock_get_quality_report, mock_generate_single_table_data, real_data):
    """
    Tests the synthesizer selection process.
    """
    # Mock the scores for each synthesizer
    mock_scores = {'gaussian_copula': 0.8, 'ctgan': 0.9, 'tvae': 0.85}

    def side_effect(real_data, synthetic_data, metadata):
        report = MagicMock()
        # Extract synthesizer type from synthetic_data mock name
        synthesizer_type = synthetic_data.name
        report.get_score.return_value = mock_scores[synthesizer_type]
        return report

    mock_get_quality_report.side_effect = side_effect

    def generate_side_effect(real_data, synthesizer_type):
        mock_df = pd.DataFrame()
        mock_df.name = synthesizer_type # Store synthesizer type for score lookup
        return mock_df

    mock_generate_single_table_data.side_effect = generate_side_effect

    best_synthesizer, _, _, all_scores = select_best_synthesizer(real_data)

    assert best_synthesizer == 'ctgan'
    assert all_scores == mock_scores
