'''
Created on Mar 31, 2011

@author: jlchandr
'''
from _winreg import *
import socket,re

key_name = r"Software\Microsoft\Windows\CurrentVersion\Internet Settings"
name="ProxyEnable"
value_in_office = 1
value_in_home = 0
def toggle_proxy():
    
    registry = ConnectRegistry(None,HKEY_CURRENT_USER)
    key = OpenKey(registry,key_name,0,KEY_QUERY_VALUE)
    "Check if the ProxyEnable Exists"
    value = QueryValueEx(key,name)
#    if value[0] == 1:
    proxy_enabled = value[0] == 1
#        print("Proxy is enabled")
#    else :
#        print("Proxy is disabled")
        
    CloseKey(key)
    
    "Now if proxy is enabled , disable it ,in home network"
    ip  = socket.gethostbyname(socket.gethostname())
    "If IP address starts by 10 then inside office otherwise home"    
    in_office = re.match('^10',ip) 
   
    key = OpenKey(registry,key_name,0,KEY_WRITE)
    if in_office :
        value = value_in_office
    else : 
         value = value_in_home
         
    SetValueEx(key,name,0,REG_DWORD,value)
    CloseKey(key)
    
    
if __name__ == '__main__' :
    toggle_proxy()