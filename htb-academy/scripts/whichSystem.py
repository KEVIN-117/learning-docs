#!/usr/bin/python3
#coding: utf-8

import re, sys, subprocess
from termcolor import colored

# python3 whichSystem.py 10.10.10.188

if len(sys.argv) != 2:
    print("\n[!] Uso: python3 " + sys.argv[0] + " <IP>\n")
    sys.exit(1)
def get_ttl(ip_address):
    proc = subprocess.Popen(["/usr/bin/ping -c 1 %s" % ip_address, ""], stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    out = out.split()
    out = out[12].decode('utf-8')

    ttl_value = re.findall(r"\d{1,3}", out)[0]

    return ttl_value

def get_os(ttl):
    ttl = int(ttl)
    if ttl >= 0 and ttl <= 64:
        return " Linux"
    elif ttl >= 65 and ttl <= 128:
        return " Windows"
    else:
        return " Not Found"

if __name__ == '__main__':
    ip_address = sys.argv[1]

    ttl = get_ttl(ip_address)

    os_name = colored(get_os(ttl), 'red', attrs=['bold'])

    print(colored("\n[+] %s (TTL -> %s): %s\n" % (ip_address, ttl, os_name), 'green', attrs=['bold']))