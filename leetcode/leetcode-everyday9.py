class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        cnt=0
        for i in items:
            if ruleKey=="type":
                if i[0]==ruleValue:
                    cnt+=1
            elif ruleKey=="color":
                if i[1]==ruleValue:
                    cnt+=1
            elif ruleKey=="name":
                if i[2]==ruleValue:
                    cnt+=1
        
        return cnt