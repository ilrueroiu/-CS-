def binary_summ(f_num, s_num):
    bi_summ = ''
    shift = 0

    for i in range(max(len(bin(f_num)[2:]), len(bin(s_num)[2:]))):
        f_digit = f_num & 1
        s_digit = s_num & 1

        summ = f_digit ^ s_digit ^ shift
        bi_summ = ''.join((str(summ), bi_summ))
        shift = (f_digit & s_digit) | ((f_digit ^ s_digit) & shift)

        f_num >>= 1
        s_num >>= 1
    mask = 2 ** len(bi_summ)
    bi_summ = bin((shift * mask) | int(bi_summ, 2))[2:]
    return shift, bi_summ
