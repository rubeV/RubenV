def inputvalues(Bus):
    for i in range(0,20):
        Bus[i] = int(input("Enter bus time for day " + str(i+1) + ": "))

def latearrivals(Bus):
    Late_Arrivals = 0
    for i in range(0,20):
        if Bus[i] < 0:
            Late_Arrivals += 1
    print("Late arrivals: " + str(Late_Arrivals))
    return Late_Arrivals

def avgtime(Bus):
    sumtotal = 0
    for i in range(0,20):
        sumtotal += Bus[i]
    print("Average number of minutes late or early: " + str(sumtotal/20))

def avglate(Bus):
    total = 0
    div = 0
    for i in range(0,20):
        if Bus[i] < 0:
            total += Bus[i]
            div +=1
    if div != 0:
        print("Average minutes late: " + str(total/div))
    else:
        print("Never late")

def anl_into_day(day):
    Day = ""
    for i in range(0,3): 
        Day += day[i]
    return Day

def validday(day):
    Day = ""
    for i in range(0,3): 
        Day += day[i]
    if Day != "Mon" or "mon" or "Tue" or "tue" or "Wed" or "wed" or "Thu" or "thu" or "Fri" or "fri":
        return True
    else: 
        return False
    

def anl_into_week(day):
    Week = 0
    Week = 5 * (int(day[3])-1)
    return Week
    
BusA = [0,0,0,2,2,4,0,3,4,-2,-5,0,0,3,4,-1,8,1,1,-2]
BusB = [0,1,0,0,1,2,0,0,0,0,1,0,0,0,2,0,0,1,0,0]
BusC = [2,0,-1,-1,-2,-2,-3,-1,0,0,-2,0,1,1,1,1,-1,-1,2,-2]
BusD = [1,0,0,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0]
BusE = [-1,-1,-1,-2,-4,-10,-2,0,0,0,0,1,2,-3,1,1,3,-1,0,0]
BusF = [0,-5,-5,-5,-4,-3,-5,0,0,0,0,-2,-3,1,1,1,0,0,-2,-5]
Buses = [BusA, BusB, BusC, BusD, BusE, BusF] 

reply = input("Enter own data y/n?")

if reply == "y":
    inputvalues(BusA)
    inputvalues(BusB)
    inputvalues(BusC)
    inputvalues(BusD)
    inputvalues(BusE)
    inputvalues(BusF)
    
latebuses = [latearrivals(BusA), latearrivals(BusB), latearrivals(BusC), latearrivals(BusD), latearrivals(BusE), latearrivals(BusF)]
latest = 0
for i in range(0,6):
    if int(latebuses[i]) > latest:
        latest = i + 1
if latest == 1:
    print("BusA is late most often")
elif latest == 2:
    print("BusB is late most often")
elif latest == 3:
    print("BusC is late most often")
elif latest == 4:
    print("BusD is late most often")
elif latest == 5:
    print("BusE is late most often")
elif latest == 6:
    print("BusF is late most often")

avgtime(BusA)
avgtime(BusB)
avgtime(BusC)
avgtime(BusD)
avgtime(BusE)
avgtime(BusF)

avglate(BusA)
avglate(BusB)
avglate(BusC)
avglate(BusD)
avglate(BusE)
avglate(BusF)

while True:
    Continue = input("Analyse day? y/n ")
    if Continue == "n":
        break
    elif Continue == "y":
        day_analysis = "WWW"
        validday(day_analysis) 
        if validday(day_analysis) == False:
            day_analysis = input("Which day would you like to analyse? Please use correct format e.g. Mon4 ")
        
        Day = anl_into_day(day_analysis)
        Week = anl_into_week(day_analysis)
        DayOfTheWeek = 0
        if Day == "Mon" or "mon":
            DayOfTheWeek += 1
        elif Day == "Tue" or "tue":
            DayOfTheWeek += 2
        elif Day == "Wed" or "wed":
            DayOfTheWeek += 3
        elif Day == "Thu" or "thu":
            DayOfTheWeek += 4
        elif Day == "Fri" or "fri":
            DayOfTheWeek += 5
       
        Analysis = Week + DayOfTheWeek 
        total = 0
        if BusA[Analysis] < 0:
            total += 1
            print("BusA is late by " + str(-1*(BusA[Analysis])) + "minutes")
        if BusB[Analysis] < 0:
            total += 1
            print("BusB is late by " + str(-1*(BusB[Analysis])) + "minutes")
        if BusC[Analysis] < 0:
            total += 1
            print("BusC is late by " + str(-1*(BusC[Analysis])) + "minutes")
        if BusD[Analysis] < 0:
            total += 1
            print("BusD is late by " + str(-1*(BusD[Analysis])) + "minutes")
        if BusE[Analysis] < 0:
            total += 1
            print("BusE is late by " + str(-1*(BusE[Analysis])) + "minutes")
        if BusF[Analysis] < 0:
            total += 1
            print("BusF is late by " + str(-1*(BusF[Analysis])) + "minutes")
        print(str(total) + "Bus(es) are late") 
        

