def main():
    test_type()
    test_inputchk()


def square(*x):
    return x[0] ** x[1]


def test_type():
    print(type(square))
    print(square(5, 3, 4, 3))


def test_inputchk():
    # 입력값 체크
    print("생년월일을 입력하세요 : ", end="")
    try:
        num = int(input())
    except ValueError as e:
        print("입력값 확인하세요.(숫자만 가능합니다.)")
        print("exception : ", e)
    else:
        print("입력한 숫자는", num, "입니다.")
    finally:
        print("Thank you...")


if __name__ == '__main__':
    main()
