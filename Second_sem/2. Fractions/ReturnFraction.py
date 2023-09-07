from math import gcd

input_num1 = '4/5'
input_num2 = '3/4'


def fr_operations(fract1, fract2):
    split1 = fract1.split("/")
    split2 = fract2.split("/")
    num1, den1 = int(split1[0]), int(split1[1])
    num2, den2 = int(split2[0]), int(split2[1])
    common_div = den1 * den2 // gcd(den1, den2)
    summary = int(num1 * (common_div / den1) + num2 * (common_div / den2))
    if summary > common_div:
        result_sum = f'{summary//common_div}({summary - common_div}/{common_div}) or {summary}/{common_div}'
    else:
        result_sum = f'{summary}/{common_div}'
    mult = (num1 * num2), (den1 * den2)
    common_div = gcd(mult[0], mult[1])
    result_mult = f'{int(mult[0]/common_div)}/{int(mult[1]/common_div)}'
    return result_sum, result_mult


result = fr_operations(input_num1, input_num2)
print(f'{input_num1} + {input_num2} = {result[0]}')
print(f'{input_num1} x {input_num2} = {result[1]}')
