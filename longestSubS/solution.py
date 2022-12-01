class Solution:
    
    def substring(count,s):

        sub = ""
        if count < len(s):
            i = s[count]
        
            while(i not in sub):
                sub += i
                count +=1

                if count < len(s):
                    i = s[count]
                else:
                    break        
        return sub
    
    def lengthOfLongestSubstring(self, s: str) -> int:

        subs = ""
        for i in range(len(s)):
            newSubs = Solution.substring(i,s)

            if len(subs) < len(newSubs):
                subs = newSubs
                
        return len(subs)
    
    def lengthOfLongSub(count,s):
        
        sub = ""
        if count < len(s):
            i = s[count]
        
            while(i not in sub):
                sub += i
                count +=1

                if count < len(s):
                    i = s[count]
                else:
                    break
        return sub

print(Solution().lengthOfLongestSubstring("dvdf"))

