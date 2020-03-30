# coding=utf-8
import calendar
import random
import sys
import re
from datetime import datetime, date, time, timedelta


def main():
    # print(calendar.month(2019, 12))

    # print(total(10, 1, 2, 3, vegetables=50, fruits=100))
    # help(total)
    # print(total.__doc__)

    # test_str01()
    # test_syspath()
    # test_prt()
    # test_random()
    # test_re()
    test_datetime()


def test_datetime():
    date1 = datetime(1970, 10, 1)
    print("date1:{}".format(date1))
    today = date.today()
    print("today:{}".format(today))
    # 요일1 정보 === 0:월, 1:화 ...
    print("월:{0}, 일:{1}, 요일1:{2}, 요일2:{3}".format(today.month, today.day, today.weekday(), "월화수목금토일"[today.weekday()]))
    now = datetime.now()
    print("{0}년 {1:02}월 {2:02}일 - {3:02}시 {4:02}분".format(now.year, now.month, now.day, now.hour, now.minute))
    print("{0.year}년 {0.month:02}월 {0.day:02}일({1}) - {0.hour:02}시 {0.minute:02}분".format(now, "월화수목금토일"[now.weekday()]))
    print(f"{now.year}년 {now.month:02}월 {now.day:02}일({'월화수목금토일'[now.weekday()]}) - {now.hour:02}시 {now.minute:02}분")
    print("오늘날짜:", now.strftime("%Y%m%d"))
    print("1970/10/1 이후 몇일이나 지났나:", now - date1)
    print("검증:", date1 + timedelta(days=18026))


def total(initial=5, *numbers, **keywords):
    """Sum of parameter value.
     Sum of param value."""
    count = initial
    for number in numbers:
        print("number:", number)
        count += number
    for key in keywords:
        print("key:{0}, value:{1}".format(key, keywords[key]))
        count += keywords[key]
    return count


def test_prt():
    age = 20
    name = 'molo'
    print("{0} was {1} years old when he wrote this book".format(name, age))
    print("why is {name1} playing with that python?".format(name1="snoopy"))
    print("{0:.3f}".format(1.0/3))
    print("{0:_^11}".format("hello"))


def test_str01():
    name = "Swrooop"

    if name.startswith("Swa"):
        print("Yes Swa")

    if 'a' in name:
        print("Yes a")

    if name.find("war") != -1:
        print("Yes war")

    delimiter = "_*_"

    mylist = ["pengsu", "nakta", "tokki"]

    print(delimiter.join(mylist))


def test_random():
    a = random.randint(0, 9)
    print(a)

    b = int(input("input number"))
    if a == b:
        print("ok")
    else:
        print("no")


def test_syspath():
    print("command line args:")
    for i in sys.argv:
        print(i)

    print("\nThe PythonPath is {}\n".format(sys.path))


def test_re():
    sample = '124324python홍길동010-1234-5678sdkk'
    pattern = re.compile(r'[가-힣]{2,4}')
    match = re.search(pattern, sample)
    print(match.group())
    pattern2 = re.compile(r'01\d-\d{3,4}-\d{4}')
    match2 = re.search(pattern2, sample)
    print(match2.group())


if __name__ == '__main__':
    main()
