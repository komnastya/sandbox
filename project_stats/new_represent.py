import pathlib

from new_count import CodeStats, by_main_or_test, by_suffix, group_by, scan_files


def represent_new(dir_to_scan):
    all_files = scan_files(dir_to_scan)
    files_group = group_by(all_files, by_suffix)
    # >>> Dict[.py: List[FileCodeStats], .txt: List[FileCodeStats], ... ]

    python_files = files_group.get('.py')  # List[FileCodeStats]
    html_files = files_group.get('.html')
    css_files = files_group.get('.css')
    txt_files = files_group.get('.txt')
    md_files = files_group.get('.md')

    if python_files:
        python_stats = CodeStats.sum([python_file[1] for python_file in python_files])

    w = 12

    def dir_structure():

        if all_files:

            # print directory name
            header = f'structure of {dir_to_scan.name.upper()} directory'
            print(f"\n{header:^{w * 10}}"
                  f"\n{'-' * w * 10}")

            # print header for the table
            print(f"{'Language':^{w}}{'Quantity':^{w}}{'%':^{w}}{'Code lines':^{w}}{'%':^{w}}"
                  f"{'Comment lines':^{w}}{'%':^{w}}{'Empty lines':^{w}}{'%':^{w}}{'Total lines':^{w}}")

            # print directory structure
            if python_files:
                print(f"{'Python':<{w}}{len(python_files):^{w}}{len(python_files) / len(all_files) :^{w}.1%}"
                      f"{python_stats.code_line_count:^{w}}{python_stats.code_percentage:^{w}.1%}"
                      f"{python_stats.comment_line_count:^{w}}{python_stats.comment_percentage:^{w}.1%}"
                      f"{python_stats.empty_line_count:^{w}}{python_stats.empty_percentage:^{w}.1%}"
                      f"{python_stats.total_line_count:^{w}}")
            if html_files:
                print(f"{'HTML':<{w}}{len(html_files):^{w}}{len(html_files) / len(all_files) :^{w}.1%}")
            if css_files:
                print(f"{'CSS':<{w}}{len(css_files):^{w}}{len(css_files) / len(all_files) :^{w}.1%}")
            if txt_files:
                print(f"{'Text':<{w}}{len(txt_files):^{w}}{len(txt_files) / len(all_files) :^{w}.1%}")
            if md_files:
                print(f"{'Markdown':<{w}}{len(md_files):^{w}}{len(md_files) / len(all_files) :^{w}.1%}")
            if all_files:
                print(f"{'Total':<{w}}{len(all_files):^{w}}{len(all_files) / len(all_files) :^{w}.1%}")

        else:
            # print statement which says that directory is empty
            statement = f'There are NOT files in {dir_to_scan.name.upper()} directory'
            print(f"\n{statement:^{w * 10}}"
                  f"\n{'-' * w * 10}\n")

    def python_files_structure():

        if python_files:
            # >>> List[(file_name, CodeStats)]]

            print(f"\n{'PYTHON FILES STRUCTURE':^{w * 10}}")
            print('-' * w * 10)

            print(f"{'File group':^{w}}{'Quantity':^{w}}{'%':^{w}}{'Code lines':^{w}}{'%':^{w}}"
                  f"{'Comment lines':^{w}}{'%':^{w}}{'Empty lines':^{w}}{'%':^{w}}{'Total lines':^{w}}")

            python_files_group = group_by(python_files, by_main_or_test)
            # >>> Dict[main: List[(file_name, CodeStats)], test: List[(file_name, CodeStats)]]

            main_python_files = python_files_group.get('main')
            # List[(file_name, CodeStats)] -> main python files

            test_python_files = python_files_group.get('test')
            # List[(file_name, CodeStats)] -> test python files

            if main_python_files:
                main_stats = CodeStats.sum([main[1] for main in main_python_files])

                print(f"{'Main files':<{w}}{len(main_python_files):^{w}}"
                      f"{len(main_python_files) / len(python_files) :^{w}.1%}"
                      f"{main_stats.code_line_count:^{w}}"
                      f"{main_stats.code_line_count / python_stats.code_line_count:^{w}.1%}"
                      f"{main_stats.comment_line_count:^{w}}"
                      f"{main_stats.comment_line_count / python_stats.comment_line_count:^{w}.1%}"
                      f"{main_stats.empty_line_count:^{w}}"
                      f"{main_stats.empty_line_count / python_stats.empty_line_count:^{w}.1%}"
                      f"{main_stats.total_line_count:^{w}}")

            if test_python_files:
                test_stats = CodeStats.sum([test[1] for test in test_python_files])
                print(f"{'Test files':<{w}}{len(test_python_files):^{w}}"
                      f"{len(test_python_files) / len(python_files) :^{w}.1%}"
                      f"{test_stats.code_line_count:^{w}}"
                      f"{test_stats.code_line_count / python_stats.code_line_count:^{w}.1%}"
                      f"{test_stats.comment_line_count:^{w}}"
                      f"{test_stats.comment_line_count / python_stats.comment_line_count:^{w}.1%}"
                      f"{test_stats.empty_line_count:^{w}}"
                      f"{test_stats.empty_line_count / python_stats.empty_line_count:^{w}.1%}"
                      f"{test_stats.total_line_count:^{w}}")

            print(
                f"{'All files':<{w}}{len(python_files):^{w}}{len(python_files) / len(python_files) :^{w}.1%}"
                f"{python_stats.code_line_count:^{w}}"
                f"{python_stats.code_line_count / python_stats.code_line_count:^{w}.1%}"
                f"{python_stats.comment_line_count:^{w}}"
                f"{python_stats.comment_line_count / python_stats.comment_line_count:^{w}.1%}"
                f"{python_stats.empty_line_count:^{w}}"
                f"{python_stats.empty_line_count / python_stats.empty_line_count:^{w}.1%}"
                f"{python_stats.total_line_count:^{w}}\n")


    dir_structure()
    python_files_structure()

represent_new(pathlib.Path(__file__).parent.parent)
