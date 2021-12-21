import glob
from pathlib import Path


def count_lines(path):
    data = {
        'path': path,
        'all_files': 0,
        'total_code': 0,
        'total_comments': 0,
        'total_empty': 0,

        'python_files': 0,
        'python_test_files': 0,
        'python_code_files': 0,
        'all_lines_in_python_files': 0,
        'code_lines_in_python_files': 0,
        'comment_lines_in_python_files': 0,
        'empty_lines_in_python_files': 0,
        'python_ten_biggest_by_code_lines': None,

        'txt_files': 0,

        'md_files': 0,

        'html_files': 0,
        'ten_biggest_html_files': 0,

        'css_files': 0,
        'ten_biggest_css_files': 0,

        'zip_files': 0,

        'other_files': 0
    }
    _all_python_files = set()

    for entry in glob.glob(f'{path}/**/*', recursive=True):
        data['all_files'] += 1

        p = Path(entry)

        if p.name.endswith('py'):
            data['python_files'] += 1

            if p.name.endswith('_test.py') or p.name.startswith('test_'):
                data['python_test_files'] += 1
            else:
                data['python_code_files'] += 1

            with open(entry, 'r', encoding="utf-8") as f:
                code_inside = 0
                comment_inside = 0
                empty_inside = 0
                total_inside = 0

                for line in f.readlines():
                    total_inside += 1
                    line = line.strip()
                    if line == '':
                        empty_inside += 1
                        data['total_empty'] += 1
                    elif line.startswith('#'):
                        comment_inside += 1
                        data['total_comments'] += 1
                    else:
                        code_inside += 1
                        data['total_code'] += 1

                data['code_lines_in_python_files'] += code_inside
                data['comment_lines_in_python_files'] += comment_inside
                data['empty_lines_in_python_files'] += empty_inside
                data['all_lines_in_python_files'] += total_inside

                _all_python_files.add((code_inside, comment_inside, empty_inside, total_inside, p.name))

        elif p.name.endswith('.txt'):
            data['txt_files'] += 1
        elif p.name.endswith('.md'):
            data['md_files'] += 1
        elif p.name.endswith('.html'):
            data['html_files'] += 1
        elif p.name.endswith('.css'):
            data['css_files'] += 1
        elif p.name.endswith('.zip'):
            data['zip_files'] += 1
        else:
            data['other_files'] += 1

    data['python_ten_biggest_by_code_lines'] = [item for item in sorted(_all_python_files, reverse=True)[:10]]
    data['all_files'] = data['all_files'] - data['other_files']
    return data
