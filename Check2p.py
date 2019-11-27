#!/usr/bin/env python3
'''Prelimary grading script for assignment 2P
   more tests are pending
'''
import sys

student_id = 'rchan'
class_file = 'a2_class'+student_id

try:
    from a2_class import *
except ImportError:
    print('Error trying to import a2_class.')
    sys.exit()

test_dates = {1:[(2019,11,5),(2019,11,6),(2019,11,4)],
              2:[(2019,2,28),(2019,3,1),(2019,2,27)],
              3:[(2019,1,1),(2019,1,2),(2018,12,31)],
              4:[(2019,12,31),(2020,1,1),(2019,12,30)],
              5:[(1999,12,31),(2000,1,1),(1999,12,30)],
              6:[(2000,2,28),(2000,2,29),(2000,2,27)],
              7:[(2000,3,1),(2000,3,2),(2000,2,29)],
              8:[(2016,12,31),(2017,1,1),(2016,12,30)],
              9:[(2016,2,28),(2016,2,29,),(2016,2,27)],
             10:[(2016,3,1),(2016,3,2),(2016,2,29)],
             11:[(2019,7,31),(2019,8,1),(2019,7,30)],
             12:[(2019,8,31),(2019,9,1),(2019,8,30)],
             13:[(2019,10,1),(2019,10,2),(2019,9,30)],
             14:[(2019,11,30),(2019,12,1),(2019,11,29)]}

total_test_score = 0
for testno in range(1,15):
    test_date = test_dates[testno][0]
    test_tm = test_dates[testno][1]
    test_ys = test_dates[testno][2]

    str_test_tm = '%.4d/%.2d/%.2d' % test_tm
    str_test_ys = '%.4d/%.2d/%.2d' % test_ys
    y,m,d = test_date

    date1 = Date(y,m,d)
    test_header='Testing for Date class - Test number: '+str(testno)
    print(test_header)
    print(len(test_header)*'-')

    test_score = 0
    print('Test for date1:',date1)
    print('date1  is:',date1)
    print('  expected tomorrow should be:',test_tm)
    print('     your date1.tomorrow() is:',date1.tomorrow())
    if str(date1.tomorrow()) == str_test_tm:
         test_score += 1
         print('Test for tomorrow method: passed')
    else:
         print('Test for tomorrow method: failed')
    print('  expected yesterday should be:',test_ys)
    print('     your date1.yesterday() is:',date1.yesterday())
    if str(date1.yesterday()) == str_test_ys:
         test_score += 1
         print('Test for yesterday method: passed')
    else:
         print('Test for yesterday method: failed')
    print(5*' ','test result: '+str(test_score)+'/2')
    total_test_score += test_score
    print(50*'=')

print('Maximum total test score:',len(test_dates)*2)
print('Total test score for this test run:',total_test_score)
