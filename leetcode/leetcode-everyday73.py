class Solution:
    def minimumDeletions(self, s: str) -> int:
        # # 超出时间限制
        # min_cnt=len(s)
        # # 遍历每一种分割线
        # for i in range(len(s)+1):
        #     cnt_a=0
        #     cnt_b=0
        #     for l in s[:i]:
        #         if l=='b':
        #             cnt_b+=1
        #     for l in s[i:]:
        #         if l=='a':
        #             cnt_a+=1
        #     print(cnt_a)
        #     print(cnt_b)
        #     min_cnt=min(min_cnt,cnt_a+cnt_b)
        # return min_cnt

        # 从前往后遍历，所以维护a的数量
        ans = delete = s.count('a')
        for c in s:
            # 遍历变成动态规划
            delete -= 1 if c == 'a' else -1
            if delete < ans:  # 手动 min 会快很多
                ans = delete
        return ans


S=Solution()
print(S.minimumDeletions("a"))
# print(S.minimumDeletions("aaaaaaaaaaaaaa"))