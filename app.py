import sys

def calculate_gross_salary(basic):
    hra = basic * 0.20
    da = basic * 0.10
    return basic + hra + da

def get_employee_details():
    if len(sys.argv) != 4:
        print("Usage: python app.py <employee_name> <employee_id> <basic_salary>")
        sys.exit(1)

    name = sys.argv[1]
    emp_id = sys.argv[2]

    try:
        basic = float(sys.argv[3])
    except ValueError:
        print("Error: Basic salary must be a number.")
        sys.exit(1)

    gross_salary = calculate_gross_salary(basic)

    return {
        "name": name,
        "emp_id": emp_id,
        "basic": basic,
        "gross_salary": gross_salary
    }

def display_employee(employee):
    print("\nEmployee Salary Details")
    print("-----------------------")
    print("Name         :", employee["name"])
    print("Employee ID  :", employee["emp_id"])
    print("Basic Salary :", employee["basic"])
    print("Gross Salary :", employee["gross_salary"])

if __name__ == "__main__":
    employee = get_employee_details()
    display_employee(employee)
