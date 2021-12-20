import glob
import pathlib
from pathlib import Path
from typing import Callable, Dict, List, Tuple


# Stats just for a single file, for example a PY file.
class FileStats:
    def __init__(self, total_line_count, code_line_count, comment_line_count, empty_line_count):
        self.total_line_count = total_line_count
        self.code_line_count = code_line_count
        self.comment_line_count = comment_line_count
        self.empty_line_count = empty_line_count

    @classmethod
    def sum(entries: List[FileEntry]) -> FileEntry:
        pass


# Type, which combines file name with its stats.
FileEntry = Tuple[
    str,  # File name.
    FileStats  # File stats.
]


def py_stats(path: Path, comment: str) -> FileStats:
    with open(path, 'r', encoding="utf-8") as f:
        total_lines = 0
        empty_lines = 0
        code_lines = 0
        comment_lines = 0
        for line in f.readlines():
            total_lines += 1
            line = line.strip()
            if line == '':
                empty_lines += 1
            elif line.startswith(comment):
                comment_lines += 1
            else:
                code_lines += 1
    return FileStats(total_lines, code_lines, comment_lines, empty_lines)


def txt_stats(path: Path) -> FileStats:
    lines = 0
    with open(path, 'r', encoding="utf-8") as f:
        for _ in f.readlines():
            lines += 1
    return FileStats(lines, 0, 0, 0)


FILE_TYPES = {
    '.py': py_stats,
    '.html': txt_stats,
    '.css': txt_stats,
    '.md': txt_stats,
    '.txt': txt_stats,
}


def scan_files(path: Path) -> List[FileEntry]:
    # For each found file...
    all_files = []
    for entry in glob.glob(f'{path}/**/*', recursive=True):
        stats = FILE_TYPES.get(entry.suffix)
        if stats is not None:
            all_files.append((path.name, stats(path)))
    return all_files


def by_suffix(entry: FileEntry) -> str:
    return Path(entry[0]).suffix


def by_test_not_test(entry: FileEntry) -> str:
    path = Path(entry[0])
    if path.name.endswith('_test.py') or path.name.startswith('test_'):
        return 'test'
    else:
        return 'not_test'


# Groups files and gathers stats about file group
def group_by(entries: List[FileEntry], key_of: Callable[[FileEntry], str]) -> Dict[str, List[FileEntry]]:
    pass


all_files = scan_files(pathlib.Path(__file__).parent.parent)  # all files in sandbox project
by_suffix_dict = group_by(all_files, by_suffix)  # files grouped by file type
py_files = by_suffix_dict['.py']  # python files
py_files_by_test_not_test = group_by(py_files, by_test_not_test)  # python files by test/code
py_code_files = py_files_by_test_not_test['not_test']  # python code files
py_test_files = py_files_by_test_not_test['test']  # python test files
