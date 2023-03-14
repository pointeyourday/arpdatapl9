


# def funkcja(str, a):
#     return print(txt[:-1])
#
#
# def funkcja(HELLO, 3)

def reverse_idx(text, index):
    if 0 <= index <= (len(text) -1):
        return (-(len(text) - index))    # lub index - len(text)
    else:
        return "error"

print(reverse_idx("HELLO", 0))
print(reverse_idx("HELLO", 4))
print(reverse_idx("lalal lalalla lallalala lala", 90))

