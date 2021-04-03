def show_messages(msgs):
    for msg in msgs:
        print(msg)

def send_messages(msgs,sent_messages):
    while msgs:
        print(msgs[0])
        sent_messages.append(msgs.pop(0))
msg=["a","b","c","d"]
sent=[]
show_messages(msg)
send_messages(msg[:],sent)
print(msg)
print(sent)