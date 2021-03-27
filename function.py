def describe_pet(pet_name,animal_type='dog'):#有default实参的形参放在最后，在调用函数不指定实参时使用default实参
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')

def make_shirt(size,words='I love Python'):
    print(f"The size is {size},and the words are {words}")
make_shirt('M','whatever')
make_shirt('M')
make_shirt(words='whatever',size='M')