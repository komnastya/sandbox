import pathlib
from typing import Dict, List

from new_count import CodeStats, FileCodeStats, by_main_or_test, by_suffix, group_by, scan_files


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

    def _print_rows(files_groups: Dict[str, List[FileCodeStats]], files_lists) -> None:
        groups_stats = CodeStats.sum([file[1] for file in files_lists])

        for group_name, files_list in files_groups.items():

            group_stats = CodeStats.sum([file[1] for file in files_list])

            name = names.get(group_name, group_name)

            if group_stats.total_line_count > 0 and group_stats.code_line_count == \
                    group_stats.comment_line_count == group_stats.empty_line_count == 0:
                print(f"{name:<{w}}{len(files_list):^{w}}{len(files_list) / len(files_lists):^{w}.2%}"
                      f"{'':^{w * 6}}"
                      f"{group_stats.plain_text_count:^{w}}{group_stats.plain_text_percentage:^{w}.0%}"
                      f"{group_stats.total_line_count:^{w}}")
            else:
                print(f"{name:<{w}}{len(files_list):^{w}}{len(files_list) / len(files_lists):^{w}.2%}"
                      f"{group_stats.code_line_count:^{w}}{group_stats.code_percentage:^{w}.2%}"
                      f"{group_stats.comment_line_count:^{w}}{group_stats.comment_percentage:^{w}.2%}"
                      f"{group_stats.empty_line_count:^{w}}{group_stats.empty_percentage:^{w}.2%}"
                      f"{'':^{w * 2}}"
                      f"{group_stats.total_line_count:^{w}}")

        print(f"\n{'Total':<{w}}{len(files_lists):^{w}}{1:^{w}.0%}"
              f"{groups_stats.code_line_count:^{w}}{'-//-':^{w}}"
              f"{groups_stats.comment_line_count:^{w}}{'-//-':^{w}}"
              f"{groups_stats.empty_line_count:^{w}}{'-//-':^{w}}"
              f"{groups_stats.plain_text_count:^{w}}{'-//-':^{w}}"
              f"{groups_stats.total_line_count:^{w}}")

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
            _print_rows(files_groups, all_files)

        else:
            # print statement which says that directory is empty
            statement = f'There are NOT files in {dir_to_scan.name.upper()} directory'
            print(f"\n{statement:^{w * 12}}"
                  f"\n{'-' * w * 12}\n")

    def python_files_structure():
        python_files = files_groups.get('.py')  # List[FileCodeStats]

        if python_files:
            # >>> List[(file_name, CodeStats)]]

            python_stats = CodeStats.sum([python_file[1] for python_file in python_files])

            print(f"\n{'PYTHON FILES STRUCTURE':^{w * 12}}")
            print('-' * w * 12)

            print(f"{'File group':^{w}}{'Quantity':^{w}}{'%':^{w}}{'Code':^{w}}{'%':^{w}}"
                  f"{'Comments':^{w}}{'%':^{w}}{'Empty':^{w}}{'%':^{w}}{'Text':^{w}}{'%':^{w}}"
                  f"{'Total':^{w}}"
                  f"\n{'-' * w * 12}")

            python_files_group = group_by(python_files, by_main_or_test)
            _print_rows(python_files_group, python_files)

    dir_structure()
    python_files_structure()
