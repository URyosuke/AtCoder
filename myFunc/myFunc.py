# 整数nを10進数 -> base進数に変換する関数
def convDec2Base(n, base):
    result = ' '
    # 10進数 → n進数
    while n > 0:
        result = str(n%base) + result
        n //= base
    return int(result)

# base進数で表されたnを10進数に変換する関数
def convBase2Dec(n, base):
    n = str(n)
    result = 0
    for i in range(len(n)):
        result += int(n[i]) * (base ** len(n) -i -1)
    return result

