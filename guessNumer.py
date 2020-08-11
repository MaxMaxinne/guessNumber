import random
def judge(guess,ans):
    colorCount=0
    rightCount=0
    colorList=[]
    for index,value in enumerate(guess):
        if value==ans[index]:
            if value not in colorList:
                colorCount+=1
                colorList.append(value)
            rightCount+=1
        elif value in ans and value not in colorList:
            colorCount+=1
            colorList.append(value)
    if rightCount==4:
        print("你猜对了！")
        return True
    else:
        print("%d个颜色正确，%d个全部正确"%(colorCount,rightCount))
        return False
totalChance=8
times=1
ballPool=[1,2,3,4,5,6]
ans=random.sample(ballPool,4)
while times<totalChance:
    guessStr=input("请输入您的推测：")
    userGuess=[int(ele) for ele in guessStr.split(' ')]
    if judge(userGuess,ans):
        break
    times+=1
    print("还有%d次机会！"%(totalChance-times))
print(ans)