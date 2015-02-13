# encoding=utf-8

import werobot
import werobot.utils
import werobot.testing
import pointsearch
import bus_search
import monitory
import nearTaxi

robot = werobot.WeRoBot(token='gis')

last={}
ope4={}
ope={}
s='0'

@robot.handler
def mainmenu(message):
    s = last.get(message.source, 'Nothing')
    op = ope.get(message.source, 'Nothing')
    msn='10'
    if message.type == 'text' :
        msn= message.content
    if s=='4' and msn!='0':
        o = ope4.get(message.source, 'Nothing')
        if o=='1':
            ope4[message.source]= 'Nothing'
            return "功能建设中···"
            
        if o=='2':
            ope4[message.source]= 'Nothing'
            return pointsearch.search(message,'停车场')
            
        if o=='3':
            ope4[message.source]= 'Nothing'
            return bus_search.bus(message)
        if o=='4':
            ope4[message.source]= 'Nothing'
            return pointsearch.search(message,'加油站')
        else:  
            ope4[message.source] = message.content
            if message.content == '1':
                return '您好，现在开始交通管制查询\n\n返回主菜单请输入【0】'
                
                
            if message.content == '2':
                return '您好，现在开始停车场查询，首先请通过左边的“+”按钮选择“位置”（请将图标放在您要查询的位置，注意地图可以拖动哦）\n\n返回主菜单请输入【0】'
                
                
            if message.content == '3':
                return '您好，现在开始公交出行查询，请您输入“城市” “起点” “终点”（中间以空格分隔）进行查询，如：福州 西禅寺 宝龙城市广场\n\n返回主菜单请输入【0】'
                
                
            if message.content == '4':
                return '您好，现在开始加油站查询，首先请通过左边的“+”按钮选择“位置”（请将图标放在您要查询的位置，注意地图可以拖动哦）\n\n返回主菜单请输入【0】'
                   
            
            else:
                return '您好，欢迎来到“美丽出行”服务平台，请输入括号中数字使用相应服务：\n输入【1】，查询交通管制\n输入【2】，查询停车场\n输入【3】，查询公交出行\n输入【4】，查询加油站\n输入【0】，返回主菜单'
            
    else:
        op = ope.get(message.source, 'Nothing')
        if op=='1':
            ope[message.source] = '0'
            return monitory.near_geoquery_with_max_distance(message)
        if op=='2':
            ope[message.source] = '0'
            return nearTaxi.near_taxiquery_with_max_distance(message)
        else:
            last[message.source] = message.content
            if last[message.source] == '1':
                ope[message.source] = '1'
                return '您好，现在开始路口监控查询，首先请通过左边的“+”按钮选择“位置”（请将图标放在您要查询的位置，注意地图可以拖动哦）'
                
            if last[message.source] == '2':
                ope[message.source] = '2'
                return '您好，现在开始附近的士查询，首先请通过左边的“+”按钮选择“位置”（请将图标放在您要查询的位置，注意地图可以拖动哦）'
                
                
            if last[message.source] == '3':
                return '您好，感谢您举报违规现象，首先请通过左边的“+”按钮选择“图片”，之后选择拍照或将已经拍好的照片传送给我们，我们将及时处理您的举报'
                
                
            if last[message.source] == '4':
                return '您好，欢迎来到“美丽出行”服务平台，请输入括号中数字使用相应服务：\n输入【1】，查询交通管制\n输入【2】，查询停车场\n输入【3】，查询公交出行\n输入【4】，查询加油站\n输入【0】，返回主菜单'

            
            else:
                return '您好，欢迎来到“美丽出行”服务平台，请输入括号中数字使用相应服务：\n输入【1】，查询路口监控\n输入【2】，查询附近的士\n输入【3】，违规举报\n输入【4】，其他查询'


       

robot.run(host='0.0.0.0',port=8080)



