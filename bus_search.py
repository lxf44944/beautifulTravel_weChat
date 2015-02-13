#coding=utf-8
import werobot
import werobot.utils
import werobot.testing
from werobot.reply import TextReply
import urllib
import xml.dom.minidom
import sys
import types

##robot = werobot.WeRoBot(token='gis')

reload(sys)
sys.setdefaultencoding( "utf-8" )


##@robot.handler
def bus(message):
    resultStr=''
    s=message.content.encode('utf-8')
    
    slist=s.split(' ')
    
    city=slist[0]
    start_addr=slist[1]
    end_addr=slist[2]
    url ='http://openapi.aibang.com/bus/transfer?app_key=d99af897dbf7abd53d1593382de5dcf2&city='+city+'&start_addr='+start_addr+'&end_addr='+end_addr 
    result = urllib.urlopen(url).read()
    f = open('foo.xml' , 'w')
    f.write(result)
    f.close()

    #xml 解析
    dom1=xml.dom.minidom.parse("foo.xml")
    root=dom1.documentElement
    segments={}
    busnode=root.getElementsByTagName('bus')
    i=1
    for buslist in busnode:
        resultStr=resultStr+ '\n\n方案'+str(i)
        i=i+1
        
        for segslist in  buslist.childNodes:
          
            #if segslist.nodeType ==1:
            if segslist.nodeName=="time":
                resultStr=resultStr+ '\n需用时间：约'
                for node in segslist.childNodes:
                    resultStr=resultStr+ str(node.data)
                resultStr=resultStr+ '分钟'
            else:
                if segslist.nodeName=="dist":
                    resultStr=resultStr+ '\n总距离：约'
                    for node in segslist.childNodes:
                        resultStr=resultStr+ str(node.data)
                    resultStr=resultStr+ '米'
                else:
                    if segslist.nodeName=="foot_dist":
                        resultStr=resultStr+ '\n需步行距离：约'
                        for node in segslist.childNodes:
                            resultStr=resultStr+ str(node.data)
                        resultStr=resultStr+ '米'
            for seglist in  segslist.childNodes:   
                for nodelist in  seglist.childNodes:
                    if nodelist.nodeType ==1:
                        if nodelist.nodeName=='foot_dist':
                            resultStr=resultStr+ '\n步行约'
                            for node in nodelist.childNodes:
                                resultStr=resultStr+ str(node.data)
                            resultStr=resultStr+ '米'
                        if nodelist.nodeName=='start_stat':
                            resultStr=resultStr+ '\n从'
                            for node in nodelist.childNodes:
                                resultStr=resultStr+ str(node.data)
                        if nodelist.nodeName=='line_name':
                            resultStr=resultStr+ '\n乘坐'
                            for node in nodelist.childNodes:
                                resultStr=resultStr+ str(node.data)
                        if nodelist.nodeName=='end_stat':
                            resultStr=resultStr+ '\n到达'
                            for node in nodelist.childNodes:
                                resultStr=resultStr+ str(node.data)
    #print resultStr
    #reply = TextReply(message=message, content=str(resultStr))
    try:
        print resultStr
        return resultStr
    except:
        print '格式错误'
        return '您输入的格式不正确'                


#robot.run(host='0.0.0.0',port=80)
