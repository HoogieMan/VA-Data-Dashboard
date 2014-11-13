# -*- coding: utf-8 -*-
"""
Created on Wed Nov 12 15:55:56 2014

@author: choog_000
"""
## query script to access all 'Average Waiting Time' files from http://cironline.org/use-data-veterans-disability-backlog, pull them down, and store them in a local directory ##

import urllib2

cityFile = open('C:\\Users\\choog_000\\Documents\\Socrata\\VA\\Dashboard\\cities.csv','r')
dataFile = open("C:\\Users\\choog_000\\Documents\\Socrata\\VA\\Dashboard\\waiting_list_data.csv",'w')

#iterate through cities from cityFile and access relevant URL, to pull down and write data to new CSV#
for line in cityFile:
    data = urllib2.urlopen("http://vbl-media.s3.amazonaws.com/data/" + line + "-average-processing-time.csv")
    readData = data.read()
    dataFile.write(readData)
    dataFile.write(',')

#unit test###
data = urllib2.urlopen("http://vbl-media.s3.amazonaws.com/data/" + 'buffalo' + "-average-processing-time.csv")
readData = data.read()
dataFile.write(readData)
    
    
shortList = ['reno', 'anchorage']
dataFileTest = open("C:\\Users\\choog_000\\Documents\\Socrata\\VA\\Dashboard\\waiting_list_data_test.csv",'w')
for item in shortList:
    data = urllib2.urlopen("http://vbl-media.s3.amazonaws.com/data/" + item + "-average-processing-time.csv")
    readData = data.read()
    dataFileTest.write(readData)
    dataFileTest.write(',')