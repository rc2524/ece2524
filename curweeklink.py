#!/usr/bin/python

import datetime
from os import environ, mkdir, symlink, path, remove

#declorations
linkpath=environ['HOME'] + "/curweek"
mydir=environ['HOME'] + "/Documents/unix/week"
firstclassday=datetime.datetime(2012,01,16)
today=firstclassday.today()

#current week in semester.
weeknum=(today-firstclassday).days/7 + 1

#location of this weeks directory.
mydir = mydir + str(weeknum) + '/'

#make the current week's directory if it doesn't already exist
if not path.isdir(mydir):
	mkdir(mydir)

#update or create link in home directory
if path.exists(linkpath):
	remove(linkpath)

symlink(mydir, linkpath)

