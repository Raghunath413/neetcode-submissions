
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp1 = {}
        for x in t:
            mp1[x] = mp1.get(x, 0) + 1

        n = len(mp1)
        mp2 = {}
        count = 0
        start = 0
        starti = 0
        ans = len(s) + 1

        for end in range(len(s)):
            if s[end] in mp1:
                mp2[s[end]] = mp2.get(s[end], 0) + 1

                if mp2[s[end]] == mp1[s[end]]:
                    count += 1

            while count == n:
                length = end - start + 1

                if length < ans:
                    ans = length
                    starti = start

                if s[start] in mp1:
                    if mp2[s[start]] == mp1[s[start]]:
                        count -= 1

                    mp2[s[start]] -= 1

                start += 1

        if ans == len(s) + 1:
            return ""

        return s[starti:starti + ans]
