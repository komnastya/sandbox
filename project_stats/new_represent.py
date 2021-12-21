import pathlib

from new_count import CodeStats, by_suffix, group_by, scan_files


def represent_new(dir_to_scan):
    all_files = scan_files(dir_to_scan)
    files_group = group_by(all_files, by_suffix)
    # >>> Dict[.py: List[FileCodeStats], .txt: List[FileCodeStats], ... ]

    python_files = files_group.get('.py')  # List[FileCodeStats]
    html_files = files_group.get('.html')
    css_files = files_group.get('.css')
    txt_files = files_group.get('.txt')
    md_files = files_group.get('.md')

    python_stats = CodeStats.sum([python_file[1] for python_file in python_files])

    w = 15

    def print_dir_name():
        header = f'structure of {dir_to_scan.name.upper()} directory'
        print(f"\n{header:^{w * 7}}"
              f"\n{'-' * w * 7}")

    def print_header():
        print(f"{'Language':^{w}}{'Quantity':^{w}}{'%':^{w}}{'Code lines':^{w}}"
              f"{'Comment lines':^{w}}{'Empty lines':^{w}}{'Total lines':^{w}}")

    def print_general_dir_structure():
        if python_files:
            print(f"{'Python':<{w}}{len(python_files):^{w}}{len(python_files) / len(all_files) :^{w}.1%}"
                  f"{python_stats.code_line_count:^{w}}{python_stats.comment_line_count:^{w}}"
                  f"{python_stats.empty_line_count:^{w}}{python_stats.total_line_count:^{w}}")
        if html_files:
            print(f"{'HTML':<{w}}{len(html_files):^{w}}{'':^{w}.1%}")
        if css_files:
            print(f"{'CSS':<{w}}{len(css_files):^{w}}{len(css_files) / len(all_files) :^{w}.1%}")
        if txt_files:
            print(f"{'Text files':<{w}}{len(txt_files):^{w}}{len(txt_files) / len(all_files) :^{w}.1%}")
        if md_files:
            print(f"{'Markdown files':<{w}}{len(md_files):^{w}}{len(md_files) / len(all_files) :^{w}.1%}")
        if all_files:
            print(f"{'Total':<{w}}{len(all_files):^{w}}{len(all_files) / len(all_files) :^{w}.1%}")

    print_dir_name()
    print_header()
    print_general_dir_structure()


represent_new(pathlib.Path(__file__).parent.parent)
