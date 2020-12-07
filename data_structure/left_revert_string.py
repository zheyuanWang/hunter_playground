test_string1 = 'abcd000'
test_string2 = ' kd '

class Solution_vanila:
    def reverseLeftWords(self, s: str, n: int) -> str:
        left = s[0:n]
        right = s[n:]
        result = right + left
        return result

class Solution:
    "remove tmp parameters"
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[0:n]

so = Solution()
print(so.reverseLeftWords(test_string2,2))
