from pathlib import Path
import json
print("=============================" )
#应用json 字符串读取 loads()
pass
#应用json 写入dump  类型取决于写进去时
data=[11,22,33,44,55,66]
data0={'laoba':100,'laowu':200}
all_data={'list':data,"dict":data0}
with open('data.json','w',encoding='UTF-8') as f:
    json.dump(all_data,f,ensure_ascii=False)#应用json 读取
with open('data.json','r',encoding='UTF-8') as f:
    data1=json.load(f)
print(data1,type(data1))
#dumps 将python的数据转为json格式 输出类型为str
info={
    'name':'张三',
    'age':19,
    'address':'北京',
    'phone':190874874
}
print(info,type(info))
info_json=json.dumps(info,ensure_ascii=False)
print(info_json,type(info_json))

