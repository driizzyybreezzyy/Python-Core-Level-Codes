def func_solve(string):
    ws = string.split()
    switch_ws = []
    
    for w in ws:
        switched_w = ""
        for i in range(0, len(w)-1, 2):
            switched_w += w[i+1] + w[i]
        
        if len(w) % 2 != 0:
            switched_w += w[-1]
        
        switch_ws.append(switched_w)
    
    switch_s = " ".join(switch_ws)
    return switch_s


str = input("Enter :")
soln = func_solve(str)
print(soln)