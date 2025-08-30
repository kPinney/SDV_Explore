import pandas as pd
import pytest
from unittest.mock import patch
from src.evaluation import (
    get_quality_report,
    plot_column_distributions,
    plot_correlation_matrices,
    plot_pca,
    plot_all_column_distributions
)
from sdv.metadata import Metadata

@pytest.fixture
def test_data():
    """
    Provides sample real and synthetic data for testing.
    """
    data = {
        'col1': [1, 2, 3, 4, 5],
        'col2': [5, 4, 3, 2, 1]
    }
    real_data = pd.DataFrame(data)
    synthetic_data = pd.DataFrame(data)
    return real_data, synthetic_data

@patch('sdmetrics.reports.single_table.QualityReport.generate')
def test_get_quality_report(mock_generate, test_data):
    """
    Tests the quality report generation.
    """
    real_data, synthetic_data = test_data
    metadata = Metadata()
    metadata.detect_from_dataframe(data=real_data)
    get_quality_report(real_data, synthetic_data, metadata.to_dict())
    mock_generate.assert_called_once()

    # Test with table metadata directly
    table_metadata = metadata.to_dict()['tables']['real_data']
    get_quality_report(real_data, synthetic_data, table_metadata)
    assert mock_generate.call_count == 2

@patch('matplotlib.pyplot.show')
def test_plot_column_distributions(mock_show, test_data):
    """
    Tests the column distribution plotting.
    """
    real_data, synthetic_data = test_data
    plot_column_distributions(real_data, synthetic_data, 'col1')
    mock_show.assert_called_once()

@patch('matplotlib.pyplot.show')
def test_plot_correlation_matrices(mock_show, test_data):
    """
    Tests the correlation matrix plotting.
    """
    real_data, synthetic_data = test_data
    plot_correlation_matrices(real_data, synthetic_data)
    mock_show.assert_called_once()

@patch('matplotlib.pyplot.show')
def test_plot_pca(mock_show, test_data):
    """
    Tests the PCA plotting.
    """
    real_data, synthetic_data = test_data
    plot_pca(real_data, synthetic_data)
    mock_show.assert_called_once()

@patch('src.evaluation.plot_column_distributions')
def test_plot_all_column_distributions(mock_plot, test_data):
    """
    Tests the plotting of all column distributions.
    """
    real_data, synthetic_data = test_data
    plot_all_column_distributions(real_data, synthetic_data)
    assert mock_plot.call_count == len(real_data.columns)
