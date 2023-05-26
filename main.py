#Python3.10


def analyzer(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        line_num = 1
        for line in file:
            code = line.split('#')[0].strip()
            if len(line) > 79:
                print(f'Line {line_num}: S001 Too Long')
            if line.startswith(' ' * 4):
                print(f'Line {line_num}: S002 Indentation is not a multiple of four')
            if code.endswith(';'):
                print(f'Line {line_num}: S003 Unnecessary semicolon')
            line_num += 1
            


def main():
    filename = input()
    analyzer(filename)


main()
