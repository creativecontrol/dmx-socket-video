#!/bin/bash

#startup script for server

#run nodeserver

function nodeStart(){
	/usr/bin/nodejs server.js
}

function pyStart(){
	/usr/bin/python dmxSock.py	
}

cd ~/Show
#sleep 30
nodeStart
#sleep 10
#pyStart &
