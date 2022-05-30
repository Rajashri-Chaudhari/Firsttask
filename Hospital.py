print()
print('--------------------------* Heuristic Multi Specility Hospital *-------------------------')
patient=input('Please enter name of patient : ')
print(f'Hello ,{patient} Welcome to our Heuristic Multi Speciality Hospital .')
print("--------------------------------------------------------------------------")
print('Please select your problem from the list given below : ')
problem=int(input('\t1)Brain\n\t2)Eye\n\t3)Ear\n\t4)Kidney\n\t5)Accidental care \n'))
age=float(input('Please, Enter your age : '))
if age<60:
    print('-------------------* Patient Info *--------------------------')
    print(f'Name of patient:  {patient}\nAge:  {age}')

    if age>0 and age <=20:
        if problem ==1:
            print("Allocated to Brain section room no.1 ")
        elif problem==2:
            print("Allocated to Eye section room no.1 ")
        elif problem==3:
            print('Allocated  to Ear section room no.1')
        elif problem==4:
            print('Allocated to Kidney section room no.1')
        elif problem==5:
            print('Allocated to Accidental care room no.1 ')
        else:
            print('Please enter valid number from above list.')
    elif age>=21 and age <=40:
        if problem ==1:
            print("Allocated to Brain section room no.2 ")
        elif problem==2:
            print("Allocated to Eye section room no.2 ")
        elif problem==3:
            print('Allocated  to Ear section room no.2')
        elif problem==4:
            print('Allocated to Kidney section room no.2')
        elif problem==5:
            print('Allocated to Accidental care room no.2 ')
        else:
            print('Please enter valid number from above list.')
    elif age>=41 and age <=60:
        if problem ==1:
            print("Allocated to Brain section room no.3 ")
        elif problem==2:
            print("Allocated to Eye section room no.3 ")
        elif problem==3:
            print('Allocated  to Ear section room no.3')
        elif problem==4:
            print('Allocated to Kidney section room no.3')
        elif problem==5:
            print('Allocated to Accidental care room no.3 ')
        else:
            print('Please enter valid number from above list.')
else:
    print('Please enter age below 60')


print('-----------------* Praying for your speedy recovery :) *-----------------------')
