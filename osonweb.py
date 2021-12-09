#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")

#print(subprocess.getoutput("sudo "+ cmd))

def Lunch_Cont(cmd):
    return(subprocess.getoutput("sudo docker run -itd --name {} centos".format(cmd)))

cid = Lunch_Cont(cmd)

def Pwd(cid):
    return(subprocess.getoutput('sudo docker exec {} pwd'.format(cid)))


#print("hello")

print('{')
print('\t"Cont_Id": "{}",'.format(cid))
print('\t"PWD": "{}"'.format(Pwd(cid)))
print('}')
