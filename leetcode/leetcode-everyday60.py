# 你是一位系统管理员，手里有一份文件夹列表 folder，你的任务是要删除该列表中的所有 子文件夹，并以 任意顺序 返回剩下的文件夹。
# 如果文件夹 folder[i] 位于另一个文件夹 folder[j] 下，那么 folder[i] 就是 folder[j] 的 子文件夹 。
# 文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：'/' 后跟一个或者多个小写英文字母。
# 例如，"/leetcode" 和 "/leetcode/problems" 都是有效的路径，而空字符串和 "/" 不是。

# 暴力
# class Solution:
#     def removeSubfolders(self, folder: list[str]) -> list[str]:
#         folder.sort(key=lambda x : len(x))
#         f=[]
#         for path in folder:
#             a=0
#             while a!=-1:
#                 a=path.find('/',a+1)
#                 if path[0:a] in f:
#                     break
#             if a==-1:
#                 f.append(path)
#         return f

# 排序
# 我们先将数组 folder 按照字典序排序，然后遍历数组，
# 对于当前遍历到的文件夹 f，如果它的长度大于等于答案数组中最后一个文件夹的长度，并且它的前缀包含答案数组的最后一个文件夹再加上一个 /，
# 则说明 f 是答案数组中最后一个文件夹的子文件夹，我们不需要将其加入答案数组中。
# 否则，我们将 f 加入答案数组中。
class Solution:
    def removeSubfolders(self, folder: list[str]) -> list[str]:
        folder.sort()
        ans = [folder[0]]
        print(ans)
        for f in folder[1:]:
            m, n = len(ans[-1]), len(f)
            if m >= n or not (ans[-1] == f[:m] and f[m] == '/'):
                ans.append(f)
        return ans



S=Solution()
print(S.removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))
