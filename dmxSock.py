import sys
import json
import subprocess
import pwd
import os
from ola.ClientWrapper import ClientWrapper
from socketIO_client import SocketIO

#global vars
video = ""
universe = 1 
chan = 1
vids = [""]*20
hold = -1		#keeps from refiring when a movie is playing

#Get data from the config.json file
def config():
	global universe
	global chan
	global vids
	#grab settings from json file
	conf = json.loads(open('config.json').read())
	#dmx universe
	universe = conf['universe']
	#dmx channel
	chan = conf['channel']-1 #subtract 1 for index 
	#video file names
	for n in range(20):
		name = 'vid'+str(n+1)
		vids[n] = conf[name]

def rangeCheck(data):
	global hold
	global video
	global vids
	slot = int(data[chan]/2.55) #get percentage
	video = ""
	if(slot!=hold):	#if a different value comes in
		#print "incoming channel: "+str(data[chan])
		#print "slot: "+str(slot)
		hold = slot	
		if(slot==0):
			video = "Black"				
		elif(slot%5==0):	# if number is divisible by 5 play a video
			video = vids[(slot-5)/5]
		else:
			video = 'x'
		#print("video: "+video)

def NewData(data):
	global video
	rangeCheck(data)
	if(video and video != 'x'):
		print("video: "+video)
		with SocketIO('localhost', 8000) as socketIO:
			socketIO.emit('dmx', {'vid':video})
			socketIO.wait(seconds=1)
  #print data[0]

def openChrome():
	pw_record = pwd.getpwnam('media')
	user_name = pw_record.pw_name
	user_home_dir = pw_record.pw_dir
	user_uid = pw_record.pw_uid
	user_gid = pw_record.pw_gid
	subprocess.Popen('google-chrome --kiosk index.html',preexec_fn=demote(user_uid, user_gid),shell=True)	

def demote(user_uid, user_gid):
    def result():
        #report_ids('starting demotion')
        os.setgid(user_gid)
        os.setuid(user_uid)
        #report_ids('finished demotion')
    return result

config()
openChrome()
with SocketIO('localhost', 8000) as socketIO:
	socketIO.emit('howdy', {'msg':"dmx connected"})
	socketIO.wait(seconds=1)
wrapper = ClientWrapper()
client = wrapper.Client()
client.RegisterUniverse(universe, client.REGISTER, NewData)
#print "running"
wrapper.Run()
