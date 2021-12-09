#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
i = f.getvalue("y")
pwd = f.getvalue("z")

#print(subprocess.getoutput("sudo "+ cmd))

def Lunch_Cont(cmd):
    return(subprocess.run("sudo docker run -itd --name {} centos".format(cmd)))

def Command_in_docker(i,cmd,pwd):
    return(subprocess.getoutput('sudo docker exec {} bash -c "cd {} ; {}"'.format(i,pwd,cmd)))
print(Command_in_docker(i,cmd,pwd))
