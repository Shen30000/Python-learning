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
test_dic={
    'p1':1,
    'p2':1,
    'p3':3,
}
for value in set(test_dic.values()):#set用于去掉重复元素
    print(value)
favorite_languages={
    'jen':['python','ruby'],
    'edward':['ruby','go'],
    'phil':['python','haskell'],
    'rita':['c',]
}
for name,languages in favorite_languages.items():
    if len(languages)==1:
        print(f"\n{name.title()}'s favorite language is:")
    else:
        print(f"\n{name.title()}'s favorite language are:")
    for language in languages:
        print(f"\t{language.title()}")