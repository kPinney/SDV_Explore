import pandas as pd
from sdv.metadata import Metadata
from sdv.single_table import GaussianCopulaSynthesizer, CTGANSynthesizer, TVAESynthesizer
from sdv.multi_table import HMASynthesizer
from src.constraints import get_constraints
from sdv.cag import Inequality

CONSTRAINT_MAP = {
    'Inequality': Inequality,
}

def generate_single_table_data(real_data, num_rows=100, synthesizer_type='gaussian_copula'):
    """
    Generates single table synthetic data using a specified synthesizer.
    """
    metadata = Metadata()
    real_data['start_date'] = pd.to_datetime(pd.date_range(start='2023-01-01', periods=len(real_data), freq='D'))
    real_data['end_date'] = pd.to_datetime(pd.date_range(start='2023-01-02', periods=len(real_data), freq='D'))

    metadata = Metadata()
    metadata = metadata.detect_from_dataframe(data=real_data, table_name='users')

    constraints_to_add = get_constraints()
    constraints_list = []
    for constraint_info in constraints_to_add:
        constraint_class = CONSTRAINT_MAP.get(constraint_info['constraint_class'])
        if constraint_class:
            constraints_list.append(
                constraint_class(**constraint_info['constraint_parameters'])
            )

    if synthesizer_type == 'gaussian_copula':
        synthesizer = GaussianCopulaSynthesizer(metadata)
    elif synthesizer_type == 'ctgan':
        synthesizer = CTGANSynthesizer(metadata)
    elif synthesizer_type == 'tvae':
        synthesizer = TVAESynthesizer(metadata)
    else:
        raise ValueError(f"Unknown synthesizer type: {synthesizer_type}")

    if constraints_list:
        synthesizer.add_constraints(constraints=constraints_list)


    synthesizer.fit(data=real_data)

    synthetic_data = synthesizer.sample(num_rows=num_rows)
    return synthetic_data, metadata

def generate_multi_table_data(real_data_dict, scale=1.0):
    """
    Generates multi-table synthetic data using HMASynthesizer.
    """
    metadata = Metadata()
    metadata.detect_from_dataframes(data=real_data_dict)

    # This is a placeholder for relationship definitions.
    # In a real scenario, you would define relationships like this:
    # metadata.add_relationship(
    #     parent_table_name='customers',
    #     child_table_name='orders',
    #     parent_primary_key='customer_id',
    #     child_foreign_key='customer_id'
    # )

    synthesizer = HMASynthesizer(metadata)
    synthesizer.fit(data=real_data_dict)

    synthetic_data = synthesizer.sample(scale=scale)
    return synthetic_data
