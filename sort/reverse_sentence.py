#题:翻转句子,但不要翻转每个单词的拼写
class Solution:
    def ReverseSentence(self, s):
        return " ".join(s.split()[::-1]) if s.strip() != "" else s

    def ExplainReverseSentence(self,s):
        #input = "you love me"
        if s.strip()=="": return s  # defence, in case of empty input
        list_split = s.split()  # ['you', 'love', 'me']
        reversed_list = list_split[::-1]  # ['me', 'love', 'you']
        joined_string = " ".join(reversed_list)
        # if "".join(reversed_list), you will get "meloveyou" as output
        return joined_string

if __name__ == '__main__':
    ss=Solution()
    print(ss.ExplainReverseSentence("you love me"))