"""
Kedro pipeline implementation.
"""

from src.data_cleaning import clean_data
from src.data_analysis import analyze_data
from src.merge import merge_data
from src.db_operations import upload_to_db

def run_pipeline():
    """
    Main function to execute the data pipeline.
    """
    print("Starting data pipeline...")

    # Step 1: Clean the data
    cleaned_data = clean_data()

    # Step 2: Merge datasets
    merged_data = merge_data(cleaned_data)

    # Step 3: Analyze the data
    analysis_results = analyze_data(merged_data)

    # Step 4: Upload results to the database
    upload_to_db(analysis_results)

    print("Pipeline execution completed.")

if __name__ == "__main__":
    run_pipeline()
