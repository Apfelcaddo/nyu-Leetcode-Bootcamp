class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split(" ")
        res = []
        for w in reversed(s):
            if w:
                res.append(w)
        return " ".join(res)