cars=['audi','bmw','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    elif 1==2:#此处说明if-elif-else结构,elif和else都不是必要的
        print("This is a test.")
    else:
        print(car.title())
    #if还有其他写法，如 if age1>=10 and age2<=20: 或
    # if (age1>=10) and (age2<=20):
    # 或 if (age1>=10) or (age2<=20):
    # 或 if 'bmw' in cars:
    # 或 if 'bmw' not in cars: