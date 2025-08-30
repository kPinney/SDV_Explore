import itertools
import os
from sdmetrics.visualization import get_column_pair_plot #, get_cardinality_plot


def plot_column_pair(real_data, synthetic_data, column_names, save_path=None):
    """
    Generates and optionally saves a plot for a pair of columns.
    """
    fig = get_column_pair_plot(
        real_data=real_data,
        synthetic_data=synthetic_data,
        column_names=column_names
    )

    if save_path:
        fig.savefig(save_path)
        print(f"Column pair plot saved to {save_path}")

    fig.show()


def plot_all_column_pairs(real_data, synthetic_data, save_dir=None):
    """
    Generates and optionally saves plots for all column pairs.
    """
    if save_dir and not os.path.exists(save_dir):
        os.makedirs(save_dir)

    column_names = real_data.columns
    for pair in itertools.combinations(column_names, 2):
        save_path = f"{save_dir}/{pair[0]}_vs_{pair[1]}.png" if save_dir else None
        print(f"Plotting {pair[0]} vs {pair[1]}...")
        plot_column_pair(real_data, synthetic_data, list(pair), save_path)

''' #to be implemented
def plot_cardinality(real_data, synthetic_data, metadata, save_path=None):
    """
    Generates and optionally saves a plot for table relationship cardinality.
    """
    fig = get_cardinality_plot(
        real_data=real_data,
        synthetic_data=synthetic_data,
        metadata=metadata
    )

    if save_path:
        fig.savefig(save_path)
        print(f"Cardinality plot saved to {save_path}")

    fig.show()
'''
