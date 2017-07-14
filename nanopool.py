# written by futurehelp: circa 2017

import urllib2
import json
import datetime
import logging
from apscheduler.schedulers.blocking import BlockingScheduler

logging.basicConfig()

#change address to your wallet address
timeData = datetime.datetime.time(datetime.datetime.now())
f = urllib2.urlopen('http://sxswdocumentary.com/nanopool.php?address=0xed13acce4d09d2af47eece5f0365fb1a80206353')
json_string = f.read()
parsed_json = json.loads(json_string)
balance = parsed_json['data']['balance']
print "Current balance %s : %s" % (balance, timeData)
fileHandle = open('nanopool.txt', 'a')
fileHandle.write(repr(balance) + '\n')
fileHandle.close()
f.close()

sched = BlockingScheduler()

#@sched.scheduled_job('interval', seconds=3600)
def timed_job():
	f = urllib2.urlopen('http://sxswdocumentary.com/nanopool.php?address=0xed13acce4d09d2af47eece5f0365fb1a80206353')
	json_string = f.read()
	parsed_json = json.loads(json_string)
	balance = parsed_json['data']['balance']
	timeData = datetime.datetime.time(datetime.datetime.now())
	print "Current balance %s : %s" % (balance, timeData)
	fileHandle = open('nanopool.txt', 'a')
	fileHandle.write(repr(balance) + '\n')
	fileHandle.close()
	f.close()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=10)
def scheduled_job():
    print('This job is run every weekday at 10am.')

sched.add_job(timed_job, 'interval', hours=1)
sched.start()
