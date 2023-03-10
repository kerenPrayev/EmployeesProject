from datetime import datetime, date
import csv
import xlsxwriter


class Employes:
    number_of_employes = 0
    raise_amont = 1
    employees_objects = []

    def __init__(self, f_n, l_n, i_d, phone, adreass, b_d, job):
        self.f_n = f_n
        self.l_n = l_n
        self.i_d = i_d
        self.phone = phone
        self.adreass = adreass
        self.b_d = b_d
        self.job = job
        Employes.add_employe_to_employees(self)
        Employes.employees_objects.append(self)
        Employes.number_of_employes += 1

    def full_name(self):
        return f'{self.f_n} {self.l_n}'

    def age(self):
        today_date = datetime.today().date()
        today_year = int(today_date.year)
        birth_year = int(str(self.b_d)[0:4])
        age = today_year-birth_year
        return age

    def employe_email(self):
        return f'{self.f_n}_{self.l_n}@email.com'

    def set_start_working_date(self, y, m, d):
        self.start_working_date = date(y, m, d)
        return f'start working date updated to {self.start_working_date}'

    def count_time_of_work(self):
        now = datetime.now()
        print(self.start_working_date)
        y = now.year-self.start_working_date.year
        m = now.month-self.start_working_date.month
        d = now.day-self.start_working_date.day
        return f'{y} years, and {m} months, and {d} days'

    def add_employe_to_employees(self):
        with open('employees.csv', 'r+', newline="") as employees_file:
            old_employe = csv.reader(employees_file)
            with open('employees.csv', 'r+', newline="") as employees_file:
                updated_employe = csv.writer(employees_file)
                add_rew_info = self.f_n, self.l_n, self.i_d, self.phone, self.adreass, self.age(), self.job
                for row in old_employe:
                    updated_employe.writerow(row)
                updated_employe.writerow(add_rew_info)

    def removed_employe_from_employees(self):
        lines = list()
        with open('employees.csv', 'r', newline="") as employees_file:
            old_employees = csv.reader(employees_file)
            for row in old_employees:
                lines.append(row)
            for line in lines:
                if line[2] == str(self.i_d):
                    print(f'the employe is:{line}')
                    lines.remove(line)
        with open('employees.csv', 'w', newline="") as employees_file:
            updated_employees = csv.writer(employees_file)
            updated_employees.writerows(lines)

    def update_start_hour(self):
        now = datetime.now()
        now_date = now.date()
        hour = now.hour
        minuts = now.minute
        with open('attendance_log.csv', 'a', newline="") as atte_log:
            atte_add = csv.writer(atte_log)
            atte_add_row = self.i_d, self.full_name(), now_date, "%02d:%02d" % (hour, minuts), "", ""
            atte_add.writerow(atte_add_row)
        return "start hour updated: %02d:%02d" % (hour, minuts)

    def update_finish_hour(self, description):
        now = datetime.now()
        now_date = now.date()
        hour = now.hour
        minuts = now.minute
        lines = list()
        with open('attendance_log.csv', 'r') as attendance_file:
            old_attendance_file = csv.reader(attendance_file)
            for row in old_attendance_file:
                lines.append(row)
            for line in lines:
                if line[0] == str(self.i_d) and line[2] == str(now_date) and line[4] == "":
                    line[4] = "%02d:%02d" % (hour, minuts)
                    line[5] = description
                    break
            else:
                return 'no start hour was updated to you today that haven\'t been finished.\n' \
                       'so you can\'t add finish hour.\n' \
                       'if you forgat to updatee your start hour today,\n' \
                       'please contact your menagrer for help.'
        with open('attendance_log.csv', 'w', newline="") as attendance_file:
            updated_attendance_file = csv.writer(attendance_file)
            updated_attendance_file.writerows(lines)
        return "finish hour updated: %02d:%02d" % (hour, minuts)

    @ staticmethod
    def make_employes_xlsx_file():
        employees_xlsx = xlsxwriter.Workbook('employees.xlsx')
        all_employees_sheet = employees_xlsx.add_worksheet('employees')
        all_employees_sheet.write('A1', 'employe_id')
        all_employees_sheet.write('B1', 'employe_name')
        all_employees_sheet.write('C1', 'phone')
        all_employees_sheet.write('D1', 'age')
        num_of_employes_updeted = 0
        for employe in Employes.employees_objects:
            all_employees_sheet.write('A' + str(num_of_employes_updeted + 2), employe.i_d)
            all_employees_sheet.write('B' + str(num_of_employes_updeted + 2), employe.full_name())
            all_employees_sheet.write('C' + str(num_of_employes_updeted + 2), employe.phone)
            all_employees_sheet.write('D' + str(num_of_employes_updeted + 2), employe.age())
            num_of_employes_updeted += 1

        employees_xlsx.close()

    @staticmethod
    def make_attandance_xlsx_file(attendance_requayerd_list, title):
        wb = xlsxwriter.Workbook('attendance.xlsx')
        ws = wb.add_worksheet('attendance reqested')
        ws.write('A1', title)
        titels = ['date', 'full_name', 'employee_id', 'start_hour', 'finish_hour', 'description', 'sumerry']
        leter = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        for le in range(0, len(leter)):
            ws.write(leter[le]+'2', titels[le])
        row_index = 3
        dict_num = 0
        for row in range(0, len(attendance_requayerd_list)):
            attend_dict = attendance_requayerd_list[dict_num]
            for le in range(0, len(leter) - 1):
                ws.write(leter[le]+str(row_index), attend_dict[titels[le]])
            start_hour = attend_dict['start_hour']
            start_hour_round_hour = start_hour[0:2]
            start_hour_minutes = start_hour[3:5]
            try:
                start_hour_minutes = int(int(start_hour_minutes)/60*100)
            except ValueError:
                start_hour_minutes = 0
            finish_hour = attend_dict['finish_hour']
            finish_hour_round_hour = finish_hour[0:2]
            finish_hour_minutes = finish_hour[3:5]
            try:
                finish_hour_minutes = int(int(finish_hour_minutes)/60*100)
            except ValueError:
                finish_hour_minutes = 0
            finally:
                start_hour_float = float(f'{start_hour_round_hour}.{start_hour_minutes}')
                finish_hour_float = float(f'{finish_hour_round_hour}.{finish_hour_minutes}')
                if start_hour_minutes <= finish_hour_minutes:
                    ws.write('G'+str(row_index), finish_hour_float-start_hour_float)
                else:
                    ws.write('G' + str(row_index),
                             (int(finish_hour_round_hour) - int(start_hour_round_hour) - 1) +
                             ((100 - start_hour_minutes) + finish_hour_minutes) / 100)
            row_index += 1
            dict_num += 1
        wb.close()
        print('your file is ready, please check in the directory.')

    @staticmethod
    def get_month_num():
        attendance_month = None
        while attendance_month is None:
            try:
                attendance_month = int(input('enter month number:'))
                if 1 <= attendance_month <= 12:
                    break
                else:
                    print('please enter a month number between 1 - 12.')
                    attendance_month = None
            except Exception as e:
                print('!please enter a number.!')
                print(e)
                attendance_month = None
        return attendance_month
