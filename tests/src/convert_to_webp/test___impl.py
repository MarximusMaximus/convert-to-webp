#!/usr/bin/env python
# type: ignore[reportPrivateUsage]
# pylint: disable=duplicate-code
"""
tests/src/batteries_forking_included/test___impl.py (batteries-forking-included)
"""

################################################################################
#region Imports

#===============================================================================
#region stdlib

from io import (
    TextIOWrapper                   as io_TextIOWrapper,
)
from os import (
    environ                         as os_environ,
)
from os.path import (
    dirname                         as os_path_dirname,
    join                            as os_path_join,
)
from subprocess import (
    run                             as subprocess_run,
)
from typing import (
    Any,
    List,
    Optional,
    Union,
)

#endregion stdlib
#===============================================================================

#===============================================================================
#region third party

from pytest import (
    mark                            as pytest_mark,
    MonkeyPatch                     as pytest_MonkeyPatch,
    param                           as pytest_param,
    Pytester                        as pytest_Pytester,
)

#endregion third party
#===============================================================================

#===============================================================================
#region ours (internal)

import convert_to_webp.__impl as MODULE_UNDER_TEST

#endregion ours (internal)
#===============================================================================

#endregion Imports
################################################################################

################################################################################
#region Helper Functions

def coerceSubprocessCommandToString(
    *args: Any,
    **kwargs: Any,
) -> Union[str, None]:  # pragma: no cover
    """
    Coerce a subprocess's call into a str.

    Returns:
        Union[str, None]: The subprocess's command as a str if exists, or None.
    """
    cmd: Optional[List[str]] = None
    if (
        len(args) > 0 and
        isinstance(args[0], list)
    ):
        cmd = args[0]
    elif (
        len(kwargs) > 0 and
        "cmd" in kwargs
    ):
        if isinstance(kwargs["cmd"], list):
            cmd = kwargs["cmd"]
        else:
            cmd = [kwargs["cmd"]]

    cmd_str = None
    if isinstance(cmd, list):
        cmd_str = " ".join(cmd)

    return cmd_str

#-------------------------------------------------------------------------------
def get_project_python_path() -> str:
    """
    Get the convert-to-webp conda environment's python path.

    Returns:
        str: convert-to-webp conda environment's python path
    """
    python_path: List[str] = []
    python_path.append(
        os_path_dirname(
            os_environ.get(
                "CONDA_PREFIX",
                "/opt/conda/miniforge/envs/placeholder",
            ),
        ),
    )
    python_path.append("convert-to-webp")
    python_path.append("bin")
    python_path.append("python")
    python_path_str = os_path_join("", *python_path)

    return python_path_str

#endregion Helper Functions
################################################################################

################################################################################
#region __main Tests

class Test___main():
    """
    Tests loading the test suite.
    """

    #-------------------------------------------------------------------------------
    def test___main(self) -> None:
        """
        Tests that the library cannot be invoked directly.
        """
        ret = getattr(MODULE_UNDER_TEST, "__main")([])  # noqa: B009
        assert ret != 0

    #-------------------------------------------------------------------------------
    def test___main__shell_invocation(self) -> None:
        """
        Tests that the library cannot be invoked directly.
        """
        python_path_str = get_project_python_path()

        cmd = [
            python_path_str,
            "./src/batteries_forking_included/__impl.py",
        ]

        p = subprocess_run(cmd, capture_output=True)

        assert p.returncode == 1
        assert b"This module should not be run directly." in p.stderr

#endregion Tests
################################################################################

################################################################################
#region getVersionNumber

#===============================================================================
class Test_getVersionNumber():
    """
    Test getVersionNumber function.
    """

    '''
    def getVersionNumber() -> str:
    '''

    #---------------------------------------------------------------------------
    def test_getVersionNumber_importlib(
        self,
    ) -> None:
        """
        Test getVersionNumber via importlib.
        """

        ret = MODULE_UNDER_TEST.getVersionNumber()

        assert ret != ""
        assert ret != "UNKNOWN"

    #---------------------------------------------------------------------------
    def test_getVersionNumber_pyproject_toml(
        self,
        monkeypatch: pytest_MonkeyPatch,
        pytester: pytest_Pytester,
    ) -> None:
        """
        Test getVersionNumber via pyproject.toml.
        """
        import importlib.metadata  # pylint: disable=import-outside-toplevel

        mock_repo_path = pytester.copy_example(
            os_path_join(
                MODULE_UNDER_TEST.MY_DIR_FULLPATH,
                "template",
            ),
        )
        pytester.makepyprojecttoml("""\
            name = "template"
            version = "0.0.0"
            description = "A template project."
        """)
        monkeypatch.setattr(
            MODULE_UNDER_TEST,
            "MY_REPO_FULLPATH",
            mock_repo_path,
        )

        def mock_importlib_metadata_version(_: str) -> str:
            raise importlib.metadata.PackageNotFoundError
        monkeypatch.setattr(
            MODULE_UNDER_TEST,
            "importlib_metadata_version",
            mock_importlib_metadata_version,
        )

        monkeypatch.delenv("BFI_VERSION", raising=False)

        ret = MODULE_UNDER_TEST.getVersionNumber()

        assert ret != ""
        assert ret != "UNKNOWN"
        assert ret == "0.0.0"

    #---------------------------------------------------------------------------
    def test_getVersionNumber_UNKNOWN(
        self,
        monkeypatch: pytest_MonkeyPatch,
        pytester: pytest_Pytester,
    ) -> None:
        """
        Test getVersionNumber via pyproject.toml.
        """
        import importlib.metadata  # pylint: disable=import-outside-toplevel

        mock_repo_path = pytester.copy_example(
            os_path_join(
                MODULE_UNDER_TEST.MY_DIR_FULLPATH,
                "template",
            ),
        )
        pytester.makepyprojecttoml("""\
            name = "template"
            version = "0.0.0"
            description = "A template project."
        """)
        monkeypatch.setattr(
            MODULE_UNDER_TEST,
            "MY_REPO_FULLPATH",
            mock_repo_path,
        )

        def mock_importlib_metadata_version(_: str) -> str:
            raise importlib.metadata.PackageNotFoundError
        monkeypatch.setattr(
            MODULE_UNDER_TEST,
            "importlib_metadata_version",
            mock_importlib_metadata_version,
        )

        def mock_open(
            f: str,
            mode: str,
            encoding: str = None,
        ) -> io_TextIOWrapper:
            # silence vulture about unused arguments
            f = f  # pylint: disable=self-assigning-variable
            mode = mode  # pylint: disable=self-assigning-variable
            encoding = encoding  # pylint: disable=self-assigning-variable
            raise Exception
        monkeypatch.setitem(
            MODULE_UNDER_TEST.getVersionNumber.__globals__,
            "open",
            mock_open,
        )

        monkeypatch.delenv("BFI_VERSION", raising=False)

        ret = MODULE_UNDER_TEST.getVersionNumber()

        assert ret != ""
        assert ret == "UNKNOWN"

#endregion getVersionNumber
################################################################################

################################################################################
#region convertToWebp

#===============================================================================
class Test_convertToWebp():
    """
    Test convertToWebp function.
    """

    '''
    def convertToWebp() -> int:
    '''

    #---------------------------------------------------------------------------
    @pytest_mark.parametrize(
        (
            "args," +
            "kwargs," +
            "expected"
        ),
        [
            pytest_param(
                [],
                {},
                1,
                id="args0_kwargs0",
            ),
            pytest_param(
                ["asdf"],
                {},
                0,
                id="args1_kwargs0",
            ),
            pytest_param(
                [
                    "asdf",
                    "qwerty",
                ],
                {},
                0,
                id="args2_kwargs0",
            ),
        ],
    )
    def test_convertToWebp_withPosArgs(
        self,
        args,
        kwargs,
        expected,
    ) -> None:
        """
        Test convertToWebp with args.
        """

        ret = MODULE_UNDER_TEST.convertToWebp(*args, **kwargs)

        assert ret == expected

#endregion convertToWebp
################################################################################
