def sumSubarrayMins(arr):
    # s=0
    # m=min(arr)
    # for i in range(0,len(arr)):
    #     if arr[i]==m:
    #         s+=arr[i]*(len(arr)-i)
    #         continue
    #     else:
    #         for j in range(1,len(arr)+1):
    #             if len(arr)-i>=j:
    #                 s+=min(arr[i:j+i])
    #             else:
    #                 continue
        
    # return s

# 每个元素E=A[i]的辐射范围都是一个连续数组，这个辐射范围内产生的所有子数组最小值都为E，因此E在每个子数组中对答案的贡献值都为E。如果这个辐射范围内的子数组有n个，那么总贡献值为n*E。

# 那么这个辐射范围内能产生多少个子数组呢？
# 我们枚举一下能产生多少个不同的左右边界对即可。假设辐射范围的左边界为left，右边界为right，元素E的下标为i，那么子数组的左边界应该在[left,i]中选取，子数组的右边界应该在[i,right]中选取。
# 因此子数组个数为(i - left + 1) * (right - i + 1)(i−left+1)∗(right−i+1)，也就是说元素A[i]对答案的总贡献值为A[i]*(i - left + 1) * (right - i + 1)A[i]∗(i−left+1)∗(right−i+1)。

# 那么我们只要计算出每个元素的贡献值，然后求和就好了。
    n = len(arr)
    # 左边界 left[i] 为左侧严格小于 arr[i] 的最近元素位置（不存在时为 -1）
    left, st = [-1] * n, []
    for i, x in enumerate(arr):
        while st and arr[st[-1]] >= x:
            st.pop()  # 移除无用数据
        if st: left[i] = st[-1]
        st.append(i)

    # 右边界 right[i] 为右侧小于等于 arr[i] 的最近元素位置（不存在时为 n）
    right, st = [n] * n, []
    for i in range(n - 1, -1, -1):
        while st and arr[st[-1]] > arr[i]:
            st.pop()  # 移除无用数据
        if st: right[i] = st[-1]
        st.append(i)

    ans = 0
    for i, (x, l, r) in enumerate(zip(arr, left, right)):
        ans += x * (i - l) * (r - i)  # 累加贡献
    return ans % (10 ** 9 + 7)

print(sumSubarrayMins([11,81,94,43,3]))

# lst=[3,1,2,4]
# print(lst[1:4])
# print(min(lst[1:4]))