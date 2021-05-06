from PIL import Image
import time


def exerciseStarts():
    with open("exerciselog.txt", "a") as fi:
        if time.localtime().tm_wday==0:
            fi.write("[Monday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise starts!\n")
        elif time.localtime().tm_wday==1:
            fi.write("[Tuesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise starts!\n")
        elif time.localtime().tm_wday==2:
            fi.write("[Wednesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise starts!\n")
        elif time.localtime().tm_wday==3:
            fi.write("[Thursday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise starts!\n")
        elif time.localtime().tm_wday==4:
            fi.write("[Friday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise starts!\n")
        elif time.localtime().tm_wday==5:
            fi.write("[Saturday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise starts!\n")
        elif time.localtime().tm_wday==6:
            fi.write("[Sunday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise starts!\n")

def exerciseOver():
    with open("exerciselog.txt","a") as fi:
        if time.localtime().tm_wday==0:
            fi.write("[Monday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise finished!\n")
        elif time.localtime().tm_wday==1:
            fi.write("[Tuesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise finished!\n")
        elif time.localtime().tm_wday==2:
            fi.write("[Wednesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise finished!\n")
        elif time.localtime().tm_wday==3:
            fi.write("[Thursday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise finished!\n")
        elif time.localtime().tm_wday==4:
            fi.write("[Friday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise finished!\n")
        elif time.localtime().tm_wday==5:
            fi.write("[Saturday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise finished!\n")
        elif time.localtime().tm_wday==6:
            fi.write("[Sunday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Exercise finished!\n")

def exeapprove():
    exerciseStarts()
    val = input("Have you completed your exercise?(Y/N) : ")
    m = val.upper()
    if m == "Y":
        exerciseOver()
        return
    elif m == "N":
       try:
           m = input("Please press enter when you have finished exercising : ")
       except Exception as e:
           print("Please press enter only!!")
       if m == "":
           exerciseOver()
           return
       else:
           print("Don't press some other keys!!")


def exerciseLogCreate():
    with open("exerciselog.txt", "w") as f:
        f.write("Exercised Time : \n")


def exeread():
    with open("exerciselog.txt") as f:
        print(f.read())

def exercise_start():
    start_exer = time.localtime()
    i=0
    while True:
        if time.localtime().tm_hour < 17:
            if time.localtime().tm_min - start_exer.tm_min == 1:
                exer = Image.open("exercise.png")
                exer.show()
                if i == 0:
                    exerciseLogCreate()
                exeapprove()
                i += 1
                start_exer = time.localtime() # we have modified the value of start to be
                # the current localtime
        elif time.localtime().tm_hour == 17:
            m=0
            try:
                m = input("Do you want to see the time spent in exercises today(Y/N)!")
            except Exception as e:
                print("Only String input!")
            b = m.upper()
            if b == "Y":
                exeread()
                break
            elif b == "N":
                break
            else:
                print("Give proper input!")
                break
    return


if __name__ == "__main__":
    exercise_start()