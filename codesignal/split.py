# Employee Information Management System

# A list of employee data
employee_data = "Name: John Doe, Age: 30, Role: Engineer"

employee_info = employee_data.split(',')

# Use strip to clean data and join to create a string with newlines
cleaned_data = "\n".join(info.strip() for info in employee_info)

print(cleaned_data)