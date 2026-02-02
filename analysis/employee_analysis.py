import pandas as pd

# Step 1: Load data
df = pd.read_csv("data/employees.csv")

# Step 2: Clean data
df['Salary'] = df['Salary'].fillna(0)
df = df.drop_duplicates()

# Step 3: Analysis
avg_salary = df.groupby('Department')['Salary'].mean()
status_count = df['Status'].value_counts()

# Step 4: Save insights
with open("output/insights.txt", "w") as f:
    f.write("Average Salary by Department:\n")
    f.write(str(avg_salary))
    f.write("\n\nEmployee Status Count:\n")
    f.write(str(status_count))

print("Analysis completed successfully.")
