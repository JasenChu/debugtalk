# 练习极客时间 黄申 程序员的数学基础课
# 05 | 递归（上）：泛化数学归纳，如何将复杂问题简单化？
'''
课后作业 
一个整数可以被分解为多个整数的乘积，例如，6 可以分解为 2*3。
请使用递归编程的方法，为给定的整数n，找到所有可能的分解（1在解中最多只出现1次）
例如，输入8，输出是可以是1*8，8*1，2*4，4*2，1*2*4，...
'''
import copy
import math

def get_product_foctors(num):
    if num <= 0:
        return []
    else:
        product_factors = []
        print(num)
        print(math.ceil(math.sqrt(num)))
        for n in range(1, math.ceil(math.sqrt(num)) + 1):
            # 如果num%n有余数不打印，没有余数打印
            if n > 0 and num % n == 0:
                product_factors.append(n)
                product_factors.append(int(num / n))
                print(product_factors)
        return sorted(list(set(product_factors)))

#print(get_product_foctors(6))
def get_multiply_combo(product, result = []):
    product_foctors = get_product_foctors(product)
    for i in product_foctors:
        new_result = copy.copy(result)
        new_result.append(i)
        divsior = product // i
        if i == 1 or i == product:
            new_result.append(divsior)
            print(new_result)
        else:
            get_multiply_combo(divsior, new_result)
if __name__ == '__main__':
    product_foctors = get_product_foctors(4)
    # print(product_foctors)

    # get_multiply_combo(6)

    # get_multiply_combo(8)
