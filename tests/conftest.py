import pathlib

from typing import Tuple


import pytest


file_path = pathlib.Path(__file__)
test_folder_path = file_path.parent.resolve()
proj_folder_path = test_folder_path.parent.resolve()


def py_files() -> Tuple[pathlib.Path]:
    return tuple(
        filter(
            lambda s:'sample.py' != s.name,
            proj_folder_path.glob('*.py')
        )
    )


def pytest_generate_tests(metafunc):
    if "py_file" in metafunc.fixturenames:
        metafunc.parametrize("py_file", py_files())


@pytest.fixture
def my_test_folder() -> pathlib.Path:
    p = test_folder_path
    assert p.exists()
    assert p.is_dir()
    return p


@pytest.fixture
def proj_folder() -> pathlib.Path:
    p = proj_folder_path
    assert p.exists()
    assert p.is_dir()
    return p


@pytest.fixture
def script_path(proj_folder:pathlib.Path) -> pathlib.Path:
    '''
    Automatically discover ex??.py file
    Force only one ex??.py file in the project folder at the moment
    '''
    exercise_files = tuple(proj_folder.glob('ex*.py'))

    result = None
    if len(exercise_files) == 0:
        raise FileNotFoundError("No Python file starting with 'ex' found in the project folder.")
    elif len(exercise_files) > 1:
        raise ValueError("Multiple Python files starting with 'ex' found in the project folder. Please ensure there is only one.")
    else:
        result = exercise_files[0]

    return result
