bicycles=['trek','cannondale','redline','specialized']
print(bicycles)
print(bicycles[0].title())#索引从0开始
print(bicycles[-1])#Python里最后一个索引为-1，倒数第二个为-2，依此类推,但列表为空时不能这样
print(f"My first bicycle was a {bicycles[0].title()}.")
bicycles.append('append')#在列表最后添加，会改变列表
print(bicycles)
bicycles.insert(0,'insert')#在位置0插入，后面的全部后移
print(bicycles)
del bicycles[1]#删除操作
print(bicycles)
popped_bicycles=bicycles.pop()#把列表最后一个赋给popped_bicycles然后删除,.pop()中可写数字，此时对数字索引pop
print(bicycles)
print(popped_bicycles)
bicycles.remove('insert')#找到‘insert’并删除
print(bicycles)
bicycles.sort()#sort会改变列表内顺序，用.sorted()就不会，使用时赋给别的列表就好了
print(bicycles)
bicycles.sort(reverse=True)#.sorted()也可以这样
print(bicycles)
print(len(bicycles))
for bicycle in bicycles:#冒号不要漏
    print(bicycle)
print(bicycle)
for value in range(1,5):#注意不含5，range一般用在for循环中，转换成列表···
    print(value)
numbers=list(range(2,11,2))#步长2
print(numbers)
squres=[]
for value in range(1,11):
    squres.append(value**2)
print(squres)
print(f"{min(squres)}\n{max(squres)}\n{sum(squres)}")
squres1=[value1**2 for value1 in range(1,11)]
print(squres1)
players=['charles','martina','michal','florance','ali']
print(players[0:3])#注意这里指索引为0~2的，若[,3]指从开头到索引为2，[0,]和[,]类似
players1=players
players2=players[:]#注意这两者不同，上面复制的是指针，下面复制的是列表元素