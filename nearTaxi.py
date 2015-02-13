#coding=utf-8
from pymongo import Connection
from bson.son import SON
import subprocess
import werobot
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def near_taxiquery_with_max_distance(message):
    lon,lat=message.location
    max_distance=1/111.12
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
    mconnection =  Connection('127.0.0.1',27017)
    db = mconnection["dbname"]
    transactions = db["dbname"]
    """perform the search.  all should work now."""
    mysearchresult=transactions.find(gq)
    i=0
    for u in mysearchresult:
        i=i+1
        #print u['addr_point']
    return '您附近一千米范围内有'+str(i)+'辆的士，请您根据需要选择出行方式，希望给您的出行带来便利！'


    
    
    


    
