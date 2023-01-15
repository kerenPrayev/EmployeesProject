from back_main import *

if __name__ == '__main__':
    print('welcome to the Employee Attendance Management System!')
    employee_id = input('enter id:')
    while True:
        employee_obje = check_id_input(employee_id)
        get_options_list_by_job(employee_obje)
        action_num = get_an_action_number()
        system_on = activating_action_num(employee_obje, action_num)
