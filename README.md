# Student Result Analysis

A Python project that analyzes student performance data from CSV files. It reports dataset and exam-score summaries, fills missing values, removes duplicate rows, saves a cleaned dataset, and displays charts for exam scores and selected factors.

## Requirements

- Python 3
- pandas
- matplotlib

## Run the project

Open PowerShell in this project folder and install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

Run the analysis:

```powershell
python Student_Result_Analysis_Using_Your_CSV.py
```

The script reads `StudentPerformanceFactors.csv` from the project folder and writes `StudentPerformanceFactors_Cleaned.csv` there. It also opens charts using Matplotlib.

## Data

The CSV files are included in this repository. The `Student_Name` column has been removed from the datasets, and the script also omits it if it is present in the input CSV.
