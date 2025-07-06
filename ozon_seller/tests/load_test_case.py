from typing import Union
import pathlib

from . import qualified_name


_TEST_DATA_DIRECTORY = "test-data"
_TEST_DATA_PATH = pathlib.Path(__file__).parent.joinpath(_TEST_DATA_DIRECTORY)


def load_test_case(test_case_kind: str, test_case_data: Union[object, type[object]]) -> str:
    test_case_filename = f"{test_case_kind}.json"
    test_case_path = _TEST_DATA_PATH.joinpath(
        qualified_name.get_last_module(test_case_data),
        qualified_name.get_qualified_name(test_case_data),
        test_case_filename,
    )

    with open(test_case_path) as test_case_file:
        return test_case_file.read().strip()
