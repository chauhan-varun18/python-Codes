# recursive function

def show(n):
    if (n == 0):  # base case ye decide krta h ki yha pe recursion ruk jana chiye ya nhi / ye jruri hota h recu. k liye
        return
    print(n)  # phela call
    show(n - 1) # 2ra call
    print("END")

show(6)