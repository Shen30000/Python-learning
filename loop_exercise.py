sandwich_orders = ['a', 'b', 'a', 'c', 'a']
print("sandwich a is sold out.")
finished_sandwiches = []
while sandwich_orders:
    if sandwich_orders[-1] == 'a':
        sandwich_orders.remove('a')  #remove从左到右执行，remove掉一个元素就结束
    else:
        print(f"I made your sandwich {sandwich_orders[-1]}.")
        sandwich = sandwich_orders.pop()
        finished_sandwiches.append(sandwich)
print(finished_sandwiches)