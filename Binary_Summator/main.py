def binary_summ(f_num, s_num):
    bi_summ = ''
    shift = 0

    for i in range(max(len(bin(f_num)), len(bin(s_num)))):
        f_digit = f_num & 1
        s_digit = s_num & 1

        summ = f_digit ^ s_digit ^ shift
        bi_summ += str(summ)
        shift = (f_digit & s_digit) | ((f_digit ^ s_digit) & shift)

        f_num >>= 1
        s_num >>= 1
    bi_summ += str(shift)
    bi_summ = bi_summ[::-1]

    return bi_summ
