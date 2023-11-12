import math
import main

print('Type the max number of binary summ you want to check. If you want to quit, type "quit".')
input_info = input()
while input_info.lower() != 'quit':
    try:
        max_num = int(input_info)
        break
    except ValueError:
        print('Try again. If you want to quit, type "quit".')
        input_info = input()
else:
    print('See you next time!')
    quit()

nums_cnt = 0
found = False
pairs = (max_num + 1) * max_num / 2

for fNum in range(max_num):
    for sNum in range(fNum, max_num):
        print(fNum, sNum)
        s, bi_summ = main.binary_summ(fNum, sNum)

        def_summ = fNum + sNum
        if def_summ != int(bi_summ, 2):
            print('Program worked incorrectly with numbers: {}, {}\n'.format(fNum, sNum))
            found = True
            break

        nums_cnt += 1
        print('Loading ... {}%\n'.format(math.floor(nums_cnt / pairs * 100)))

if not found:
    print('Hooray! Program worked correctly with a lot of numbers!')
