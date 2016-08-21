__author__ = 'Giruvegan'

letter_dict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F',
               6:'G', 7:'H', 8:'I', 9:'J', 10:'K', 11:'L',
               12:'M', 13:'N', 14:'O', 15:'P', 16:'Q', 17:'R',
               18:'S', 19:'T', 20:'U', 21:'V', 22:'W', 23:'X',
               24:'Y', 25:'Z'}

def plans(case_input):
    input = case_input.split(' ')
    ans = []
    senates = {}
    for i in range(len(input)):
        senates[letter_dict[i]] = int(input[i])

    while senates:
        sorted_items = sorted(senates.items(), key=lambda x: -x[1])
        if len(sorted_items) == 2:
            keys = [sorted_items[0][0], sorted_items[1][0]]
            ans.append(''.join(keys))
            for key in keys:
                senates[key] -= 1
                if senates[key] == 0:
                    senates.pop(key)
        else:
            key = sorted_items[0][0]
            ans.append(key)
            senates[key] -= 1
            if senates[key] == 0:
                senates.pop(key)

    return ' '.join(ans)

if __name__ == '__main__':

    filepath = 'A-large.in.txt'
    fout = open(filepath.split('.')[0] + '.out.txt', 'w')
    all_input = open(filepath, 'r').readlines()
    case_num = int(all_input[0])
    for i in range(2, len(all_input), 2):
        case_input = all_input[i].replace('\n', '')
        fout.write('case #' + str(i/2) + ': ' + plans(case_input) + '\n')