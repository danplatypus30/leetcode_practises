class Solution: 
    def addBinary(self, a: str, b: str) -> str: 
        c = list(a) 
        d = list(b) 
        ca = 0 
        re = [] 
        while c and d: 
            e = c.pop() 
            f = d.pop() 
            if e == "1" and f == "1" and ca == 1: 
                re.insert(0,"1") 
            elif e == "1" and f == "1": 
                re.insert(0,"0") 
                ca = 1 
            elif (e == "1" or f == "1") and ca == 1: 
                re.insert(0,"0") 
            elif e == "1" or f == "1": 
                re.insert(0,"1") 
                ca = 0 
            elif ca == 1: 
                re.insert(0, "1") 
                ca = 0 
            else: 
                re.insert(0,"0") 
        if c: 
            while c: 
                e = c.pop() 
                if ca == 1 and e == "1": 
                    re.insert(0,"0") 
                elif e == "1": 
                    re.insert(0, "1") 
                elif ca == 1: 
                    re.insert(0,"1") 
                    ca = 0 
                else: 
                    re.insert(0,"0") 
        elif d: 
            while d: 
                f = d.pop() 
                if ca == 1 and f == "1": 
                    re.insert(0,"0") 
                elif f == "1": 
                    re.insert(0,"1") 
                elif ca == 1: 
                    re.insert(0, "1") 
                    ca = 0 
                else: 
                    re.insert(0,"0")
        if ca == 1:
            re.insert(0,"1")
        return "".join(re)