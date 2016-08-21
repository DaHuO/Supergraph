

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True


def main():
    cases = int(raw_input())
    for case in range(1, cases+1):
        line = raw_input().split(' ')
        length = int(line[0])
        num_coins_needed = int(line[1])

        start = '1' + '0'*(length-2) + '1'
        solution = {}
        possibile_coins = []
        current_num = start
        stop = '1' + '0'*(length-1) + '1'

        while current_num != stop:
            if not is_prime(int(current_num, base=2)):
                possibile_coins.append(current_num)
            current_num = bin((int(current_num, base=2) + 2))[2:]


        for base in range(3, 11):
            #print 'base ', base, 'size of list', len(possibile_coins)
            coins_to_consider = list(possibile_coins)
            counter = 0
            removed = 0

            for coin in coins_to_consider:
                counter += 1
                #if counter % 200 == 0:
                    #print 'checked {} numbers'.format(counter)


                cur_num = int(coin, base=base)
                if is_prime(cur_num):
                    possibile_coins.remove(coin)

                    #removed += 1
                    #if removed % 50 == 0:
                        #print 'removed {} numbers'.format(removed)
                elif base == 10:
                    solution[coin] = []
                    if len(solution) == num_coins_needed:
                        break

        print 'Case #1:'
        for number in solution.iterkeys():
            print number,
            for base in range(2, 11):
                cur_num = int(number, base=base)
                for divisor in range(2, int(cur_num**(.5)) +1):
                    if cur_num % divisor == 0:
                        print divisor,
                        #solution[number].append(divisor)
                        break
            print


if __name__ == "__main__":
    main()

