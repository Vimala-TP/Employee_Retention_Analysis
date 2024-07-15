#Module File
#Authentication
aut={'TCS001':['sj001'],
     'TCS006':['pi006'],
     'TCS165':['ms165'],
     'TCS008':['jn008']}
#Current Employee Details who r present in company
emp={'TCS001':['Swaraj',8855216947,'Project Head','16/03/2022','16/03/2027','5 years',500000,'swaraj01@gmail.com',10,'-'],
     'TCS006':['Prakruti',9984854513,'Software Developer','05/04/2021','-','-',800000,'prakruti12@gmail.com',12,'-'],
     'TCS165':['Manas',8654321365,'Data Analyst','12/01/2022','12/01/2028','6 years',600000,'manas65@gmail.com',9,'-'],
     'TCS008':['John',8657146358,'System Architect','10/03/2020','-','-',1000000,'johnn5@gmail.com',11,'-']}	
#Employee reason for quiting a job
q={'TCS001':['Swaraj','-'],
   'TCS006':['Prakruti','-'],
   'TCS165':['Manas','-'],
   'TCS008':['John','-']}	
#Feedback to Employees
fee={'TCS001':['Swaraj','-'],
     'TCS006':['Prakruti','-'],
     'TCS165':['Manas','-'],
     'TCS008':['John','-']}
def MainMenu():
    print('''\nEnter the type of candidate
    1.CEO of company
    2.Employee
    3.Exit''')
    while 1:
        try:
            ch1=int(input('='))
            break
        except ValueError as e:
            print('Invalid Choice  ',e)
    return ch1
class Menu:
    def CEOMenu(self):
        print('''\n-----Menu for CEO of Company-----
        1.View the employee details
        2.View the resigned employee details
        3.Give feedback to employees
        4.Show feedbacks given to employees 
        5.Exit''')
        while 1:
            try:
                ch2=int(input('Enter your choice ='))
                break
            except ValueError as e:
                print('Invalid Choice  ',e) 
        return ch2 
def EmpMenu():
    print('''\n-----Employee Menu-----
    1.Login
    2.Quit the Job
    3.Exit''')
    while 1:
        try:
            ch3=int(input('Enter your choice ='))
            break
        except ValueError as e:
            print('Invalid Choice  ',e)
    return ch3
def IndEmp():
    print('\n--------------------Login Page--------------------')
    idd=input('Enter your id = ')
    if (idd in emp) :
        pwd=input('Enter Password = ')	
        if (aut[idd][0]==pwd):
            print('Employee page')
            print('''\n\n-----Your Details-----
ID                : {}
Name              : {}
Contact number    : {}
Designation       : {}
Start Date        : {}
End Date          : {}
Contract          : {}
Salary            : {}
Mail id           : {}
Working hours     : {} houres'''.format(idd,emp[idd][0],emp[idd][1],emp[idd][2],emp[idd][3],emp[idd][4],emp[idd][5],emp[idd][6],emp[idd][7],emp[idd][8]))
            while 1:
                try:
                    f=int(input('Enter your Feedback to the company(1-10) = '))
                    break
                except ValueError as e:
                    print('Invalid Feedback it should range from 1-10',e)
            if f<=3 and f>=0:
                emp[idd].pop()
                emp[idd].append('Good') 
            elif f<=7 and f>3:
                emp[idd].pop()
                emp[idd].append('Better')
            else:
                emp[idd].pop()
                emp[idd].append('Best')
        else:
            print('Invalid Password')
    else:
        print('Invalid id')
def EmpQ():
    idd=input('Enter your id = ')
    print('''1.Insufficiant salary
2.Heavy work load
Any number(except 1 and 2) for other reason''')
    r=int(input('Select your reason to quit the job = '))
    if r==1:
        emp[idd][6]=((10/100)*emp[idd][6])+emp[idd][6]
        print('Your salary has been updated with 10%')
        return;
    elif r==2:
        emp[idd][8]=emp[idd][8]-1
        print('Your working houres is reduced by 1 houre')
        return;
    emp.pop(idd)
    r1=input('Enter your reason = ')
    q[idd].pop()
    q[idd].append(r1)
def EmpDe():
    print('''{:<10} {:<10} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<15} {:<15} '''.format('\nID','Name','Ph.no','Designation','Start date','End Date','Contract','Salary','Mail id','Working houres','Feedback to company'))
    print('-------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    for key,value in emp.items():
        i=key
        Name,Ph,Designation,Startdate,EndDate,Contract,Salary,Mail_id,whours,Feedback=value
        print('''{:<10} {:<10} {:<15} {:<20} {:<15} {:<15} {:<15} {:<15} {:<25} {:<15} {:<15}  '''.format(i,Name,Ph,Designation,Startdate,EndDate,Contract,Salary,Mail_id,whours,Feedback))
def EmpR():
    print('''Resigned Employee Details\n''')
    print('{:<15} {:<10} {:<15}'.format('\nEmployee_id','Name','Reason'))
    print('------------------------------------------------------------------------------')
    for key,value in q.items():
        i=key
        name,reason=value
        if i not in emp:
            print('{:<15} {:<10} {:<15}'.format(i,name,reason))
def EmpFee():
    print('\nFeedback for employees')
    iid=input('Enter employee id = ')
    if iid in emp:
        while 1:
            try:
                f=int(input('Enter your Feedback(1-10) to the employee {} = '.format(fee[iid][0])))
                break
            except Exception as e:
                print('Invalid Feedback it should range from 1-10',e)
        if f<=3 and f>=0:
            fee[iid].pop()
            fee[iid].append('Good') 
        elif f<=7 and f>3:
            fee[iid].pop()
            fee[iid].append('Better')
        else:
            fee[iid].pop()
            fee[iid].append('Best')
    else:
        print('Invalid id')
def ShowEmpFeed():
            print('{:<15} {:<10} {:<15}'.format('\nEmployee_id','Name','Feedback'))
            print('------------------------------------------------')
            for key,value in fee.items():
                ii=key
                namee,fbb=value
                if ii in emp:
                    print('{:<15} {:<10} {:<15}'.format(ii,namee,fbb))