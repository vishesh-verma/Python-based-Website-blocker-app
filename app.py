from datetime import datetime as dt
import time
ip="127.0.0.1"#redirect
website=["www.facebook.com","www.google.com"]#websites to be blocked

while True:
    if(dt(dt.now().year,dt.now().month,dt.now().day,14) > dt.now() > dt(dt.now().year,dt.now().month,dt.now().day,12)):#the number 14 and 12 are the time of working that is from 12 to 2pm between this your choosen website will not work
         print("working hours")
         with open("/etc/hosts","r+") as file:# enter the path of your hosts file- for mac users- /etc/hosts | for windows user-C:\Windows\System32\drivers\etc\hosts
              content=file.read()
              for i in website:
                  if(i in content):
                      pass
                  else:
                      file.write(ip+ " " + i+"\n")


    else:
            with open("/etc/hosts","r+") as file:# enter the path of your hosts file- for mac users- /etc/hosts | for windows user-C:\Windows\System32\drivers\etc\hosts
                    content=file.readlines()
                    file.seek(0)
                    for y in content:
                            if  not any(x in y for x in website):
                                 file.write(y)
                    file.truncate()
            print("fun hours")

    time.sleep(5)
