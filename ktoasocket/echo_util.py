from datetime import datetime


def calcDate(gubun):
    now = datetime.now()
    if gubun == 'd':
        return f"{now.year}{now.month:02}{now.day:02}"
    elif gubun == 't':
        return f"{now.hour:02}{now.minute:02}{now.second:02}"
    else:
        return f"{now.year}{now.month:02}{now.day:02}{now.hour:02}{now.minute:02}{now.second:02}"


def calcAccptNum(sendPart):
    return f"{calcDate('d')}{sendPart}{'0000000'}"


if __name__ == '__main__':
    calcDate('t')
