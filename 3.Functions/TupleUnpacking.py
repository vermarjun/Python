# Employee data
work_hours = [('KrishnaJi',400),('Tuti',200),('Emojie',300)]

def employee_check(employee_data):
    current_max = 0
    current_employee_of_month = 'a'
    for employee,workhours in employee_data:
        if workhours > current_max:
            current_max = workhours
            current_employee_of_month = employee
        else:
            pass
    return current_employee_of_month,current_max

employee_of_month, workhours = employee_check(work_hours)
print(employee_of_month)
print(workhours)