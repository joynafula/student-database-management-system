# Student Performance Analysis

**Project type:** Reconstructed learning / portfolio project  
**Level:** Beginner  
**Author:** Wanyonyi Joy Nafula

## Project overview

This project demonstrates a basic workflow for exploring student performance data with Python and Pandas. It calculates average scores, groups records using a simple threshold, prints summary statistics and creates charts.

The included dataset is **synthetic**: all records are fictional and were created for learning. It does not represent actual learners or a real school.

## Questions explored

- What is the average score in each subject?
- How many records fall into each performance group?
- What is the relationship (correlation) between study hours and average score in this sample?

## Tools

- Python
- Pandas
- Matplotlib

## Files

- `student_performance.csv` — fictional sample dataset.
- `student_performance_analysis.py` — analysis script.
- `outputs/` — charts and analysed data generated when the script runs.

## Setup and run

1. Install Python 3.
2. Open a terminal in this folder.
3. Install dependencies:

   ```bash
   pip install pandas matplotlib
   ```

4. Run:

   ```bash
   python student_performance_analysis.py
   ```

The script creates an `outputs` folder containing two charts and a CSV with calculated columns.

## Method

1. Load the CSV into a Pandas DataFrame.
2. Inspect the first records and check for missing values.
3. Calculate each learner's average across Mathematics, English and Science.
4. Categorise records as `Pass` when the average is at least 50, otherwise `Needs support`.
5. Print descriptive statistics and the correlation between study hours and average score.
6. Create and save visualisations.

## Important interpretation note

A correlation in this small fictional dataset does not prove that additional study hours cause higher marks. The dataset is small and artificial, so its results should not be generalised to real students.

## Possible improvements

- Use a larger, real, anonymised dataset with appropriate permission.
- Add validation for missing or invalid scores.
- Compare results across classes or terms.
- Explore attendance and performance together.
- Add more visualisations and a written analysis of findings.

## Learning objectives

This project is intended to practise loading CSV data, selecting columns, calculating values, using Pandas summary functions, interpreting correlation and creating basic charts.
