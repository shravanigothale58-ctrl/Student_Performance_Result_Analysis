
# MINI PROJECT 1: STUDENT RESULT ANALYSIS
# Dataset: StudentPerformanceFactors.csv
# Libraries: Pandas and Matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# 1. Import the CSV dataset
# --------------------------------------------------
# Keep this Python file and the CSV file in the same folder.
df = pd.read_csv("StudentPerformanceFactors.csv")
df = df.drop(columns=["Student_Name"], errors="ignore")

# Display the first five records to understand the data
print("\n========== FIRST FIVE RECORDS ==========")
print(df.head())

# Display dataset size, column names, and data types
print("\n========== DATASET INFORMATION ==========")
print("Number of rows and columns:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types and non-missing values:")
df.info()

# --------------------------------------------------
# 2. Check and clean missing values
# --------------------------------------------------
# Count missing values in every column
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Create a copy so the original imported data stays unchanged
df_clean = df.copy()

# Fill missing numerical values with that column's median
numeric_columns = df_clean.select_dtypes(include="number").columns
for column in numeric_columns:
    df_clean[column] = df_clean[column].fillna(df_clean[column].median())

# Fill missing text/category values with the most frequent value
categorical_columns = df_clean.select_dtypes(include="object").columns
for column in categorical_columns:
    if df_clean[column].isnull().any():
        df_clean[column] = df_clean[column].fillna(df_clean[column].mode()[0])

# Remove exact duplicate rows, if any
df_clean = df_clean.drop_duplicates()

print("\nRows after cleaning:", len(df_clean))
print("Remaining missing values:", int(df_clean.isnull().sum().sum()))

# --------------------------------------------------
# 3. Explore exam scores
# --------------------------------------------------
# Exam_Score is the outcome/target column in this dataset
print("\n========== EXAM SCORE SUMMARY ==========")
print(df_clean["Exam_Score"].describe().round(2))

# Calculate the average, highest, and lowest exam scores
average_score = df_clean["Exam_Score"].mean()
highest_score = df_clean["Exam_Score"].max()
lowest_score = df_clean["Exam_Score"].min()

print("Average exam score:", round(average_score, 2))
print("Highest exam score:", highest_score)
print("Lowest exam score:", lowest_score)

# This dataset does not contain student names or IDs.
# Use the row number as a record reference when showing the highest score.
topper_index = df_clean["Exam_Score"].idxmax()
topper = df_clean.loc[topper_index]

print("\n========== HIGHEST-SCORING RECORD ==========")
print("Dataset record number:", topper_index + 1)
print("Exam score:", topper["Exam_Score"])
print("Hours studied:", topper["Hours_Studied"])
print("Attendance:", topper["Attendance"])
print("Previous scores:", topper["Previous_Scores"])

# --------------------------------------------------
# 4. Compare average exam scores by selected factors
# --------------------------------------------------
# Group the data by a category and calculate the mean exam score
category_columns = [
    "Parental_Involvement",
    "Access_to_Resources",
    "Motivation_Level",
    "Internet_Access",
    "School_Type",
    "Peer_Influence",
    "Gender"
]

print("\n========== AVERAGE EXAM SCORE BY FACTOR ==========")
for column in category_columns:
    print(f"\nAverage Exam_Score by {column}:")
    print(df_clean.groupby(column)["Exam_Score"].mean().round(2).sort_values(ascending=False))

# --------------------------------------------------
# 5. Filter records with exam scores of 80 or above
# --------------------------------------------------
# This is an example threshold; change it for your analysis
high_scores = df_clean[df_clean["Exam_Score"] >= 80]

print("\n========== EXAM SCORES OF 80 OR ABOVE ==========")
print("Number of records:", len(high_scores))
print(high_scores[["Exam_Score", "Hours_Studied", "Attendance", "Previous_Scores"]].head(10))

# --------------------------------------------------
# 6. Save the cleaned dataset
# --------------------------------------------------
df_clean.to_csv("StudentPerformanceFactors_Cleaned.csv", index=False)
print("\nCleaned dataset saved as StudentPerformanceFactors_Cleaned.csv")

# --------------------------------------------------
# 7. Visualisation 1: Distribution of exam scores
# --------------------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df_clean["Exam_Score"], bins=15, edgecolor="black")
plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 8. Visualisation 2: Study hours and exam score
# --------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df_clean["Hours_Studied"], df_clean["Exam_Score"], alpha=0.5)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Hours Studied")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 9. Visualisation 3: Attendance and exam score
# --------------------------------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df_clean["Attendance"], df_clean["Exam_Score"], alpha=0.5)
plt.title("Attendance vs Exam Score")
plt.xlabel("Attendance")
plt.ylabel("Exam Score")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 10. Visualisation 4: Average exam score by motivation
# --------------------------------------------------
motivation_average = df_clean.groupby("Motivation_Level")["Exam_Score"].mean().sort_values(ascending=False)

plt.figure(figsize=(7, 5))
plt.bar(motivation_average.index, motivation_average.values)
plt.title("Average Exam Score by Motivation Level")
plt.xlabel("Motivation Level")
plt.ylabel("Average Exam Score")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 11. Visualisation 5: Average exam score by school type
# --------------------------------------------------
school_average = df_clean.groupby("School_Type")["Exam_Score"].mean()

plt.figure(figsize=(6, 5))
plt.bar(school_average.index, school_average.values)
plt.title("Average Exam Score by School Type")
plt.xlabel("School Type")
plt.ylabel("Average Exam Score")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 12. Correlation between numerical columns
# --------------------------------------------------
# Correlation measures the strength and direction of a linear relationship.
numeric_df = df_clean.select_dtypes(include="number")
correlation = numeric_df.corr()

print("\n========== CORRELATION WITH EXAM SCORE ==========")
print(correlation["Exam_Score"].sort_values(ascending=False).round(2))

# Display a simple correlation chart for Exam_Score
score_correlation = correlation["Exam_Score"].drop("Exam_Score").sort_values()

plt.figure(figsize=(8, 5))
plt.barh(score_correlation.index, score_correlation.values)
plt.title("Correlation of Numerical Factors with Exam Score")
plt.xlabel("Correlation Coefficient")
plt.ylabel("Numerical Factor")
plt.tight_layout()
plt.show()
