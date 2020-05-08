import math

# 管理職


def get_m(k, y):
    s = (k+y)*17/100
    m = k + y - round(s, -1)-(k+y-round(s, -1))*10/100
    return m
# 一般社員


def get_n(k, z_time):
    z_unit = (k/160*1.25)/10
    z = z_time*math.floor(z_unit)*10
    s = (k+z)*17/100
    n = k+z-round(s, -1) -(k+z-round(s, -1))*10/100
    return n
# アルバイト


def get_a(time, unit):
    a = time*unit-time*unit*10/100
    return a


if __name__ == "__main__":
	#浜口知実
	ht = get_m(360000, 30000)
    # 寺尾哲雄
    tt = get_m(350000, 80000)
    # 若林仁継
    wh = get_m(375000, 40000)
    # 寺田帆香
    th = get_n(320000, 30)
    # 広田康弘
    hy = get_n(295000, 20)
    # 菅沼洋一郎
    sy = get_n(220000, 35)
    # 菊池章
    ka = get_a(90, 1200)
    # 山岸柑奈
    yk = get_a(120, 1000)
    # 給与振込額の表示
    print(f' 寺尾哲雄 = {int(tt)}')
    print(f' 若林仁継 = {int(wh)}')
    print(f' 寺田帆香 = {int(th)}')
    print(f' 広田康弘 = {int(hy)}')
    print(f' 菅沼洋一郎 = {int(sy)}')
    print(f' 菊池章 = {int(ka)}')
    print(f' 山岸柑奈 = {int(yk)}')
    print(f' 浜口知実 = {int(ht)}'))
