# coding=utf-8
# from csv import reader
# import cvs
import os
import time


def main():
    # test_readfile01()
    # test_readfile02()
    test_fcopy()


def test_readfile01():
    with open('test_numpy.py') as csv_file1:
        lines = csv_file1.read().split()
        for line0 in lines:
            print(line0)

        while True:
            line = csv_file1.readline()
            if not line:
                break
            print(line)


def test_readfile02():
    with open('test_numpy.py') as csv_file2:
        for line1 in csv_file2:
            print(line1)


def test_fcopy():
    source = ['c:\\cmdata']
    target_dir = 'c:\\backup'
    target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)
    zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))
    print("Zip command is:", zip_command)
    print("Running...")
    if os.system(zip_command) == 0:
        print("Successful backup to", target)
    else:
        print("Backup Fail")


if __name__ == '__main__':
    main()
