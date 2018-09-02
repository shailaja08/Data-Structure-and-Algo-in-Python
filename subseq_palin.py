from collections import Counter
def pali(s,t):
    indices = []
        # trev = t.reverse()
    j = 0
    m = len(s)
    n = len(t)
    for i in range(m):
        try:
            j = t.index(s[i])

        except:
            return False
    return True
        

s = "aec"
t = "ahbgdc"
print(pali(s,t))
