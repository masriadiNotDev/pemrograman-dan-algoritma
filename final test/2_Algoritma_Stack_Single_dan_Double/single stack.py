
# masriadi sisfo b D0425309

stack = []

def push(item):
    stack.append(item)

def pop():
    if len(stack) == 0:
        return "Stack kosong"
    return stack.pop()

# Contoh penggunaan
push(10)
push(20)
push(30)

print("Isi Stack:", stack)
print("Pop:", pop())
print("Isi Stack setelah Pop:", stack)
