#!/usr/bin/python

import datetime
from os import environ, mkdir, symlink, path, remove

def mkdirandlink(folder, link):
	#make the current week's directory if it doesn't already exist
	if not path.isdir(folder):
		mkdir(folder)

	#update or create link in home directory
	if path.exists(link):
		remove(link)

	symlink(folder, link)

if __name__ == '__main__':
	#declorations
	linkpath=environ['HOME'] + "/curweek"
	mydir=environ['HOME'] + "/Documents/unix/week"
	firstclassday=datetime.datetime(2012,01,16)
	today=firstclassday.today()

	#current week in semester.
	weeknum=(today-firstclassday).days/7 + 1

	#location of this weeks directory.
	mydir = mydir + str(weeknum) + '/'

	mkdirandlink(mydir, linkpath)
