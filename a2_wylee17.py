#!/usr/sbin/env python3
"""
OPS435 Assignment 2P - Fall 2019
Program: a1_wylee17.py (replace student_id with your Seneca User name)
Author: "Wonyoung Lee"
The python code in this file (a1_wylee17.py) is original work written by
"Wonyoung Lee". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.
"""

import os,sys


class Date:
    """
This class is designed for date change    
"""
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day 

    def __repr__(self):
        months = str(self.month).zfill(2)
        return f"{self.year}-{months}-{self.day}"

    def __str__(self):
        months = str(self.month).zfill(2)
        return f"{self.year}/{months}/{self.day}"
    
    def __add__(self,other):
        return self.day + other.day
    
    def __sub__(self,other):
        return self.day - other.day
    
    def days_to_time(self):
        pass


    def dbda(self):
        '''
Call tomorrow if the date is greater than 0, call yesterday if the date is less than 0.        
'''
        for i in range(self.day):
            self.date = tomorrow(self.date)
            print(self.date)
        if self.days == 0:
            pass

    
        for i in range(-self.days):
            self.date = yesterday(self.date)
            #print('negative')
        print(self.date)
        return self.date

    
    def leap_year(self, year):
        
        if (year % 4) == 0: 
            if (year % 100) == 0:
                if (year % 400) == 0:
                    leapyear = True
                else: 
                    leapyear = False
            else:
                leapyear = True   
        else: 
            leapyear = False   
        
        return leapyear


    def days_in_mon(self, year):
        '''
    This function outputs the maximum date of the leap month        
'''
        if self.leap_year(self.year):
            feb_max = 29
        else:
            feb_max = 28

        self.mon_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, \
        6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        return self.mon_max


    def valid_date(self, date):
        '''
       This function checks the date which is valid or invalid
       ''' 
        year = int(self.year[:4])
        month = int(self.month[5:7])
        day = int(self.day[8:])
        date = self.date

        if self.month > 12: 
            print("Error: Invalid month")
            sys.exit()
        elif self.day >31:
            print("Error: Invalid day")
            sys.exit()

    def tomorrow(self):   
        '''
       This function outputs the next day through another function        
'''
        str_year = self.year
        str_month = self.month
        str_day = self.day
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        mon_max = self.days_in_mon(year)
        

        tmp_day = day + 1 #tomorrow

        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month] #if tmp_day is maximum date, add 1 for month
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1 #if tmp_month is maximum date, add 1 for year
            year = year + 1
        else:
            to_month = tmp_month + 0

        tmr_date = str(year)+"/"+str(to_month).zfill(2)+"/"+str(to_day).zfill(2)
        
        return tmr_date


    def yesterday(self):
        '''
       This function outputs the previous day through another function 
        '''
        str_year = self.year
        str_month,self.month,self.day
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)
        mon_max = self.days_in_mon(year)
        
            
        tmp_day = day - 1
            

        if tmp_day == 0: 
            month = month - 1
            if month == 0: 
                year -= 1
                month = 12
                tmp_day = mon_max[month]
                
            else:
                tmp_day = mon_max[month]
        else:
            year -= 0
            month -= 0
            
        next_date = str(year)+"/"+str(month).zfill(2)+"/"+str(tmp_day).zfill(2)

        return next_date

    if __name__ == "__main__":
        
        #usage()
        """
        if len(sys.argv) > 1 and sys.argv[1] != '--step': 
            date = sys.argv[1]
            days = sys.argv[2]
            dbda(date,days)
            for i in range(1, days + 1):
                #print(i)
                dbda(date,i)
                """

        """
        elif sys.argv[1] == '--step':
            date = sys.argv[2]
            days = int(sys.argv[3])
            #steps = sys.argv[3]
            #steps = str(days)
        """
        


