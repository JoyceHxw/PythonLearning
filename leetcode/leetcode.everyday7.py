
def arraySign(nums) -> int:
    cnt_neg=0
    cnt_pos=0
    for num in nums:
        if num<0:
            cnt_neg+=1
        elif num>0:
            cnt_pos+=1
        else:
            return 0
    if cnt_neg%2==0:
        return 1
    else:
        return -1