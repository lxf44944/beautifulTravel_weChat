====================================
BeautifulTravel_WeChat
====================================
这是一个在linux下执行的“美丽出行”微信公众平台服务端Python程序。

使用框架
========
微信机器人：https://github.com/whtsky/WeRoBot:

程序原理
========
在微信公众平台申请为开发者模式，将服务器ip绑定后，在服务器上部署项目。本程序中用到了mongodb，其中存有车辆位置信息，并实时更新，代码如下：

    #!/usr/bin/env python  
    #coding=utf-8  
    import socket
    import SocketServer
    import thread
    import time
    import datetime
    from time import ctime  
    from pymongo import Connection #导入模块
    con = Connection('127.0.0.1',27017)#此处ip应该为数据来源地址
    db = con.rtfcd
    
    postData = []
    offset_dict={}
    
    def rcvData(a,b):
    	address = ('0.0.0.0', 8787)
    	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    	s.bind(address)
    
    	while True:
    		data, addr = s.recvfrom(2048)
    		if not data:
    			print "client has exist"
    			break
    		dataArr = data.strip().split('\n')
    		for line in dataArr:
    			lineArr = line.strip().split(',')
    			msgid,length,mdid,areaid,lng,lat,speed,direct,status,year,month,day,hour,minute,second,carType = lineArr
    			timeStr = str(datetime.datetime(int(year), int(month), int(day), int(hour),int(minute),int(second)))
    			iTime = float(time.strftime('%S',time.localtime(time.time())))
    			db.rtfcd.update({"mid":mdid},{"mid":mdid,"aid":areaid,"addr_point":[float(lng),float(lat)],"spd":speed,"dir":direct,"sta":status,"gt":datetime.datetime(int(year), int(month), int(day), int(hour),int(minute),int(second)),"ct":carType},True);
    	s.close()
    	
    
    rcvData(1,1)

摄像头位置与链接已存在于数据库中，因涉及数据隐私，此处不提供摄像头与车辆的数据信息，请依据格式自行模拟


程序入口
========
menu.py是主程序，执行该文件即可
