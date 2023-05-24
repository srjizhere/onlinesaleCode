import pandas as pd

# Read the department.csv file
department_df = pd.read_csv('departments.csv')

# Read the employees.csv file
employees_df = pd.read_csv('employees.csv')

# Read the salaries.csv file
salaries_df = pd.read_csv('salaries.csv')

# Merge the dataframes to get the department names and average monthly salaries
merged_df = employees_df.merge(department_df, left_on='DEPT ID', right_on='ID')

merged_df = merged_df.merge(salaries_df, left_on='ID_x', right_on='EMP_ID')

# Calculate the average monthly salary for each department
average_salary_per_dept = merged_df.groupby('NAME_y')['AMT (USD)'].mean()

# Convert department names to categorical data type to preserve the order
department_df['NAME'] = pd.Categorical(department_df['NAME'], categories=average_salary_per_dept.index, ordered=True)

# Merge the average salaries with the department names while preserving the order
result_df = pd.merge(department_df, average_salary_per_dept, left_on='NAME', right_index=True)

# Get the top three departments with the highest average salary
columns_to_hide = ['ID']
top_three_departments = result_df.head(3).drop(columns_to_hide,axis=1)

# Display the top three departments with average monthly salary
print(top_three_departments)
