class Solution:

    def encode(self, strs: List[str]) -> str:
        for i, v in enumerate(strs):
            l = len(v)
            strs[i] = str(l)+"#"+strs[i]
        return " ".join(strs)

    def decode(self, s: str) -> List[str]:
        l = len(s)
        p = 0
        temp = ""
        ans = []
        while p < l:
            if s[p] != "#":
                temp += s[p]
                p += 1
                continue
            else:
                ss = int(temp)

            ans.append(s[p+1:p+1+ss])
            temp = ""
            p += ss + 1
        return ans 