employees = [{
  "name": "Tina",
  "age": 30,
  "birthday": "1990-03-10",
  "job": "DevOps Engineer",
  "address": {
    "city": "New York",
    "country": "USA"
  }
},
{
  "name": "Tim",
  "age": 35,
  "birthday": "1985-02-21",
  "job": "Developer",
  "address": {
    "city": "Sydney",
    "country": "Australia"
  }
}]

# iterate all employees
for employee in employees:
    print("Name: ", employee['name'])
    print("Job: ", employee['job'])
    print("City: ", employee['address']['city'])       

# access second employee country
print(employees[1]['address']['country'])    

output:
Name:  Tina
Job:  DevOps Engineer
City:  New York
Name:  Tim
Job:  Developer
City:  Sydney
Australia