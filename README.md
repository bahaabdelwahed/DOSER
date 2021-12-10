# DOSER
EDUCATION PURPOSE ONLY  !!!!!!!!!!!!!<br>
Doser is basically an Denial of Service attack that affects websites and local machines

  [+] DDOS Websites ,Detect And BYPASS CLOUDFLARE <br>
  [+] RUN SYN FLOOD AND PING OF DEATH ATTACK<br>
  [+] ARP Spoof Target in the local Network<br>
  
  # How to install and run
      
      * git clone https://github.com/bahaabdelwahed/DOSER/<br>
      * Install used library (pip3 install <library_name>)<br>
      * cd DOSER<br>
      * chmod +x doser.py<br>
  # USAGE : 
  
       python3 doser.py -u https://example.com <br>
       run this command against website doser tell you if the site use cloudflare and start attack with <br>
       
       python3  doser.py -syn 127.0.0.1 -p 21 <br>
       run syn flood attack against 127.0.0.1:21 this option use scapy to send multiple request in multiple thread<br>
       
       doser.py -pod 127.0.0.1 <br>
       Multiple request  against ICMP protocole<br>
       
       doser.py -arp <br>
       Run GUI console that ask for local ip adress to start arp spoof<br>
       
   
   
       WANT TO USE PROXY Make sure to update this :
       proxies ={
            'https': 'https://140.227.69.170:6000',
           'https': 'https://3.12.95.129:80',
           'https': 'https://167.99.174.59:80',
           'https':'https://92.204.251.170:1080',
           'https':'https://186.225.45.13:80',
           'https':'https://140.82.5.38:80',
           'https':'https://188.126.90.10:8888',
           'https':'https://140.82.5.38:1080',
               }
       and to change proxies=False in ligne 71 to proxies=proxies

   
