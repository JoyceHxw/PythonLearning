# 给你一个长度为 n 的字符串数组 names 。你将会在文件系统中创建 n 个文件夹：在第 i 分钟，新建名为 names[i] 的文件夹。
# 由于两个文件 不能 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 (k) 的形式为新文件夹的文件名添加后缀，其中 k 是能保证文件名唯一的 最小正整数 。
# 返回长度为 n 的字符串数组，其中 ans[i] 是创建第 i 个文件夹时系统分配给该文件夹的实际名称。
class Solution:
    def getFolderNames(self, names: list[str]) -> list[str]:
        results=[]
        index={}
        print(names)
        for name in names:
            if name not in results:
                results.append(name)
                index[name]=1
            else:
                k=index[name]
                while name+"("+str(k)+")" in index:
                    k+=1
                t=name+"("+str(k)+")"
                results.append(t)
                index[name]=k+1
                index[t]=1
                # 超出时间限制
                # for i in range(1,len(names)):
                #     a=name
                #     a+=f"({i})"
                #     if a not in results:
                #         results.append(a)
                #         break
        return results

S=Solution()
# print(S.getFolderNames(["gta","gta(1)","gta","avalon"]))
# print(S.getFolderNames(["kingston(0)","kingston","kingston"]))
print(S.getFolderNames(["m","t","y(4)","t","a","p","h","h","z","z(2)(2)","x(3)","h(4)(3)","l","z(1)"
                        ,"h","s(1)(2)","y(3)(2)","m(3)","i","h","u","j(1)(4)","q","j(1)","c","n(4)"
                        ,"k","s(1)(4)","p(2)","m","r(1)(4)","k(3)","d(3)(1)","e(4)"]))
