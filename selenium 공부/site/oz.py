import json

json_data = '''
{
    "server_list": {
        "userid":"kmo9000",
        "title":"\uc870 \uc740\uc18c \ub9ac",
        "ip":"14.6.131.105",
        "port":7700,
        "volume":5890607,
        "pingcnt":8678612,
        "gender":1,
        "pserverd":4   
    }
}
'''

json_obj = json.loads(json_data)

print(json_obj)
print("게시자 : " + json_obj['server_list']['userid'])
print("제목 : " + json_obj['server_list']['title'])