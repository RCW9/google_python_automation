#!/usr/bin/env python3

import csv
import os
def read_employees(csv_file_location):
    with open(csv_file_location) as csv_file:
        csv_dict = csv.DictReader(csv_file)
        employee_list = []
        for dict  in csv_dict:
            employee_list.append(dict)
        return employee_list

employee_list = read_employees("/home/student-04-841d975be894/data/employees.csv")

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data[' Department'])
    department_data={}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
    with open(report_file, "w+") as file:
        for key in sorted(dictionary):
            file.write(str(key)+':'+str(dictionary[key])+'\n')


write_report(dictionary,"/home/student-04-841d975be894/test_report.txt")