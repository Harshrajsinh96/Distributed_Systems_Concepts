import requests, time
import sys
import asyncio 

def sync_fun(int):
	r = requests.get('https://requestb.in/ze1ktmze', data={"ts":time.time()})
	print(r.status_code,r.content, "Process : %i"%int, "Started")
	print(r.status_code,r.content, "Process : %i"%int, "Ended")

async def async_fun(int):
	r = requests.get('https://requestb.in/ze1ktmze', data={"ts":time.time()})
	print(r.status_code,r.content, "Process : %i"%int, "Started")
	await asyncio.sleep(2)
	print(r.status_code,r.content, "Process : %i"%int, "Ended")

def invalid_input():
		print("Enter in the form of : python3 filename.py sync 3")

if (len(sys.argv) == 3 and sys.argv[1]=='async' and sys.argv[2].isdigit()):
		print(" ---Asynchronous Call--- ")
		loop = asyncio.get_event_loop()
		j=1
		while j<=int(sys.argv[2]):
			lst=[]
			lst.append(asyncio.ensure_future(async_fun(j)))
			j+=1 
		loop.run_until_complete(asyncio.wait(lst))
		loop.close()
	
elif (len(sys.argv) == 3 and sys.argv[1]=='sync' and sys.argv[2].isdigit()):
		print(" ---Synchronous Call--- ")
		i=1
		while i<=int(sys.argv[2]):
			sync_fun(i)
			i+=1
else:
	invalid_input()