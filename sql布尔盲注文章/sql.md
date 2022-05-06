![image-20220505125455320](sql.assets/image-20220505125455320.png)

抓包测试注入点

![image-20220505125218371](sql.assets/image-20220505125218371.png)

![image-20220505125313678](sql.assets/image-20220505125313678.png)

根据两次回显值的不同判断存在布尔盲注

爆数据库名长度为7

![image-20220505011831954](sql.assets/image-20220505011831954.png)

爆数据库名为 message

![image-20220505011953939](sql.assets/image-20220505011953939.png)

猜解表数 为3

![image-20220505124954601](sql.assets/image-20220505124954601.png)

爆表明长度 分别为 4 4 8

![image-20220505012008219](sql.assets/image-20220505012008219.png)

爆表名 flag suer username 猜测 flag 在表名为flag的表中

![image-20220505010613032](sql.assets/image-20220505010613032.png)

猜解字段数 为2

![image-20220505010921882](sql.assets/image-20220505010921882.png)

爆各个字段个数 分别为 4 2

![image-20220505011446509](sql.assets/image-20220505011446509.png)

爆字段名 分别为flag  id 

![image-20220505011538397](sql.assets/image-20220505011538397.png)

爆flag

![image-20220505011652626](sql.assets/image-20220505011652626.png)