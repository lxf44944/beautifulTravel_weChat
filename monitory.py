#coding=utf-8
from pymongo import Connection
from bson.son import SON
import subprocess
import werobot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def near_geoquery_with_max_distance(message):
    lon,lat=message.location
    max_distance=5/111.12
    """ Build the $near dict with your lat/lon values """
    near_dict = {'$near':[float(lat), float(lon)]}
    """ build the maxdistance dict with your max distance value """
    max_dist_dict={'$maxDistance': float(max_distance)}
    """ Create a SON object from our near_dict. ORDER IS IMPORTANT. THIS MUST BE FIRST! """
    q=SON(near_dict)
    """ Now add the 2nd item (max_dist_dict) to the ordered SON dict """
    q.update(max_dist_dict)
    """ Now put all of the above into a dict with using the key for your geospatial data """
    gq={'addr_point': q}
    """ Connect to the DB, use you local settings """
    mconnection =  Connection('localhost', 27017)
    db = mconnection["mlcx"]
    transactions = db["addresses"]
    """perform the search.  all should work now."""
    mysearchresult=transactions.find(gq)
    #print mysearchresult
    url= str(mysearchresult[0]["addr_url"])
    name= str(mysearchresult[0]["addr_name"]).encode('utf-8')
    print url
    dir='/var/www/html/weixin'
    p = subprocess.Popen(['mplayer','-prefer-ipv4','-fps','25','-frames','4','-vf','pp=fd/ffmpegdeint', '-nosound', '-vo', 'jpeg:outdir='+dir,url],stdout=subprocess.PIPE,shell=False)   
    #print p.stdout.readlines()
    return [
        [
            "实时路况",
            "美丽出行",
            "http://127.0.0.1/weixin/00000004.jpg",
            "http://127.0.0.1/weixin/00000004.jpg"
        ],
        [
            name,
            "http://127.0.0.1/weixin/00000004.jpg",
            "http://127.0.0.1/weixin/00000004.jpg",
            "http://127.0.0.1/weixin/00000004.jpg"
        ]
    ]


    
