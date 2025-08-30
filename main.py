import pandas as pd
from src.data_loader import load_single_table_data
from src.selection import select_best_synthesizer
from src.evaluation import plot_all_column_distributions

def main():
    """
    Main script to run the SDV workflow.
    """
    # Opt-in to future behavior for pandas
    pd.set_option('future.no_silent_downcasting', True)
    
    # Load data
    real_data = load_single_table_data('data/sample_data.csv')

    # Select the best synthesizer
    best_synthesizer, best_synthetic_data, best_report, all_scores = select_best_synthesizer(real_data)

    print("\n--- Synthesizer Evaluation Results ---")
    for synthesizer, score in all_scores.items():
        print(f"- {synthesizer}: {score:.4f}")

    print(f"\nBest synthesizer: {best_synthesizer}")
    print(f"Quality score: {best_report.get_score():.4f}")

    # Plot distributions
    print("\nGenerating distribution plots for the best model...")
    plot_all_column_distributions(real_data, best_synthetic_data, save_dir='reports')
    print("Plots saved to the 'reports' directory.")

if __name__ == '__main__':
    main()
