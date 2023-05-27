# Python3.10
import os
import sys

def analyzer(filename):
    blank_lines = 0
    with open(filename, "r", encoding="utf-8") as file:
        line_num = 1
        for line in file:
            code = line.split("#")[0][:-1]
            comment = line.split("#")[1:2]
            if len(line) > 79:
                print(f"{os.path.relpath(filename)}: Line {line_num}: S001 Too Long")
            if count_space(line) % 4 != 0:
                print(f"{os.path.relpath(filename)}: Line {line_num}: S002 Indentation is not a multiple of four")
            if code.strip().endswith(";"):
                print(f"{os.path.relpath(filename)}: Line {line_num}: S003 Unnecessary semicolon")
            if comment:
                if code:
                    reversed_code = code[::-1]
                    if count_space(reversed_code) < 1:
                        print(
                            f"{os.path.relpath(filename)}: Line {line_num}: S004 At least two spaces before inline comment required"
                        )
                if "todo" in comment[0].lower():
                    print(f"{os.path.relpath(filename)}: Line {line_num}: S005 TODO found")
            if code.strip() == "":
                blank_lines += 1
            else:
                if blank_lines > 2:
                    print(f"{os.path.relpath(filename)}: Line {line_num}: S006 More than two blank lines used")
                blank_lines = 0
            line_num += 1


def count_space(line):
    count = 0
    for char in line:
        if char == " ":
            count += 1
        else:
            break
    return count


def main():
    args = sys.argv
    file_or_folder(args[1])


def file_or_folder(path):
    if os.path.isdir(path):
        filelist = sorted(os.listdir(path))
        for file in filelist:
            if file.endswith(".py"):
                analyzer(os.path.join(path, file))
    else:
        analyzer(path)


main()
