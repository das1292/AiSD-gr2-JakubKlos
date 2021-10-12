def foo(text):
    text = text.lower().replace(" ", "")
    x = len(text)
    for i in range(x-1):
        if text[i] != text[x-1-i]:
            return False
    return True
x = input()
print("1" if(foo(x)) else "0")

