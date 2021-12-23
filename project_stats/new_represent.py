import pathlib

from new_count import CodeStats, big_ten, by_main_or_test, by_suffix, group_by, scan_files


def represent(dir_to_scan: pathlib.Path) -> None:
    all_files = scan_files(dir_to_scan)
    files_groups = group_by(all_files, by_suffix)
    # >>> Dict[.py: List[FileCodeStats], .txt: List[FileCodeStats], ... ]

    w = 10

    names = {
        '.py': 'Python',
        '.txt': 'Text',
        '.md': 'Markdown',
        '.css': 'CSS',
        '.html': 'HTML',
        'test': 'Test files',
        'main': 'Main files'
    }

    def _print_rows(files_list, by_parameter) -> None:

        files_list_stats = CodeStats.sum([file[1] for file in files_list])
        file_groups = group_by(files_list, by_parameter)

        for group_name, group_files in file_groups.items():

            group_stats = CodeStats.sum([file[1] for file in group_files])

            name = names.get(group_name, group_name)

            if group_stats.total_line_count > 0 and group_stats.code_line_count == \
                    group_stats.comment_line_count == group_stats.empty_line_count == 0:
                print(f"{name:<{w}}{len(group_files):^{w}}{len(group_files) / len(files_list):^{w}.2%}"
                      f"{'':^{w * 6}}"
                      f"{group_stats.plain_text_count:^{w}}{group_stats.plain_text_percentage:^{w}.0%}"
                      f"{group_stats.total_line_count:^{w}}")
            else:
                print(f"{name:<{w}}{len(group_files):^{w}}{len(group_files) / len(files_list):^{w}.2%}"
                      f"{group_stats.code_line_count:^{w}}{group_stats.code_percentage:^{w}.2%}"
                      f"{group_stats.comment_line_count:^{w}}{group_stats.comment_percentage:^{w}.2%}"
                      f"{group_stats.empty_line_count:^{w}}{group_stats.empty_percentage:^{w}.2%}"
                      f"{'':^{w * 2}}"
                      f"{group_stats.total_line_count:^{w}}")

        print(f"\n{'Total':<{w}}{len(files_list):^{w}}{1:^{w}.0%}"
              f"{files_list_stats.code_line_count:^{w}}{'-//-':^{w}}"
              f"{files_list_stats.comment_line_count:^{w}}{'-//-':^{w}}"
              f"{files_list_stats.empty_line_count:^{w}}{'-//-':^{w}}"
              f"{files_list_stats.plain_text_count:^{w}}{'-//-':^{w}}"
              f"{files_list_stats.total_line_count:^{w}}")

    def dir_structure():

        if all_files:

            # print directory name
            header = f'structure of {dir_to_scan.name.upper()} directory'
            print(f"\n{header:^{w * 12}}"
                  f"\n{'-' * w * 12}")

            # print header for the table
            print(f"{'Language':^{w}}{'Quantity':^{w}}{'%':^{w}}{'Code':^{w}}{'%':^{w}}"
                  f"{'Comments':^{w}}{'%':^{w}}{'Empty':^{w}}{'%':^{w}}{'Text':^{w}}{'%':^{w}}"
                  f"{'Total':^{w}}"
                  f"\n{'-' * w * 12}")

            # print directory structure
            _print_rows(all_files, by_suffix)

        else:
            # print statement which says that directory is empty
            statement = f'There are NOT files in {dir_to_scan.name.upper()} directory'
            print(f"\n{statement:^{w * 12}}"
                  f"\n{'-' * w * 12}\n")

    def files_group_structure(files):

        if files:
            # >>> List[(file_name, CodeStats)]]

            print(f"\n{'PYTHON FILES STRUCTURE':^{w * 12}}")
            print('-' * w * 12)

            print(f"{'File group':^{w}}{'Quantity':^{w}}{'%':^{w}}{'Code':^{w}}{'%':^{w}}"
                  f"{'Comments':^{w}}{'%':^{w}}{'Empty':^{w}}{'%':^{w}}{'Text':^{w}}{'%':^{w}}"
                  f"{'Total':^{w}}"
                  f"\n{'-' * w * 12}")

            _print_rows(files, by_main_or_test)

    def ten_biggest_files(files, group_name):

        if files:

            big_10 = big_ten(files)

            header = f'TEN BIGGEST {group_name.upper()} FILES by QUANTITY of CODE LINES'
            print(f"\n{header:^{w * 12}}")
            print("-" * w * 12)

            print(
                f"{'FILE NAME':^{w * 5}}"
                f"{'Code lines':^{w}}{'%':^{w}}"
                f"{'Comments':^{w}}{'%':^{w}}"
                f"{'Empty':^{w}}{'%':^{w}}"
                f"{'Total':^{w}}\n"
                f"{'-' * w * 12}"
            )

            for name, stats in big_10:
                print(f"{pathlib.Path(name).name:<{w * 5}}"
                      f"{stats.code_line_count:^{w}}{stats.code_percentage:^{w}.1%}"
                      f"{stats.code_line_count:^{w}}{stats.comment_percentage:^{w}.1%}"
                      f"{stats.empty_line_count:^{w}}{stats.empty_percentage:^{w}.1%}"
                      f"{stats.total_line_count:^{w}}"
                      )

    dir_structure()
    python_files = files_groups.get('.py')  # List[FileCodeStats]
    files_group_structure(python_files)
    ten_biggest_files(python_files, 'python')
