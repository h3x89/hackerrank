# A tiny piece of code that represents an HR Employee Data Management system.
# This code will manage a simple string that contains employee data.

employee_data = "Alice,Developer,30|Bob,Manager,45|Charlie,Designer,25"
# Splitting the employee data by '|' to separate each employee's info
employee_list = employee_data.split('|')

# TODO: For each employee, create a formatted string with stripped details and role eligibility for a junior position

for employee in employee_list:
    # TODO: Parse the employee data and add eligibility note if applicable
    name, role, age = employee.split(',')
    eligibility = " - Eligible for junior position" if role == "Developer" or role == "Designer" else ""
    print(f"Name: {name} - Role: {role} - Age: {age}{eligibility}")
    # Example: Name: Alice - Role: Developer - Age: 30 - Eligible for junior position