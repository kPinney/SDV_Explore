"""
This module provides functionality to automatically select the best synthesizer.
"""
import time
from src.synthesizer import generate_single_table_data
from src.evaluation import get_quality_report
from sdv.metadata import Metadata

def select_best_synthesizer(real_data, synthesizers=None):
    """
    Selects the best synthesizer for a given dataset based on the quality score.
    """
    if synthesizers is None:
        synthesizers = ['gaussian_copula']
    best_synthesizer = None
    best_synthetic_data = None
    best_report = None
    best_score = -1
    all_scores = {}

    metadata = Metadata()
    metadata.detect_from_dataframe(data=real_data)

    for synthesizer_type in synthesizers:
        print(f"Evaluating synthesizer: {synthesizer_type}")
        start_time = time.time()
        synthetic_data, metadata = generate_single_table_data(real_data, synthesizer_type=synthesizer_type)
        table_name = list(metadata.to_dict()['tables'].keys())[0]
        table_metadata = metadata.to_dict()['tables'][table_name]
        report = get_quality_report(real_data, synthetic_data, table_metadata)
        score = report.get_score()
        all_scores[synthesizer_type] = score
        end_time = time.time()
        print(f"Time taken for {synthesizer_type}: {end_time - start_time:.2f} seconds")

        if score is not None and score > best_score:
            best_score = score
            best_synthesizer = synthesizer_type
            best_synthetic_data = synthetic_data
            best_report = report

    return best_synthesizer, best_synthetic_data, best_report, all_scores
