import pathlib


# Write a python script which does the following:
# Scans all python files in this projects +
# For each such file counts the number of text lines in it +
# Prints the sum of all lines in all files in current project +
# Count all lines, even empty ones +
# Prints 10 files with the most line count TODO!
# Rewrite function using glob module TODO!


def count_lines(path):
    empty_lines = 0
    comment_lines = 0
    code_lines = 0
    python_files = 0
    for entry in path.iterdir():
        if entry.is_file and entry.name.endswith('.py'):
            python_files += 1
            with open(entry, 'r', encoding="utf-8") as f:
                for line in f.readlines():
                    line = line.strip()  # remove spaces at the beginning and in the end
                    if line == '':
                        empty_lines += 1
                    elif line.startswith('#'):
                        comment_lines += 1
                    else:
                        code_lines += 1
        elif entry.is_dir():
            empty, comments, code, p_files = count_lines(entry)
            empty_lines += empty
            comment_lines += comments
            code_lines += code
            python_files += p_files

    return empty_lines, comment_lines, code_lines, python_files


print('Empty lines: {} \nComment lines: {} \nCode lines: {} \nTotal count of Python files: {}'.format(
    *count_lines(pathlib.Path(__file__).parent)))

# -------------------------------------------------------------------------------------------------------------------#

# what is a byte? it is the smallest unit of information in a computer.
# byte consists of 8 bits, 8 binary digits, zeros/ones
# inside computer memory everything is a byte
# pictures are bytes, videos are bytes, sounds are bytes, texts are sequences of bytes
# encoding is taking the original information and converting it to a sequence of bytes
# decoding is converting sequences of bytes ...
# Unicode is a table of symbols in which each symbol has an abstract number
# text encoding is a way to represent abstract symbol number as a sequence of bytes
# there are a few such encodings
# UTF-8, UTF-16, etc.
# UTF-8 is the most popular
