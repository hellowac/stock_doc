import sys

a = "31.42	171.78	384.79	708.19	1110.43	1593.16	2199.94	2893.34	3675.97	4596.49	6076.84	8133.84	10835.6	14150.65	27097.36	44564.71	63088.31	82699.85	103431.98	125496.85	148395.9	172154.15	196797.38	222352.14	248845.77	276306.43	304763.15	334245.8	364785.16	396869.15	429749.45"

b = a.split()

c = [float(i) for i in b]

list_c = list(c)


len = len(list_c)

for i in range(0, len):

    if i + 1 == len:
        break

    start = list_c[i]
    end = list_c[i+1]

    percent = ((end-start) / start) * 100
    percent = round(percent, 2)

    print(f"{start} => {end} 增长率为: {percent}")

# print(c)


def get_income(principal: int, apr: float, days: int) -> float:
    """ 计算按年利率持有指定天数所获得的利息

        principal:  本金
        apr: 年利率
        days: 持有天数
    
    返回: float 类型的利息值
    """
    # 计算利息

    return principal * apr * (days/365)


def cycle_income(capital: int, apr: float, days: int, cycle:int):
    """ 计算按年率持有指定天数并且复利N次所获得的利息收入。

        principal:  本金
        apr: 年利率
        days: 持有天数
        cycle: 复利几次
    """

    print(f"{capital} 按年利率 {apr} 持有天数{days} 复利 {cycle} 次, 计算如下:")

    # 累计本金
    congest_capital = capital
    income_total = 0

    for i in range(1, cycle + 1):

        income = get_income(congest_capital, apr, days)
        income = round(income, 2)
        income_total += income

        congest_capital += income
        congest_capital = round(congest_capital, 2)

        print(f"{capital} 第{i}次 共获得利息: {income}, 本息共计: {congest_capital};")
    
    return_rate = round((income_total / capital) * 100, 2)
    print(f"{capital} 元，一共占用资金: {days * cycle} 天, 共获利: {income_total}元, 收益率: {return_rate}%")



if __name__ == "__main__":
    capital = 55000  # 本金
    rate = 0.0205     # 年利率
    days = 15        # 持有天数
    cycle = 4        # 复利四次

    cycle_income(capital, rate, days, cycle)

    # print("--" * 10)

    # capital = 55000  # 本金
    # rate = 0.0215     # 年利率
    # days = 66        # 持有天数
    # cycle = 1        # 复利1次

    # cycle_income(capital, rate, days, cycle)

    # print("--" * 10)

    # capital = 10000  # 本金
    # rate = 0.08     # 年利率
    # days = 14        # 持有天数
    # cycle = 1        # 复利1次

    # cycle_income(capital, rate, days, cycle)

    # print("--" * 10)

    # capital = 5000  # 本金
    # rate = 0.0508     # 年利率
    # days = 90        # 持有天数
    # cycle = 1        # 复利1次

    # cycle_income(capital, rate, days, cycle)


