"""
* @Author: Sachin S Kore
* @Date: 2021-11-16
* @Title :  To check employee using OOPS concept
"""
from logging import *
import random
import csv

import employee

company_list = []


class Employee:
    is_full_time = 1
    is_part_time = 2
    day_hour = 0

    def __init__(self):
        self.employee_name = ""
        self.wage_per_hour = 0
        self.maximum_working_days = 0
        self.maximum_working_hours = 0
        self.daily_wage_list = []
        self.total_wage = 0
        self.working_days = 0
        self.total_working_hours = 0

    def enter_data(self):

        try:
            self.employee_name = input("Enter Employee name : -")
            self.wage_per_hour = int(input("Enter Employee Wage Per Hour : -"))
            self.maximum_working_days = int(input("Enter Employee maximum working days : -"))
            self.maximum_working_hours = int(input("Enter Employee maximum working hours : -"))

        except ValueError:

            print("Please Enter Integer values")
            warning("Please Enter Integer values")

            employee.Employee.enter_data()

    def check_attendance(self):
        """
          Description:
              This function is to check whether employee is present or absent.
              Employee daily wage is calculated for full day and part time.
          """
        attendance = self.switch()

        if attendance == self.is_full_time:
            self.day_hour = 8
        elif attendance == self.is_part_time:
            self.day_hour = 4
        else:
            self.day_hour = 0

        return self.day_hour

    def calculate_wage(self):
        """
        Description:
            this function calculate employee wage
        Return:
            this function return total employee wage of a month
        """

        while self.working_days < self.maximum_working_days and self.total_working_hours < self.maximum_working_hours:
            working_hours = self.check_attendance()
            daily_wage = working_hours * self.wage_per_hour
            self.total_wage += daily_wage
            self.total_working_hours += working_hours
            self.working_days += 1

        return self.total_wage

    def switch(self):
        """
        Description:
            this function To using Switch for case
        Return:
            this function return Employee attendance
        """

        absent = 0
        full_present = 1
        part_present = 2

        switcher = {
            0: absent,
            1: full_present,
            2: part_present,
        }
        emp_check = random.randint(0, 2)
        attendance = switcher.get(emp_check)
        return attendance


class Company:
    employee_list = []
    list_start = 0
    list_length = 0
    total_wage = 0

    def __init__(self):
        self.row = []
        self.mult_row = []
        self.company_list = company_list
        self.fields = ['Company ', 'Employee', 'Salary', 'Days', 'Hours']
        self.employee_num = 0
        self.count = 0
        self.company_name = ""

    def add_employee(self):
        """
         Description:
              this function use To give input from user for Employee Quantity
         """
        try:
            self.employee_num = int(input("Enter Employee Quantity : -"))
            for employee_obj in range(self.employee_num):
                employee = Employee()
                employee.enter_data()
                self.employee_list.append(employee)

        except Exception:
            print("Please Enter Employee Quantity in Number")
            warning("Please Enter Employee Quantity in Number")


            company.add_employee()

    # def add_company(self):
    #     """
    #        Description:
    #             this function To use for adding Company
    #     """
    #     self.count = 1
    #     for company_obj in range(self.count):
    #         company.enter_company_data()
    #         self.company_list.append(company)

    def enter_company_data(self):
        self.company_name = input("Enter company name : -")

    def total_salary(self):
        """
        Description:
            this function To show total employee wage
        """

        for company_l in self.company_list:
            print("company name is ", company_l.company_name)
            self.list_length += self.employee_num
            for employee in self.employee_list[self.list_start:self.list_length]:
                print("Employee name is : -", employee.employee_name)
                print("Total Salary of Employee is : - ", employee.calculate_wage())
                print("Total working days : -", employee.working_days)
                print("Total working Hours : -", employee.total_working_hours)
                print("")
                self.row = [company_l.company_name, employee.employee_name, employee.calculate_wage(),
                            employee.working_days, employee.total_working_hours]
                self.mult_row.append(self.row)
                self.total_wage += employee.calculate_wage()
            print("total wage :", self.total_wage)
            self.total_wage = 0
            self.list_start += self.employee_num

    def csv_file(self):
        """
          Description:
                    this function Generating Employee detail CSV File
        """
        # name of csv file
        filename = "Employee_detail.csv"

        # writing to csv file
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)

            # writing the fields
            csvwriter.writerow(self.fields)

            # writing the data rows
            csvwriter.writerows(self.mult_row)


if __name__ == "__main__":
    """
    Description:
                To show menu of Employee
    """
    LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}'
    basicConfig(filename='logfile.log', level=DEBUG, filemode='w', style='{', format=LOG_FORMAT)

    while True:
        print("""
               1.Enter a new company
               2:Enter new employee
               3.display detail
               4.Csv
               5.exit`
               """)
        choice = int(input("Enter you choice :"))
        if choice == 1:
            count = 1
            for company_obj in range(count):
                company = Company()
                company.enter_company_data()
                company_list.append(company)
        elif choice == 2:
            company.add_employee()
        elif choice == 3:
            company.total_salary()
        elif choice == 4:
            company.csv_file()
        elif choice == 5:
            break
        else:
            print(" Wrong choice ..........")
            warning(" Wrong choice ..........")
