import time
t = time.strftime('%H:%M:%S')
print(t)
hour = int(time.strftime('%H'))
if(hour>=0 and hour<12):
    print("GOOD MORNING DEAR")
elif(hour>=12 and hour<17):
    print("GOOD EVENING DEAR")
elif(hour>=17 and hour<24):
    print("GOOD NIGHT DEAR")
