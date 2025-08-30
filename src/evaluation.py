from sdmetrics.reports.single_table import QualityReport
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

def get_quality_report(real_data, synthetic_data, metadata):
    """
    Generates a quality report for single table data.
    """
    report = QualityReport()
    report.generate(real_data, synthetic_data, metadata)
    return report

def plot_column_distributions(real_data, synthetic_data, column_name, save_path=None):
    """
    Plots and optionally saves the distribution of a column for real and synthetic data.
    """
    plt.figure(figsize=(12, 6))
    sns.histplot(real_data[column_name], color='blue', label='Real Data', kde=True, stat='density', alpha=0.5)
    sns.histplot(synthetic_data[column_name], color='red', label='Synthetic Data', kde=True, stat='density', alpha=0.5)
    plt.title(f'{column_name.capitalize()} Distribution: Real vs. Synthetic')
    plt.legend()

    if save_path:
        plt.savefig(save_path)
        print(f"Plot saved to {save_path}")

    plt.show()

def plot_correlation_matrices(real_data, synthetic_data, save_path=None):
    """
    Plots and optionally saves the correlation matrices of real and synthetic data.
    """
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    real_corr = real_data.corr()
    sns.heatmap(real_corr, ax=axes[0], cmap='viridis')
    axes[0].set_title('Real Data Correlation Matrix')

    synthetic_corr = synthetic_data.corr()
    sns.heatmap(synthetic_corr, ax=axes[1], cmap='viridis')
    axes[1].set_title('Synthetic Data Correlation Matrix')

    if save_path:
        plt.savefig(save_path)
        print(f"Correlation matrices plot saved to {save_path}")

    plt.show()

def plot_pca(real_data, synthetic_data, save_path=None):
    """
    Plots and optionally saves the PCA of real and synthetic data.
    """
    pca = PCA(n_components=2)

    real_pca = pca.fit_transform(real_data)
    synthetic_pca = pca.transform(synthetic_data)

    plt.figure(figsize=(12, 6))
    plt.scatter(real_pca[:, 0], real_pca[:, 1], c='blue', label='Real Data', alpha=0.5)
    plt.scatter(synthetic_pca[:, 0], synthetic_pca[:, 1], c='red', label='Synthetic Data', alpha=0.5)
    plt.title('PCA of Real vs. Synthetic Data')
    plt.legend()

    if save_path:
        plt.savefig(save_path)
        print(f"PCA plot saved to {save_path}")

    plt.show()

def plot_all_column_distributions(real_data, synthetic_data, save_dir=None):
    """
    Plots and optionally saves the distribution of all columns for real and synthetic data.
    """
    for column in real_data.columns:
        save_path = f"{save_dir}/{column}_distribution.png" if save_dir else None
        plot_column_distributions(real_data, synthetic_data, column, save_path)
