#coding=utf-8
import werobot
import werobot.utils
import werobot.testing
from werobot.reply import TextReply
import urllib
import xml.dom.minidom
import sys
import types
import findcity

#robot = werobot.WeRoBot(token='gis')

reload(sys)
sys.setdefaultencoding( "utf-8" )


#@robot.handler
def search(message,cate):
    resultStr=''
  
    x, y = message.location
    #cate='停车场'
    city=findcity.city(x,y)
    #print city
    url ='http://openapi.aibang.com/search?app_key=d99af897dbf7abd53d1593382de5dcf2&city='+city+'&cate='+cate+'&rc=2&lng='+str(y)+'&lat='+str(x)
    result = urllib.urlopen(url).read()
    #print result
    f = open('search.xml' , 'w')
    f.write(result)
    f.close()

    #xml 解析
    dom1=xml.dom.minidom.parse("search.xml")
    root=dom1.documentElement
    segments={}
    busnode=root.getElementsByTagName('biz')
    i=1
    for buslist in busnode:
        resultStr=resultStr+ '\n\n地点'+str(i)
        i=i+1
        
        for segslist in  buslist.childNodes:
          
            #if segslist.nodeType ==1:
            if segslist.nodeName=="name":
                resultStr=resultStr+ '\n名称:'
                for node in segslist.childNodes:
                    resultStr=resultStr+ str(node.data)
                
            else:
                if segslist.nodeName=="addr":
                    resultStr=resultStr+ '\n地址：'
                    for node in segslist.childNodes:
                        resultStr=resultStr+ str(node.data)
                    
                else:
                    if segslist.nodeName=="dist":
                        resultStr=resultStr+ '\n距离：约'
                        for node in segslist.childNodes:
                            resultStr=resultStr+ str(node.data)
                        resultStr=resultStr+ '千米'
            
    #print resultStr
    #reply = TextReply(message=message, content=str(resultStr))
    try:
        #print resultStr
        return resultStr
    except:
        #print '格式错误'
        return '您输入的格式不正确'                


#robot.run(host='0.0.0.0',port=80)
