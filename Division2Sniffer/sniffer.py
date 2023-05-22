from scapy.all import *
import requests
import json

detected_agents = []

banner = """                                     
    ████████▄   ▄█   ▄█    █▄   ▄█     ▄████████  ▄█   ▄██████▄  ███▄▄▄▄            
    ███   ▀███ ███  ███    ███ ███    ███    ███ ███  ███    ███ ███▀▀▀██▄          
    ███    ███ ███▌ ███    ███ ███▌   ███    █▀  ███▌ ███    ███ ███   ███          
    ███    ███ ███▌ ███    ███ ███▌   ███        ███▌ ███    ███ ███   ███          
    ███    ███ ███▌ ███    ███ ███▌ ▀███████████ ███▌ ███    ███ ███   ███          
    ███    ███ ███  ███    ███ ███           ███ ███  ███    ███ ███   ███          
    ███   ▄███ ███  ███    ███ ███     ▄█    ███ ███  ███    ███ ███   ███          
    ████████▀  █▀    ▀██████▀  █▀    ▄████████▀  █▀    ▀██████▀   ▀█   █▀      
   ▄████████ ███▄▄▄▄    ▄█     ▄████████    ▄████████    ▄████████    ▄████████ 
  ███    ███ ███▀▀▀██▄ ███    ███    ███   ███    ███   ███    ███   ███    ███ 
  ███    █▀  ███   ███ ███▌   ███    █▀    ███    █▀    ███    █▀    ███    ███ 
  ███        ███   ███ ███▌  ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄      ▄███▄▄▄▄██▀ 
▀███████████ ███   ███ ███▌ ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
         ███ ███   ███ ███    ███          ███          ███    █▄  ▀███████████ 
   ▄█    ███ ███   ███ ███    ███          ███          ███    ███   ███    ███ 
 ▄████████▀   ▀█   █▀  █▀     ███          ███          ██████████   ███    ███ 
                                                                     ███    ███ 
        [ Hmm do you smell that? The smell of that loud VOIP pack? ]  
         [ If the bugs are not enough, now you can get DDoS'd Too ]
                [ D e v e l o p e d - b y - @ E x C r i m ]
                    [ B E - G A Y - D O - C R I M E ]

"""

def get_agent_ip_info(IP):
    req = requests.get('http://ip-api.com/json/' + IP)
    json_data = json.loads(req.content)
    print("[+] Agent Country: " + json_data["country"])
    print("[+] Agent Region: " + json_data["regionName"])
    print("[+] Agent City: " + json_data["city"])
    print("[+] Agent ISP: " + json_data["isp"])
    print("")

def packet_callback(packet):
    if Raw in packet:
        if b'\xca\xfe\xbe\xef' in packet[Raw].load:
            if '192' not in packet[IP].src:
                if packet[IP].src not in detected_agents:
                    detected_agents.append(packet[IP].src)
                    print("[!] New agent detected: " + packet[IP].src)
                    get_agent_ip_info(packet[IP].src)

print(banner)
sniff(prn=packet_callback)