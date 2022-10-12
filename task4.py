from HelperModule import employees

e = employees()
employees = e.read_employees()
youngest_employee = e.get_youngest_employee(employees)

print("Youngest Employee Name:"+youngest_employee['name'])
print("Youngest Employee Age:"+(str(youngest_employee['age'])))