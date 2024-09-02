TY, TM, TD = map(int,input().split())
DY, DM, DD = map(int,input().split())

def checkLeapYear(num):
    if num%400 == 0:
        return True
    elif num%100 == 0:
        return False
    elif num%4 == 0:
        return True
    else :
        return False 

def sol():
    global TY, TM, TD, DY, DM, DD
    nn = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    ll = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    dday = 0
    iscuryearleaf = checkLeapYear(TY)
    while True:
        if TY == DY and TM == DM and TD == DD:
            break
        TD += 1
        if iscuryearleaf == True:
            if ll[TM] < TD:
                TD = 1
                TM += 1
        else:
            if nn[TM] < TD:
                TD = 1
                TM += 1
        if TM > 12:
            TY += 1
            TM = 1
            iscuryearleaf = checkLeapYear(TY)
        dday += 1
    print("D-"+str(dday))

normal = {0:0, 1:31, 2:59, 3:90, 4:120, 5:151, 6:181, 7:212, 8:242, 9:273, 10:303, 11:334}
leaf = {0:0, 1:31, 2:60, 3:91, 4:121, 5:152, 6:182, 7:213, 8:244, 9:274, 10:305, 11:335}


'''
if DY-TY >= 1000 and DM>=TM and DD>=TD:
    print("gg")
else:
    Tdelay = (leaf[TM-1] if checkLeapYear(TY) else normal[TM-1]) + TD-1
    Ddelay = (leaf[DM-1] if checkLeapYear(DY) else normal[DM-1]) + DD-1

    # print(Tdelay, Ddelay)

    delay = Ddelay-Tdelay
    for i in range(TY, DY):
        if checkLeapYear(i):
            delay += 366
        else:
            delay += 365
    print('D-'+str(delay))
'''


if DY-TY > 1000 :
    print("gg")
elif DY - TY == 1000 :
    if DM>TM :
        print("gg")
    elif DM==TM and DD>=TD:
        print("gg")
    else:
        sol()
else:
    sol()


