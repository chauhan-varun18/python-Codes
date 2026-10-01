p1 = 'make a lot of money'
p2 = "buy now"
p3 = "follow now " 
p4 = "click this"

message = input("enter your cmnt:")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this cmnt is spam")

else:
    print("this cmnt is not spam")