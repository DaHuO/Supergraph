__author__ = 'Sander van Rijn <svr003@gmail.com>'

if __name__ == '__main__':

    num_cases = int(input())

    for i in range(1, num_cases+1):

        digits = {d for d in '0123456789'}
        history = set()
        base_number = int(input())
        cur_number = 0
        insomniac = False

        while len(digits) > 0:

            cur_number += base_number
            for digit in str(cur_number):
                digits.discard(digit)

            if cur_number in history:
                insomniac = True
                break
            else:
                history.add(cur_number)

        if insomniac:
            print('Case #{}: INSOMNIA'.format(i))
        else:
            print('Case #{}: {}'.format(i, cur_number))
