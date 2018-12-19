# 练习极客时间 黄申 程序员的数学基础课
# 05 | 递归（上）：泛化数学归纳，如何将复杂问题简单化？
# clj 2018.12.19 

rewards = [1, 2, 5, 10]

def getResult(totalReward, result=[]):
    if totalReward == 0:
        print(result)
    elif totalReward < 0:
        return
    else:
        for rd in rewards:
            newResult = result.copy()
            newResult.append(rd)
            getResult(totalReward - rd, newResult)

if __name__ == '__main__':
    getResult(2)
    getResult(3)