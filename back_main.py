from classes import *


def check():
    """adding backround info, to check the system"""
    mos = Menagers('fi', 'li', '4', 8, 'j', '1955-09-5', 'm')
    mos.set_start_working_date(2021, 4, 11)
    geay = Menagers('li', 'fi', '8', 4, 't', '1955-09-4', 'm')
    geay.set_start_working_date(2020, 12, 5)
    nr = Hayeard('n', 'r', '44', 8, 't', '1995-09-5', 'h', mos)
    nr.set_start_working_date(2020, 12, 14)
    rn = Hayeard('r', 'n', '48', 8, 'r', '1975-07-5', 'h', mos)
    rn.set_start_working_date(2020, 12, 14)


check()


def activating(employee_obje):

    if employee_obje.job == 'h':
        for index, chose in enumerate(h_options):
            print(f'{index + 1}. {chose}.')
        action_num = get_an_action_number()

        if action_num == 1:
            print(employee_obje.update_start_hour())
            activating(employee_obje)

        elif action_num == 2:
            print('add description or just pres enter')
            description = input('description:')
            print(employee_obje.update_finish_hour(description))
            activating(employee_obje)

        elif action_num == 3:
            attendance_month = get_month_num()
            with open('attendance_log.csv', 'r') as attendance_file:
                all_attendance = csv.DictReader(attendance_file)
                attendancere_rquayeard_list = []
                for line in all_attendance:
                    if str(employee_obje.i_d) == line['employee_id'] and int(line['date'][5:7]) == attendance_month:
                        attendancere_rquayeard_list.append(line)
            Employes.make_attandance_xlsx_file(
                attendancere_rquayeard_list,
                f'Attendance of {employee_obje.full_name()} in the month: {attendance_month}')

        else:
            print(f'action number {action_num} not in your actions list')

    elif employee_obje.job == 'm':
        for index, chose in enumerate(m_options):
            print(f'{index + 1}. {chose}.')
        action_num = get_an_action_number()

        if action_num == 1:
            print(employee_obje.update_start_hour())
            activating(employee_obje)

        elif action_num == 2:
            print('add description or just pres enter')
            description = input('description:')
            print(employee_obje.update_finish_hour(description))
            activating(employee_obje)

        elif action_num == 3:
            with open('attendance_log.csv', 'r') as atandance_file:
                attendance_month = get_month_num()
                all_attendance = csv.DictReader(atandance_file)
                attendancere_rquayeard_list = []
                for line in all_attendance:
                    if str(employee_obje.i_d) == line['employee_id'] and int(line['date'][5:7]) == attendance_month:
                        attendancere_rquayeard_list.append(line)
            Employes.make_attandance_xlsx_file(
                attendancere_rquayeard_list,
                f'Attendance of {employee_obje.full_name()} in the month: {attendance_month}')

        elif action_num == 4:
            for index4, chose4 in enumerate(m_meanage_employees_options):
                print(f'{index4+1}. {chose4}.')
            action_num4 = get_an_action_number()
            if action_num4 == 1:
                print('in order to add employee, you must fill in all the requested data!')
                while True:
                    f_n = input("first name:")
                    if len(f_n) >= 2 and f_n.isalpha():
                        break
                    else:
                        print('name must have etlist tow letters, and contain leters only.')
                while True:
                    l_n = input('last name:')
                    if len(l_n) >= 2 and l_n.isalpha():
                        break
                    else:
                        print('name must have etlist tow letters, and containe letters only.')
                while True:
                    i_d = input('identity number:')
                    if len(i_d) == 9 and i_d.isdigit():
                        break
                    else:
                        print('identity number must have nine numbers and contain only numbers.')
                while True:
                    phone = input('phone number:')
                    if len(phone) == 10 and phone.isdigit():
                        break
                    else:
                        print('phone number must have ten numbers and contain only numbers.')
                while True:
                    adreass = input('adreass:')
                    if len(adreass) >= 2:
                        break
                    else:
                        print('adress must have etlist tow letters.')
                while True:
                    try:
                        b_d_y = int(input('birth date: year:'))
                        if len(str(b_d_y)) == 4:
                            break
                        else:
                            print('enter 4 numbers year.')
                    except ValueError:
                        print('!please enter a number.!')
                while True:
                    try:
                        b_d_m = int(input('birth date: month:'))
                        if 1 <= b_d_m <= 12:
                            break
                        else:
                            print('enter month year between 1 - 12.')
                    except ValueError:
                        print('!please enter a number.!')
                while True:
                    try:
                        b_d_d = int(input('birth date: day:'))
                        if 1 <= b_d_d <= 31:
                            break
                        else:
                            print('enter number of day between 1 - 31.')
                    except ValueError:
                        print('!please enter a number.!')
                b_d = datetime(b_d_y, b_d_m, b_d_d)
                while True:
                    job = input('job asiment:')
                    if job == 'h':
                        menager_id = input('menager id:')
                        menager_obje = get_obje(menager_id)
                        if menager_obje is not None:
                            Hayeard(f_n, l_n, i_d, phone, adreass, b_d, job, menager_obje)
                            break
                        else:
                            print(f'no menager with {menager_id} id number, pleas chack.')
                    elif job == 'm':
                        Menagers(f_n, l_n, i_d, phone, adreass, b_d, job)
                        break
                    else:
                        print('enter "h":hayeard, "m": menager')
                print(f'{get_obje(i_d).full_name()} was add to employees.')

            elif action_num4 == 2:
                while True:
                    employee_id_to_remove = input('enter id:')
                    try:
                        employee_obje_to_remove = get_obje(employee_id_to_remove)
                        employee_obje_to_remove.removed_employe_from_employees()
                        print(f'the employee {employee_obje_to_remove.full_name()} \
                        was removed from the company\'s employeed list')
                        break
                    except AttributeError:
                        print(f'no employee with {employee_id_to_remove} id number, pleas chack.')

            elif action_num4 == 3:
                while True:
                    employee_id_to_change_menager = input('enter id:')
                    try:
                        employee_obje_to_chang_menager = get_obje(employee_id_to_change_menager)
                        if employee_obje_to_chang_menager.job == 'h':
                            print(f'old menager:{employee_obje_to_chang_menager.manager.full_name()},\
                            id:{employee_obje_to_chang_menager.manager.i_d}')
                            old_menager_id = input('old menager id:')
                            old_menager_obje = get_obje(old_menager_id)
                            new_menager_id = input('new menager id:')
                            new_menager_obje = get_obje(new_menager_id)
                            employee_obje_to_chang_menager.change_menager(old_menager_obje, new_menager_obje)
                            print(f'{employee_obje_to_chang_menager.full_name()}\'s menager had change \
                            from: {old_menager_obje.full_name()}, to: {new_menager_obje.full_name()}')
                            break
                    except AttributeError:
                        print(f'no employee with {employee_id_to_change_menager} id number, pleas chack.')

            elif action_num4 == 4:
                print('my hayeard:')
                for obj in employee_obje.hayeard:
                    print(f'{obj.full_name()},id:{obj.i_d},phone:{obj.phone},adress:{obj.adreass},age:{obj.age()}')

            elif action_num4 == 5:
                for index45, chose45 in enumerate(m_employees_attandance_options):
                    print(f'{index45 + 1}. {chose45}.')
                action_num45 = get_an_action_number()

                if action_num45 == 1:
                    attendance_month = get_month_num()
                    with open('attendance_log.csv', 'r') as attendance_log:
                        attendance_list = csv.DictReader(attendance_log)
                        attendancere_rquayeard_list = []
                        for atend in attendance_list:
                            atend_date = atend['date']
                            atend_month = int(atend_date[5:7])
                            if atend_month == attendance_month \
                                    and get_obje(atend['employee_id']) in employee_obje.hayeard:
                                attendancere_rquayeard_list.append(atend)
                    Employes.make_attandance_xlsx_file(
                        attendancere_rquayeard_list,
                        f'Atendance of all {employee_obje.full_name()}\'s hayeards in the month: {attendance_month}')

                elif action_num45 == 2:
                    attendance_date = input('enter date number as yyyy-mm-dd:')
                    with open('attendance_log.csv', 'r') as attendance_log:
                        attendance_list = csv.DictReader(attendance_log)
                        attendancere_rquayeard_list = []
                        for atend in attendance_list:
                            if atend['date'] == attendance_date \
                                    and get_obje(atend['employee_id']) in employee_obje.hayeard:
                                attendancere_rquayeard_list.append(atend)
                    Employes.make_attandance_xlsx_file(
                        attendancere_rquayeard_list,
                        f'Atendance of all {employee_obje.full_name()}\'s hayeards in the date: {attendance_date}')

                elif action_num45 == 3:
                    while True:
                        attendance_employee = input('enter employee id:')
                        if get_obje(attendance_employee) in Employes.employees_objects:
                            with open('attendance_log.csv', 'r') as attendance_log:
                                attendance_list = csv.DictReader(attendance_log)
                                attendancere_rquayeard_list = []
                                for atend in attendance_list:
                                    if atend['employee_id'] == attendance_employee:
                                        attendancere_rquayeard_list.append(atend)
                                    Employes.make_attandance_xlsx_file(
                                        attendancere_rquayeard_list,
                                        f'Atendance of {get_obje(attendance_employee).full_name()}:')
                            break
                        else:
                            print(f'no employee with {attendance_employee} id number, pleas chack.')

                elif action_num45 == 4:
                    attendance_month = get_month_num()
                    with open('attendance_log.csv', 'r') as attendance_log:
                        attendance_list = csv.DictReader(attendance_log)
                        attendancere_rquayeard_list = []
                        for atend in attendance_list:
                            if int(atend['start_hour'][0:2]) > 9 and attendance_month == int(atend['date'][5:7]) \
                                    and get_obje(atend['employee_id']) in employee_obje.hayeard:
                                attendancere_rquayeard_list.append(atend)
                    Employes.make_attandance_xlsx_file(
                        attendancere_rquayeard_list,
                        f'Atendance of my late employees in the month: {attendance_month}')

                elif action_num45 == 5:
                    while True:
                        starting_employee_id = input('enter the employee id:')
                        if get_obje(starting_employee_id) in Employes.employees_objects:
                            print('set the start working date:')
                            while True:
                                try:
                                    date_y = int(input('year:'))
                                    if len(str(date_y)) == 4:
                                        break
                                    else:
                                        print('enter 4 numbers year.')
                                except ValueError:
                                    print('!please enter a number.!')
                            while True:
                                try:
                                    date_m = int(input('month:'))
                                    if 1 <= date_m <= 12:
                                        break
                                    else:
                                        print('enter month year between 1 - 12.')
                                except ValueError:
                                    print('!please enter a number.!')
                            while True:
                                try:
                                    date_d = int(input('day:'))
                                    if 1 <= date_d <= 31:
                                        break
                                    else:
                                        print('enter number of day between 1 - 31.')
                                except ValueError:
                                    print('!please enter a number.!')
                            for obj in Employes.employees_objects:
                                if obj.i_d == starting_employee_id:
                                    print(obj.set_start_working_date(date_y, date_m, date_d))
                            break
                        else:
                            print(f'no employee with {starting_employee_id} id number, pleas chack.')
                elif action_num45 == 6:
                    while True:
                        employee_id_to_apdate_atend = input('enter the employee id:')
                        if get_obje(employee_id_to_apdate_atend) in Employes.employees_objects:
                            with open('attendance_log.csv', 'r') as attendance_log:
                                attendance_list = csv.reader(attendance_log)
                                attendancere_as_list = []
                                for atend in attendance_list:
                                    attendancere_as_list.append(atend)
                            employee_obje_to_apdate_atend = get_obje(employee_id_to_apdate_atend)
                            while True:
                                date_with_form = input('enter date as the form 2023-01-01:')
                                if len(date_with_form) == 10 and date_with_form[4] == '-' and date_with_form[7] == '-':
                                    break
                                else:
                                    print('wrong form, try again.')
                            while True:
                                start_hour = input('enter start hour as the form 09:25 :')
                                if len(start_hour) == 5 and start_hour[2] == ':':
                                    break
                                else:
                                    print('wrong form, try again.')
                            while True:
                                finish_hour = input('enter finish hour as the form 09:25 :')
                                if len(finish_hour) == 5 and finish_hour[2] == ':':
                                    break
                                else:
                                    print('wrong form, try again.')
                            description = input('enter description or just hit enter:')
                            atte_add_row = employee_obje_to_apdate_atend.i_d, employee_obje_to_apdate_atend.full_name()\
                                , date, start_hour, finish_hour, description
                            attendancere_as_list.append(atte_add_row)
                            with open('attendance_log.csv', 'w', newline="") as attendance_log:
                                attendance_list = csv.writer(attendance_log)
                                for atend in attendancere_as_list:
                                    attendance_list.writerow(atend)
                            print(f"atend updated: {date}, {start_hour} - {finish_hour}")
                            break
                        else:
                            print(f'no employee with {employee_id_to_apdate_atend} id number, pleas chack.')

        else:
            print(f'action number {action_num} not in your actions list')


def activate():
    print('welcome to the Employee Attendance Management System!')
    employee_id = input('enter id:')
    if not employee_id.isdigit():
        '''or len(employee_id)!=9:'''
        print('enter id number, with 9 numbers')
    else:
        employee_obje = get_obje(employee_id)
        if employee_obje is None:
            print(f'no employee with {employee_id} id number, pleas chack.')
        else:
            print(f'Hello {employee_obje.full_name()}')
            print('actions available for you:')
            activating(employee_obje)
    activate()


activate()
