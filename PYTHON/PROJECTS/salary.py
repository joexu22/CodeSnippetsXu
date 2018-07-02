"""
Author: Joe Xu
Calculates the salary of employee taking account of regular hours and overtime
"""
import math

def main():
    """
    Input hourly wage, total regular hours, and total overtime hours and calc
    """
    wage = float(input("hourly wage: "))
    hours = float(input("total regular hours: "))
    overtime = float(input("total overtime hours: "))

    weekly_pay = wage*hours + 1.5*wage*overtime
    print("The weekly pay is: ${:.2f}".format(weekly_pay))

if __name__ == "__main__":
    main()