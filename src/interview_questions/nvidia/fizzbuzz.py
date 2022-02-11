# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


def fizz_buzz(num):
    output = []
    for i in range(1, num + 1):
        txt = ''
        if i % 3 == 0:
            txt += "Fizz"
        if i % 5 == 0:
            txt += "Buzz"

        if txt == '':
            txt = str(i)
        output.append(txt)

    return output


assert fizz_buzz(3) == ["1", "2", "Fizz"]
assert fizz_buzz(15) == ["1", "2", "Fizz", "4", "Buzz", "Fizz",
                         "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
