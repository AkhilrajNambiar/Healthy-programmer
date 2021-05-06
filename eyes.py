from PIL import Image
import time


def eyeLogCreate():
    with open("eyelog.txt", "w") as f:
        f.write("The time you gave a break for your eyes : \n")


def eyeRestStarts():
    with open("eyelog.txt", "a") as fi:
        if time.localtime().tm_wday==0:
            fi.write("[Monday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak starts!\n")
        elif time.localtime().tm_wday==1:
            fi.write("[Tuesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak starts!\n")
        elif time.localtime().tm_wday==2:
            fi.write("[Wednesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak starts!\n")
        elif time.localtime().tm_wday==3:
            fi.write("[Thursday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak starts!\n")
        elif time.localtime().tm_wday==4:
            fi.write("[Friday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak starts!\n")
        elif time.localtime().tm_wday==5:
            fi.write("[Saturday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak starts!\n")
        elif time.localtime().tm_wday==6:
            fi.write("[Sunday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak starts!\n")

def eyeRestOver():
    with open("eyelog.txt","a") as fi:
        if time.localtime().tm_wday==0:
            fi.write("[Monday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak finished!\n")
        elif time.localtime().tm_wday==1:
            fi.write("[Tuesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak finished!\n")
        elif time.localtime().tm_wday==2:
            fi.write("[Wednesday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak finished!\n")
        elif time.localtime().tm_wday==3:
            fi.write("[Thursday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak finished!\n")
        elif time.localtime().tm_wday==4:
            fi.write("[Friday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak finished!\n")
        elif time.localtime().tm_wday==5:
            fi.write("[Saturday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak finished!\n")
        elif time.localtime().tm_wday==6:
            fi.write("[Sunday : "+str(time.localtime().tm_hour)+":"+
              str(time.localtime().tm_min)+":"+str(time.localtime().tm_sec)+" ]")
            fi.write(" Eyebreak finished!\n")

def eyeapprove():
    eyeRestStarts()
    val = input("Have you completed eye rest?(Y/N) : ")
    m = val.upper()
    if m == "Y":
        eyeRestOver()
        return
    elif m == "N":
       try:
           m = input("Please press enter when you have finished rest : ")
       except Exception as e:
           print("You cannot give integer as input!!")
       if m=="":
           eyeRestOver()
           return
       else:
           print("Don't press some other keys!!")

def eyeread():
    with open("eyelog.txt") as f:
        print(f.read())

def eye_start():
    start = time.localtime()
    i = 0
    while True:
        if time.localtime().tm_hour < 17:
            if time.localtime().tm_min - start.tm_min == 20:
                eye = Image.open("eye.jpg")
                eye.show()
                if i==0:
                    eyeLogCreate()
                eyeapprove()
                i+=1
                start=time.localtime()#we have modified the value of start to be
                #the current localtime
        elif time.localtime().tm_hour == 17:
            m=0
            try:
                m = input("Do you want to see the time spent in eye rest today(Y/N)!")
            except Exception as e:
                print("Only String input!")
            b=m.upper()
            if b == "Y":
                eyeread()
                break
            elif b == "N":
                break
            else:
                print("Give proper input!")
                break
    return


if __name__ == "__main__":
    start = time.localtime()
    eye_start()