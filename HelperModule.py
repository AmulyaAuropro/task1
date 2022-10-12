class employees:
    
    def _init_():
        pass

    def read_employees(self):
        employees =  []
        no_of_employees = int(input("Enter the number of employees: "))
        for i in range(no_of_employees):
            employee ={}
            employee["name"]=  input(f'Enter the Employee({i}) name :')
            employee["age"]= int(input(f'Enter the Employee({i}) Age :'))
            employee["birthday"]=  input(f'Enter the Employee({i}) birthday :')
            employee["job"]=  input(f'Enter the Employee({i}) job :')
            employees.append(employee)
        
        return employees

    def get_youngest_employee(self,employees):
        ages = {}
        for idx,e in enumerate(employees):
            ages[idx] = e['age']
        return employees[min(ages, key=ages.get)]