class Solution:
    def decodeString(self, s: str) -> str:
        self.countstack =[]
        self.stringstack =[]
        i = 0
        while i < len(s):
            
            if s[i].isalpha():
                self.stringstack.append(s[i])
            elif s[i] == "[":
                self.countstack.append("/")
                self.stringstack.append(s[i])
            elif s[i].isdigit():
                self.countstack.append(int(s[i]))
            elif s[i] == "]":
                print(self.countstack)
                buffer = 0
                self.countstack.pop()
                j = 0
                while self.countstack and self.countstack[-1]!= "/":
                    buffer += self.countstack.pop() * 10 ** j
                    j += 1
                s2 = ''
                res = ''
                while self.stringstack[-1] != '[':
                    s2 = self.stringstack.pop() + s2
                self.stringstack.pop()
                for j in range(buffer):
                    res += s2

                self.stringstack.append(res)
            i += 1
            
        return ("".join(self.stringstack))
        