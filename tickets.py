print()
print('Read the instructions carefully!!')
print()
s = ['Bangalore', 'Chennai', 'Madurai', 'Vijayawada', 'Vizag']
cls = ['first_ac','second_ac', 'third_ac', 'sleeper']
cost = [1200,900,600,300,100]
print('This train is going to stop only in :', s)
print('The available classes are : ', cls)
print('NOTE : Train will not be available on month ends!!. And you can book tickets for journey which you wish to travel after 9 months')
print()
start = input('Enter your starting place : ')
end = input('Enter your destination place : ')
if (start not in s) or (end not in s):
    print('This train is going to stop only in :', s)
    print('So select valid starting place and destination place')
    print('Again start the process from beggening!!')
elif start==end:
    print('Your starting place and destination place cannot be same')
else:
    passengers = int(input('Total no.of passengers : '))
    ph_no = input('Enter mobile number of passenger : ')
    start_time = int(input('Enter the start time(in 24hrs)(only in hrs) : '))
    start_date, start_month = map(int,input("Enter starting date and month(seperated with ',') : ").split(','))
    c=1
    while c>0:
        clas = input('class : ')
        if clas in cls:
            c-=1
        else:
            print('Enter the valid class type!!')
    name = []
    age = []
    gender = []
    for i in range(passengers):
        n = input('Enter name of person : ')
        a = input('Enter age of person : ')
        g = input('Enter gender of person : ')
        name.append(n)
        age.append(a)
        gender.append(g)
    s_ind = s.index(start)
    e_ind = s.index(end)
    c_ind = cls.index(clas)
    cost_ind = int(cost[c_ind])
    distance = (abs(s_ind-e_ind))*500
    time = (abs(s_ind-e_ind))*6
    end_time = (start_time+time)%24
    end_date = (start_date)+((start_time)//24)
    price = distance*(cost_ind)

    l1 = []
    l2 = []
    l3 = []
    l7=  []
    a = "A"
    b = "B"
    c = "C"

    for i in range(1, 11, 1):
        l1.append(f"{a}{i}")
    for i in range(1, 16, 1):
        l2.append(f"{b}{i}")
    for i in range(1, 21, 1):
        l3.append(f"{c}{i}")
    l4 = l1 + l2 + l3
    l6 = l4
    g=0
    while g==0:  # no of entries that day
        count = len(l4)
        g = g+0
        if count > 0:
            print("Number seats available : ", count)

            print("Please choose the seat")
            print(l4)

            l5 = list(map(str, input("Enter the Seat no's(seperated by ',') : ").split(",")))

            for i in l5:
                if i in l4:
                    l4.remove(i)
                    g=g-1
                    l7.append(i)
                else:
                    print("enter correct seat no")
                    print("Please enter the wrong seat number  correctly again")
                    g=g*0

    print()
    print()
    print('Boarding place :', start)
    print('Time of boarding :', start_time)
    print('Date and month of boarding :', start_date, ',', start_month)
    print('Arraival place :', end)
    print('Time of arraival :', end_time)
    print('Date and month of arraival :', end_date, ',', start_month)
    print('Total distance(in km) :', distance)
    print('Total time taken(in hrs) :', time)
    print('Passenger mobile number :', ph_no)
    print('Total cost :', price)
    print()
    print('Passengers details : ')
    details = {}
    for i in range(passengers):
        details['S.n0']=i+1
        details['Name']=name[i]
        details['Age']=age[i]
        details['Gender']=gender[i]
        print(details)
        details['S.n0']=''
        details['Name']=''
        details['Age']=''
        details['Gender']=''

    print("seat no's : ",l7)