import glob
import pathlib


# Write a python script which does the following:
# Scans all python files in this projects +
# For each such file counts the number of text lines in it +
# Prints the sum of all lines in all files in current project +
# Count all lines, even empty ones +
# Prints 10 files with the most line count +
# Rewrite function using glob module +


def count_lines(path):
    empty_total = 0
    comments_total = 0
    code_total = 0
    python_files = 0

    mapping = set()

    for entry in glob.glob(f'{path}/**/*.py', recursive=True):
        python_files += 1

        with open(entry, 'r', encoding="utf-8") as f:
            code_inside = 0
            comment_inside = 0
            empty_inside = 0

            for line in f.readlines():
                line = line.strip()
                if line == '':
                    empty_inside += 1
                elif line.startswith('#'):
                    comment_inside += 1
                else:
                    code_inside += 1

            empty_total += empty_inside
            comments_total += comment_inside
            code_total += code_inside

            mapping.add((code_inside, sum((empty_inside, comment_inside, code_inside)), pathlib.Path(entry).name))

    biggest_ten = [item for item in sorted(mapping, reverse=True)[:10]]

    return path, empty_total, comments_total, code_total, python_files, biggest_ten

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
