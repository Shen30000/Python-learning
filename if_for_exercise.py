users = ['admin', 'michal', 'jessie', 'eric', 'john']
guest = input()
if guest == 'admin':
    print("Hello admin!")
elif (guest == 'michal') or (guest == 'jessie') or (guest == 'eric') or (guest == 'john'):
    print("Hello my friend!")
else:
    print("We need to find some users.")
    del users[:]