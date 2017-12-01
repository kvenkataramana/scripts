##########################

#Purpose : Cleans up the files older than 60 days in client upload folders on  in /ftphome parition
#########################
#!/usr/bin/python
import os, subprocess,datetime,shutil
basedir = "/home/nvenkataramana/ftphome/"
clients = [ client for client in os.listdir(basedir) if os.path.isdir(os.path.join(basedir,client)) and not os.path.islink(os.path.join(basedir,client))]
#clients.remove("lost+found")
#clients.remove("")
"""
You can hardcode clients as well if you need to restrict cleanup to particluar clients 
You need to uncomment below line and list your clients
"""
#clients = ['chp']
print "clients are"
print clients
now = datetime.datetime.now()
days = 60
ydays = 365
def list_contents(folder):
  for root, dirs, files in  os.walk(folder,topdown=False):
    #print "root is ", root
    for dir  in dirs: 
      print os.path.join(root,dir)
    for file in files:
     print os.path.join(root,file)

def listfiledirs(folder):
  for cwd, subdirs, files in  os.walk(folder,topdown=False):
    #print "root is ", root
    for dir  in subdirs: 
      print "files in" + cwd +  " are " + str(files)
    # print os.path.join(root,file)


def find_oldfiles(folder):
 for client in clients:
  for cwd, subdirs, files in  os.walk(os.path.join(folder,client,client,"upload")):
    #print "root is " + cwd + "\n"
    for file in files:
       path = os.path.join(cwd,file)
       if now - datetime.datetime.fromtimestamp(os.path.getmtime(path)) > datetime.timedelta(days):
         print str(path)
         #os.remove(path)
 
def findroot_oldfiles(folder):
 for client in clients:
  for cwd, subdirs, files in  os.walk(os.path.join(folder,client,client)):
    #print "root is " + cwd + "\n"
    for file in files:
       path = os.path.join(cwd,file)
       if now - datetime.datetime.fromtimestamp(os.path.getmtime(path)) > datetime.timedelta(ydays):
         print str(path)
         #os.remove(path)

def find_olddirs():
 for client in clients:
   for root,dirs,files in os.walk(os.path.join(basedir,client,client,"upload"),topdown=False):
      for dir in dirs:
       if (now - datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(root,dir)))) > datetime.timedelta(days):
         print os.path.join(root,dir)
         #shutil.rmtree(os.path.join(root,dir))

def find_emptydirs():
 for client in clients:
   for root,dirs,files in os.walk(os.path.join(basedir,client,client,"upload"),topdown=False):
     for dir in dirs:
      if not os.listdir(os.path.join(root,dir)):
       print  os.path.join(root,dir)
       #os.rmdir(os.path.join(root,dir))
    
   
#print "contents"
#list_contents(basedir)
print "files older than 60 days"
find_oldfiles(basedir)
#print "directories older than 60 days"
#find_olddirs()
#print "Empty Directories"
#find_emptydirs()
#print "Files in each client root directories older than 1 year"
#findroot_oldfiles(basedir)
