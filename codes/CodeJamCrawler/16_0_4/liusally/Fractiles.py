

def main():
    of = open('fractiles-small.out', 'w', 1)

    with open('D-small-attempt0.in', 'r') as f:
        count = int(f.readline().rstrip('\n'))
        for i in range(count):
            line = f.readline().rstrip('\n')
            nums = line.split(' ')
            K = int(nums[0])
            C = int(nums[1])
            S = int(nums[2])

            of.write('Case #{}:'.format(i + 1))
            for ind in range(1, K+1):
                position = (ind - 1) * K**(C-1) + 1
                of.write(' {}'.format(position))

            of.write('\n')

    of.close()

if __name__ == "__main__":
    main()
