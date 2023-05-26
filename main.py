# write your code here
def analyzer(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        line_num = 1
        for line in file:
            if len(line) > 79:
                print(f'Line {line_num}: S001 Too Long')
            line_num += 1


def main():
    filename = input()
    analyzer(filename)


main()
