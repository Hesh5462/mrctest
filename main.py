import time,sys

vistor_list = []
vistor_cnt = int(0)
work = True

def in_or_out(vistor_cnt):
    print('Check in : 1\nCheck out : 2\nShow List : 3')
    choose = input('Check in or out:')
    if choose is '1' :
        return vistor_in(vistor_cnt)
    elif choose is '2':
        return vistor_out(vistor_cnt)
    elif choose is '3':
        for i in vistor_list:
            print('Vistor :',i[0],'\n','Entry Time :',i[1],'\n','Leave Time :',i[2])
    else:
        print('Unknow command')
        return in_or_out(vistor_cnt)
def vistor_out(vistor_cnt):
    vistor_name = input('Please type your name:')
    vistor_out_time = time.ctime(time.time())
    if checkvistor(vistor_name) == False:
        for i in vistor_list:
            if vistor_name == i[0] and i[2] == 0:
                i.insert(2,vistor_out_time)
        print('Good Bye,', vistor_name, ' Leave Time:', vistor_out_time)
        vistor_cnt = vistor_cnt - 1
        print(vistor_cnt,'People in office')
        return vistor_cnt
    else:
        print('You have to check in first')

def vistor_in(vistor_cnt):
    vistor_name = input('Please type your name:')
    vistor_in_time = time.ctime(time.time())
    if checkvistor(vistor_name) == False:
        print('You are already in')
        return vistor_in(vistor_cnt)
    else:
        vistor_list.append([vistor_name, vistor_in_time, 0])
        print('Welcome,', vistor_name, ' Entry time:', vistor_in_time)
        vistor_cnt = vistor_cnt + 1
        print(vistor_cnt,'People in office')
        return vistor_cnt

def checkvistor(name):
    for i in vistor_list:
        if name == i[0] and i[2] == 0:
            return False

while(work is True):
    vistor_cnt = in_or_out(vistor_cnt)

