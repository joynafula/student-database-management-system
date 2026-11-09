"""
Student Performance Analysis
A beginner-friendly portfolio project using a small synthetic dataset.

Install:
    pip install pandas matplotlib

Run:
    python student_performance_analysis.py

Note:
    The CSV contains fictional sample records. It is not real school data.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = Path(__file__).with_name("student_performance.csv")
OUTPUT_DIR = Path(__file__).with_name("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def load_data(file_path):
    """Load the student dataset and return it as a DataFrame."""
    data = pd.read_csv(file_path)
    return data


def prepare_data(data):
    """Check missing values and create useful calculated columns."""
    print("\nFirst five records:")
    print(data.head())

    print("\nDataset information:")
    print(data.info())

    print("\nMissing values per column:")
    print(data.isnull().sum())

    score_columns = ["math_score", "english_score", "science_score"]
    data["average_score"] = data[score_columns].mean(axis=1)
    data["performance"] = data["average_score"].apply(
        lambda score: "Pass" if score >= 50 else "Needs support"
    )
    return data


def summarize_data(data):
    """Print summary statistics and simple comparisons."""
    score_columns = ["math_score", "english_score", "science_score"]

    print("\nSummary statistics:")
    print(data[score_columns + ["average_score"]].describe().round(2))

    print("\nAverage score by subject:")
    print(data[score_columns].mean().round(2))

    print("\nNumber of students in each performance group:")
    print(data["performance"].value_counts())

    print("\nCorrelation between study hours and average score:")
    correlation = data["study_hours"].corr(data["average_score"])
    print(round(correlation, 2))


def create_visualizations(data):
    """Save two charts that help explore the dataset."""
    subject_averages = data[
        ["math_score", "english_score", "science_score"]
    ].mean()

    subject_averages.plot(kind="bar", title="Average Score by Subject")
    plt.xlabel("Subject")
    plt.ylabel("Average score")
    plt.ylim(0, 100)
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "average_scores_by_subject.png")
    plt.close()

    plt.scatter(data["study_hours"], data["average_score"])
    plt.title("Study Hours and Average Score")
    plt.xlabel("Study hours")
    plt.ylabel("Average score")
    plt.tight_layout()
    plt.savefig(OUTPUT_DIR / "study_hours_vs_average_score.png")
    plt.close()

    print(f"\nCharts saved in: {OUTPUT_DIR}")


def main():
    data = load_data(DATA_FILE)
    data = prepare_data(data)
    summarize_data(data)
    create_visualizations(data)

    data.to_csv(OUTPUT_DIR / "analysed_student_results.csv", index=False)
    print("Analysis complete.")


if __name__ == "__main__":
    main()
