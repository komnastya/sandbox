from __future__ import annotations

import glob
from pathlib import Path
from typing import Callable, Dict, List, Tuple


class CodeStats:
    def __init__(self, total_line_count: int, code_line_count: int, comment_line_count: int, empty_line_count: int):
        self.total_line_count = total_line_count
        self.code_line_count = code_line_count
        self.comment_line_count = comment_line_count
        self.empty_line_count = empty_line_count
        if self.total_line_count:
            self.code_percentage = self.code_line_count / self.total_line_count
            self.comment_percentage = self.comment_line_count / self.total_line_count
            self.empty_percentage = self.empty_line_count / self.total_line_count
        else:
            self.code_percentage = 0
            self.comment_percentage = 0
            self.empty_percentage = 0

    @classmethod
    def sum(cls, entries: List[CodeStats]) -> CodeStats:
        total_lines = 0
        code_lines = 0
        comment_lines = 0
        empty_lines = 0
        for entry in entries:
            total_lines += entry.total_line_count
            code_lines += entry.code_line_count
            comment_lines += entry.comment_line_count
            empty_lines += entry.empty_line_count
        return CodeStats(total_lines, code_lines, comment_lines, empty_lines)

    def __str__(self):
        w = 10
        return f"{'-' * 50}\n" \
               f"{'Total lines':<{w * 2}}{self.total_line_count:<{w}}{'100%':<{w}}\n" \
               f"{'Code lines':<{w * 2}}{self.code_line_count:<{w}}{self.code_percentage:<{w}.1%}\n" \
               f"{'Comment lines':<{w * 2}}{self.comment_line_count:<{w}}{self.comment_percentage:<{w}.1%}\n" \
               f"{'Empty lines':<{w * 2}}{self.empty_line_count:<{w}}{self.empty_percentage:<{w}.1%}\n" \
               f"{'-' * 50}"


# Type, which combines file name with its stats.
FileCodeStats = Tuple[
    str,  # File name.
    CodeStats  # Code stats.
]


def py_stats(path: Path) -> CodeStats:
    with open(path, 'r', encoding="utf-8") as f:
        lines = 0
        empty_lines = 0
        code_lines = 0
        comment_lines = 0
        for line in f.readlines():
            lines += 1
            line = line.strip()
            if line == '':
                empty_lines += 1
            elif line.startswith('#'):
                comment_lines += 1
            else:
                code_lines += 1
    return CodeStats(lines, code_lines, comment_lines, empty_lines)


def txt_stats(path: Path) -> CodeStats:
    lines = 0
    with open(path, 'r', encoding="utf-8") as f:
        for _ in f.readlines():
            lines += 1
    return CodeStats(lines, 0, 0, 0)


FILE_TYPES = {
    '.py': py_stats,
    '.html': txt_stats,
    '.css': txt_stats,
    '.md': txt_stats,
    '.txt': txt_stats,
}


def scan_files(dir: Path) -> List[FileCodeStats]:
    result = []
    for entry in glob.glob(f'{dir}/**/*', recursive=True):
        path = Path(entry)
        stats = FILE_TYPES.get(path.suffix)
        if stats is not None:
            result.append((str(path), stats(path)))
    return result


def by_suffix(entry: FileCodeStats) -> str:
    return Path(entry[0]).suffix


def by_main_or_test(entry: FileCodeStats) -> str:
    path = Path(entry[0])
    if path.name.endswith('_test.py') or path.name.startswith('test_'):
        return 'test'
    else:
        return 'main'


# Groups files and gathers stats about file group
def group_by(entries: List[FileCodeStats], key_of: Callable[[FileCodeStats], str]) -> Dict[str, List[FileCodeStats]]:
    data: Dict[str, List[FileCodeStats]] = dict()
    for entry in entries:
        key = key_of(entry)
        if not data.get(key):
            data[key] = [entry]
        else:
            data[key].append(entry)
    return data


def python_biggest_ten(files: List[FileCodeStats]) -> List[FileCodeStats]:
    return sorted(files, key=lambda file_data: file_data[1].code_line_count, reverse=True)[:10]
