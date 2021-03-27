def make_album(singer,name,num=None):
    if num:
        album={}
        album['artist']=singer
        album['album_name']=name
        album['number']=num
    else:
        album={}
        album['artist']=singer
        album['album_name']=name
    return(album)
while True:#在测试后发现如果在函数内定义无限循环，循环只会执行一次
    singer=input("Singer's name:")
    if singer=='q':
        break
    name=input("Album's name:")
    if name=='q':
        break
    num=input("Song's number:")
    if num=='q':
        break
    print(make_album(singer,name,num))