import ast
import importlib
import logging
import pathlib
import sys

from typing import Tuple

import pytest

file_path = pathlib.Path(__file__)
test_folder = file_path.parent.absolute()
proj_folder = test_folder.parent.absolute()

sys.path.insert(0, str(proj_folder))


def test_syntax_validity(py_file:pathlib.Path):

    code = py_file.read_text(encoding="utf-8")

    try:
        ast.parse(code)
    except SyntaxError as e:
        pytest.fail(f"Syntax error in file: {py_file.relative_to(proj_folder)}\n{e}")


@pytest.fixture(scope="session")  # Session scope to share the allowed modules across tests
def allowed_modules() -> Tuple[str]:
    return tuple()


def test_allowed_imports(py_file:pathlib.Path, allowed_modules:Tuple[str]):

    code = py_file.read_text(encoding="utf-8")

    tree = ast.parse(code)

    for node in ast.walk(tree):
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            module_name = node.module if isinstance(node, ast.ImportFrom) else node.names[0].name
            if module_name not in allowed_modules:
                pytest.fail(
                    f"Import of disallowed module '{module_name}' in {py_file}\n"
                    f"{py_file.relative_to(proj_folder)} 파일에서 '{module_name}' 모듈을 import 않기 바랍니다."
                )


def has_func_call(file_path:pathlib.Path, func_name:str="input") -> bool:
    '''
    Checks if a Python script contains a call to the 'input' function.
    '''
    with open(file_path, "r") as f:
        tree = ast.parse(f.read())

    result = False  # No input() call found yet

    for node in ast.walk(tree):
        if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == func_name):
            result = True  # Found an input() call
            break
        elif(
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == func_name):
            result = True
        # end if
    # end ast.walk loop

    return result


@pytest.mark.parametrize("func", ["input", "map", "reduce"])
def test_has_func_call(func:str, py_file:pathlib.Path, proj_folder:pathlib.Path):
    try:
        assert has_func_call(
            py_file,
            func_name=func,
        ) == False, (
            f"Please do not call function {func} in file {py_file.relative_to(proj_folder)}.\n"
            f"파일 {py_file.relative_to(proj_folder)} 에서 {input} 를 호출하지 않기 바랍니다.\n"
        )
    except AssertionError as e:
        pytest.fail(str(e.__cause__))
    except Exception as e:
        logging.exception(str(e.__cause__))
        pytest.fail(
            f"Could not check if the script has an {func}() call\n"
            f"스크립트가 {func}() 함수를 호출하는지 확인할 수 없습니다\n"
        )


def test_importable(py_file:pathlib.Path):
    name0 = py_file.name.split('.')[0]
    if name0.startswith('ex'):
        module = importlib.import_module(py_file.name.split('.')[0])
        assert module is not None


if __name__ == "__main__":
    pytest.main([__file__])
