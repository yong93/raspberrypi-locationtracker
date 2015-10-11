import sys,time,geolocation,publisher
from subprocess import call

SleepTime = 10 # seconds
_lat = 0.00
_lon = 0.00

def maintain():
    global _lat
    global _lon
    x=y
    (lat,lon,accuracy) = geolocation.getLocation()
    if(lat != _lat or lon !=_lon):
        data = str(lat) + "," + str(lon) + "," + str(accuracy)
        print "publishing ", data
        publisher.publishtoInternet(data)
        _lat = lat
        _lon = lon
    else:
        print "no change in coordinates"

print "program begins"
while True:
    try:
        maintain()
    except Exception as inst:
        print type(inst), ' exception captured'
        print inst
        sys.stdout.flush()
        #file = open('/tmp/loctracker.error.log','a')
        #file.write('exception occured, trying to reboot')
        #file.close()
        #call(["sudo","reboot"])
    #break
    for i in range(0,SleepTime):
        sys.stdout.write("\restarting in %d seconds " % (SleepTime-i))
        sys.stdout.flush()
        time.sleep(1)

       
