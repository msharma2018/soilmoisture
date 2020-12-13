import RPi.GPIO as GPIO
import time
from datetime import datetime
import MySQLdb
channel = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
def callback(channel):
    if GPIO.input(channel):
        print("Water detected")
	dateTimeValue = datetime.now()
	print(dateTimeValue)
	db = MySQLdb.connect("us-cdbr-east-02.cleardb.com","b1abe9ea04ccbe","808435a1","heroku_47d4dcb9ec5878d" )
	cursor = db.cursor()
	sql = """INSERT INTO moisture(dateAdded,
		 moistureDetected,plantType)
		 VALUES (%s,%s,%s)"""
	try:
	   cursor.execute(sql,(dateTimeValue, 'Yes','Cactus'))
	   db.commit()
	except Exception, e:
	   db.rollback()
	   print(str(e))
	db.close()
	print("Connection Closed")
    else:
        print("No Water ")
        
GPIO.add_event_detect(channel,GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(channel,callback)

while True:
    time.sleep(1)
            

