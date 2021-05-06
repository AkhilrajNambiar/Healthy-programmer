# #Healthy programmer
# 9am-5pm
#
# Water - water.mp3(assume it to be in this directory!) 3.5 litres water
# you can generate any type of reminder and once user has finished drinking
# and he presses enter he should be able to resume his job or you can
# ask user a boolean question.
# Also generate a log containing a timestamp that how much time did he take
# for drinking water
#
# Eyes - eyes.mp3(Every 30 minutes)
# Same  task over (Y/N) input at the end of each time
#create log as well

# Physical activity - physical.mp3(Every 45 minutes)
# Here also you can take boolean task over input from user
# create log as well


from PIL import Image
# a=8.0  #From 9 am to 5 pm we have 8 hrs
# b=3.5
# c=b/a
# print(c)#So we get that in average per hour you should drink 440ml
# Let us say that we remind the user to drink a glass of water every
# 30 minutes. So every 30 minutes he has to drink 220 ml of water
# that is the average volume of a glass of water
import time
import os

import exercise
import eyes

start = 0
#We will check the timer to start at 9 am
# if time.struct_time.tm_hour==9 and time.struct_time.tm_min==0 and time.struct_time.tm_sec==0:
#     start=time.localtime()

def waterdrinkstart():
    with open("waterlog.txt","a") as fi:
        if time.localtime().tm_wday==0:
            fi.write("[Monday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Started drinking water!\n")
        elif time.localtime().tm_wday==1:
            fi.write("[Tuesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Started drinking water!\n")
        elif time.localtime().tm_wday==2:
            fi.write("[Wednesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Started drinking water!\n")
        elif time.localtime().tm_wday==3:
            fi.write("[Thursday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Started drinking water!\n")
        elif time.localtime().tm_wday==4:
            fi.write("[Friday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Started drinking water!\n")
        elif time.localtime().tm_wday==5:
            fi.write("[Saturday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Started drinking water!\n")
        elif time.localtime().tm_wday==6:
            fi.write("[Sunday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Started drinking water!\n")

def waterdrinkover():
    with open("waterlog.txt", "a") as fi:
        if time.localtime().tm_wday==0:
            fi.write("[Monday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Stopped drinking water!\n")
        elif time.localtime().tm_wday==1:
            fi.write("[Tuesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Stopped drinking water!\n")
        elif time.localtime().tm_wday==2:
            fi.write("[Wednesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Stopped drinking water!\n")
        elif time.localtime().tm_wday==3:
            fi.write("[Thursday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Stopped drinking water!\n")
        elif time.localtime().tm_wday==4:
            fi.write("[Friday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Stopped drinking water!\n")
        elif time.localtime().tm_wday==5:
            fi.write("[Saturday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Stopped drinking water!\n")
        elif time.localtime().tm_wday==6:
            fi.write("[Sunday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Stopped drinking water!\n")

def approve():
    waterdrinkstart()
    val = input("Have you finished drinking water(Y/N) : ")
    m = val.upper()
    if m == "Y":
        waterdrinkover()
        return
    elif m == "N":
       try:
           m = input("Please press enter when you have finished drinking : ")
       except Exception as e:
           print("You cannot give integer as input!!")
       if m=="":
           waterdrinkover()
           return
       else:
           print("Don't press some other keys!!")


def waterLogCreate():
    with open("waterlog.txt","w") as f:
        f.write("Details of when you drank water today\n")

def waterread():
    with open("waterlog.txt") as f:
        print(f.read())

def water_start():
    start=time.localtime()
    i=0
    while True:
        if time.localtime().tm_hour < 17:
            if time.localtime().tm_min - start.tm_min == 2:
                wat = Image.open("water.jpg")
                wat.show()
                if i==0:
                    waterLogCreate()
                approve()
                i+=1
                start=time.localtime()#we have modified the value of start to be
                #the current localtime
        elif time.localtime().tm_hour==17:
            m=0
            try:
                m = input("Do you want to see the time spent in drinking water today(Y/N)!")
            except Exception as e:
                print("Only String input!")
            b=m.upper()
            if b=="Y":
                waterread()
                break
            elif b=="N":
                break
            else:
                print("Give proper input!")
                break
    return


if __name__ == "__main__":
    start = time.localtime()
    print("1.Drinking ample water")
    print("2.Eye care")
    print("3.Exercise")

    # choice 1
    c1 = input("Do you want to lock timer for drinking water(Y/N) : ")
    m = c1.upper()

    # choice 2
    c2 = input("Do you want to lock timer for eyes rest(Y/N) : ")
    n = c2.upper()

    # choice 3
    c3 = input("Do you want to lock timer for drinking water(Y/N) : ")
    o = c3.upper()

    # starting water timer
    if m == "Y":
        water_start()
    elif m == "N":
        print("OK")

    # starting eye care timer
    if n == "Y":
        eyes.eye_start()
    elif n == "N":
        print("OK")

    # starting exercise timer
    if o == "Y":
        exercise.exercise_start()
    elif o == "N":
        print("OK")



