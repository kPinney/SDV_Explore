"""
This module defines constraints for the SDV synthesizer.
"""

def get_constraints():
    """
    Returns a list of constraints to be applied to the metadata.
    """
    constraints = [
        {
            'constraint_class': 'Inequality',
            'constraint_parameters': {
                'low_column_name': 'start_date',
                'high_column_name': 'end_date',
                'table_name': 'users'
            }
        }
    ]
    return constraints
