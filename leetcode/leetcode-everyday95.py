class Solution:
    def prevPermOpt1(self, arr: list[int]) -> list[int]:
        # 从尾部开始找最长递减子序列
        n=len(arr)
        i=n-1
        j=n-2
        isFlag=True
        while i>0 and isFlag==True:
            j=i-1
            while j>-1:
                if arr[j+1]-arr[j]<0:
                    isFlag=False
                    break
                j-=1
            if isFlag==True:
                i-=1
        if isFlag==True:
            return arr
        print("i=",i)
        print("j=",j)
        isFlag2=True
        # 可能有相邻重复值
        while i>j and isFlag2==True:
            if arr[i]<arr[j]:
                while arr[i]==arr[i-1]:
                    i-=1
                isFlag2=False
                break
            if isFlag2==True:
                i-=1
        temp=arr[j]
        arr[j]=arr[i]
        arr[i]=temp
        return arr

        # 代码精简
        # n = len(arr)
        # for i in range(n - 2, -1, -1):
        #     if arr[i] > arr[i + 1]:
        #         j = n - 1
        #         while arr[j] >= arr[i] or arr[j] == arr[j - 1]:
        #             j -= 1
        #         arr[i], arr[j] = arr[j], arr[i]
        #         break
        # return arr

S=Solution()
print(S.prevPermOpt1([3,1,1,3]))