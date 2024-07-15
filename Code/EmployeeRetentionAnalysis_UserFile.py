#UserFile
print('\n----------------------------TechSol----------------------------\n')
import PMod
while 1:
    ch1=PMod.MainMenu()
    if ch1==1:
        while 1:
            ob=PMod.Menu()
            ch2=ob.CEOMenu()
            if ch2==1:
                PMod.EmpDe()
            elif ch2==2:
                PMod.EmpR()
            elif ch2==3:
                PMod.EmpFee()
            elif ch2==4:
                PMod.ShowEmpFeed()
            elif ch2==5:
                break
            else:
                print('Invalid choice')
    elif ch1==2:
        while 1:
            ch3=PMod.EmpMenu()
            if ch3==1:
                PMod.IndEmp()
            elif ch3==2:
                PMod.EmpQ()
            elif ch3==3:
                break
            else:
                print('Invalid choice')
    elif ch1==3:
        print('\n------------------Thank You...:)------------------')
        break
    else:
        print('Invalid choice')           