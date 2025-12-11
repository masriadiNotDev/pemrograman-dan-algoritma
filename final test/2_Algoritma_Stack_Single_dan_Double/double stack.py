
# masriadi sisfo b D0425309

# Dua stack dalam satu list
max_size = 10
array = [None] * max_size

top1 = -1
top2 = max_size

def push1(value):
    global top1, top2
    if top1 + 1 == top2:
        print("Stack penuh")
    else:
        top1 += 1
        array[top1] = value

def push2(value):
    global top1, top2
    if top1 + 1 == top2:
        print("Stack penuh")
    else:
        top2 -= 1
        array[top2] = value

def pop1():
    global top1
    if top1 == -1:
        return "Stack 1 kosong"
    value = array[top1]
    top1 -= 1
    return value

def pop2():
    global top2
    if top2 == max_size:
        return "Stack 2 kosong"
    value = array[top2]
    top2 += 1
    return value

# Contoh
push1(10)
push1(20)
push2(30)
push2(40)

print("Array:", array)
print("Pop1:", pop1())
print("Pop2:", pop2())
