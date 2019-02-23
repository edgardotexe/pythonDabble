#23 Februar, 2019

import datetime
from time import localtime, strftime

def clockIn(empDB):

    while True:
        print(strftime('%Y-%m-%d %H:%M:%S', localtime()))
        empID = input('Enter your ID: ')
        
        if empID not in empDB:
            print('ACCESS DENIED!\n')
        else:
            print('Clocked IN at\n' + strftime('%Y-%m-%d %H:%M:%S', localtime()))
    
"""    
def newEmployee(empDB):

    empName = input('Enter a new employee: ')

    if empName in empDB:
        print(empDB[empName] + ' already exist in the database.\n')
    else:
        empLname = input('Enter ' + empName + '\'s last name: ')
        empDB[empName] = empLname


empDB = {}
jobNum = []


print(empDB)
newEmployee(empDB)
print(empDB)
"""
empID = ['043']
#print(datetime.datetime.now())
clockIn(empID)
    

