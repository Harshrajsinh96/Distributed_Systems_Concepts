from __future__ import print_function
from platform import system as system_name #for selecting system
import re # for using Regular Expression in string search
import subprocess

hosts = {"23.23.255.255":"us-east-1", "13.58.0.253":"us-east-2", "13.52.0.2":"us-west-1", "34.208.63.251":"us-west-2", 
"52.61.0.254":"us-gov-west-1", "35.182.0.251":"ca-central-1", "18.231.0.252":"sa-east-1", "34.240.0.253":"eu-west-1", 
"18.194.0.252":"eu-central-1", "35.176.0.252":"eu-west-2", "35.180.0.253":"eu-west-3", "13.112.63.251":"ap-northeast-1", 
"13.124.63.251":"ap-northeast-2", "13.228.0.251":"ap-southeast-1", "13.54.63.252":"ap-southeast-2", "13.126.0.252":"ap-south-1", 
"52.80.5.207":"cn-north-1", "52.83.214.0":"cn-northwest-1"}
result = {}

if system_name().lower()=="windows" :
    platform = "-n" # For Windows
else :
    platform = "-c" # For Linux, MacOS

for i in hosts.keys():
    ping = subprocess.Popen(

        ["ping", platform, "3", i],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    out, error = ping.communicate()
    
    if system_name().lower()=="windows" :
    	avrg = re.search(r'Average = (\d+)', out.decode(), re.MULTILINE).group(1) #output STYLE differs in windows and linux/MacOS hence IF/ELSE && decode() for converting byte data to string so that RE can search
    else:
    	data = out.split('/'.encode()) #enode() for converting string to byte
    	avrg = data[4]
    result[float(avrg)] = i

a = 1
x = sorted(result.keys())

for i in x:
    print(str(a) + ". " + str(hosts[result[i]]) + " [" + str(result[i]) + "] - " + str(i) + "ms")
    a = a + 1