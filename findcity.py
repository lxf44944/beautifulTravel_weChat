#coding=utf-8
import werobot
import werobot.utils
import werobot.testing
from werobot.reply import TextReply
import urllib
import xml.dom.minidom
import sys
import types


reload(sys)
sys.setdefaultencoding( "utf-8" )

def city(x,y):
    
    url ='https://maps.googleapis.com/maps/api/geocode/xml?latlng='+str(x)+','+str(y)+'&sensor=false&language=zh-CN'
    
    result = urllib.urlopen(url).read()
    
    f = open('findcity.xml' , 'w')
    f.write(result)
    f.close()

    #xml 解析
    dom1=xml.dom.minidom.parse("findcity.xml")
    root=dom1.documentElement
   
    busnode=root.getElementsByTagName('address_component')
    typeis=''
    for buslist in busnode:    
        for segslist in  buslist.childNodes:
            if segslist.nodeName=="long_name":
                for node in segslist.childNodes:
                    longname= str(node.data)
                    
                
            if segslist.nodeName=="type":
                for node in segslist.childNodes:
                    typeis= str(node.data)
            if typeis=='locality':
                return longname
                
                
