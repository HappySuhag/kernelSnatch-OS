#!/usr/bin/python3

import cgi
import subprocess
import time


#print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
#i = f.getvalue("y")

def Run_cmd(cmd,i):
    return (subprocess.getoutput("sudo docker exec {} {}".format(i,cmd)))

#print('{\n')
#print('"O/p" : "{}"'.format(subprocess.getoutput("sudo docker exec {} {}".format(i,cmd))))
#print('\n}')

def run(cmd):
    subprocess.getoutput("sudo {}".format(cmd))
    time.sleep(500)
    subprocess.getoutput("sudo clear")

print('{\n')
print('"O/p" : "{}"'.format(run(cmd)))
print('\n}')
