# from gift import have_gift
import gift


def send1():
    # 发礼物方法
    print("发礼物啦")
    # have_gift=True
    # print(id(have_gift))
    gift.have_gift = True
    print(id(gift.have_gift))
