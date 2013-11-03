#!/bin/bash

#startup script for server

#run nodeserver

function nodeStart(){
	/usr/bin/nodejs server.js
}

function pyStart(){
	sed -i 's/"exit_type": "Crashed"/"exit_type": "None"/' ~/.config/google-chrome/Default/Preferences 
	sed -i 's/"exited_cleanly": false/"exited_cleanly": true/' ~/.config/google-chrome/Default/Preferences 

	/usr/bin/python dmxSock.py	
}

cd ~/Show
#sleep 30
nodeStart &
sleep 10
pyStart &
sleep 10
xdotool mousemove 50 50
