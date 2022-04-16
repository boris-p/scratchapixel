# we want to loop over the bits and always shift by one
# we shift right but before that we check if the number is even or odd
# if it's odd we know we need to add to the leftpart of the array
# I decided to do this by having a another number which represents the result
# and if the number in the rightmost side is 1 add X^2 where X is


# there might be a better solution where we can avoid storing
# another number or avoid the division but as a whiteboarding question
# this is what I came up with

import cProfile


def reverse_number(num, num_of_bits=32):
    b = '{:0{width}b}'.format(num, width=num_of_bits)
    return int(b[::-1], 2)

    # num_to_add = 2**(num_of_bits - 1)
    # res = 0
    # for _ in range(num_of_bits):
    #     remainder = num % 2

    #     num >>= 1

    #     # add 1 to the current power (going from left to right)
    #     if remainder == 1:
    #         res += num_to_add
    #     num_to_add /= 2

    # return res


def main():
    # I want to start with a simple example so keeping the number
    # of bits as a param
    for _ in range(100000):
        assert reverse_number(4, 3) == 1
        assert reverse_number(1, 3) == 4

        # 10100010
        assert reverse_number(162, 8) == 69
        # 01000101
        assert reverse_number(69, 8) == 162

        assert reverse_number(0) == 0

        assert reverse_number(4294967295) == 4294967295

        assert reverse_number(1) == 2**31
        assert reverse_number(2**31) == 1


if __name__ == '__main__':
    cProfile.run('main()')
