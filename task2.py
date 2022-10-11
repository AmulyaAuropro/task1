employee={
  "name": "Tim",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer"
}

employee['job'] = "Software Engineer"
for key in employee.keys():
    print(key, employee[key])
