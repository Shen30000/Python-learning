aa={'name':'aa','age':'11','city':'ny'}
print(aa['name'])
print(aa['age'])
print(aa['city'])
favorite_num={}
favorite_num['p1']='this is p1'
favorite_num['p2']='this is p2'
favorite_num['p3']='this is p3'
for key,value in favorite_num.items():#items：键值对  keys：键  value：值
    print(f"{key}:{value}")