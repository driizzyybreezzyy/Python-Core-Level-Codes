def rev_string_func(string):
    words = string.split() 
    rev_ws = [] 

    for i in words: 
        rev_w = i[::-1] 
        rev_ws.append(rev_w)
    rev_str = ' '.join(rev_ws)
    return rev_str
str1 = input("Enter : ")
rev_str = rev_string_func(str1)
print(rev_str)