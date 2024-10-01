import pathlib
import subprocess

from typing import Tuple


import pytest


file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()


def test_function_only_in_py_file(py_file:pathlib.Path):
    with open(py_file, 'r') as file:
        lines = file.readlines()

    for line in lines:
        line_strip = line.strip()
        if line.startswith('#') or line.startswith('"""') or line.startswith("'''"):
            continue
        elif line.startswith('def ') and line_strip.endswith(':'):
            continue
        elif line.startswith('import ') or (line.startswith('from ') and ' import ' in line):
            continue
        assert line.startswith(' ') or line_strip == '', (
            f"{line} not in any function\n"
            f"{line} 는 어느 함수에도 포함되지 않음"
        )


@pytest.fixture
def git_log() -> Tuple[str]:
    return tuple(
        subprocess.check_output(
            ['git', 'log', '--pretty=format"%h%x09%an%x09%ad%x09%s"'],
            encoding='utf-8'
        ).splitlines()
    )


def test_git_log(git_log:Tuple[str]):
    new_commits = []
    for line in git_log:
        h, n, d, s = line.split('\t')
        if "github-classroom[bot]" != n:
            new_commits.append(line)
    assert new_commits, "No new commits"


if __name__ == "__main__":
    pytest.main([__file__])
