#! false
# pylint: disable=duplicate-code
"""
tests/src/convert_to_webp/bin/test_bin.py (convert_to_webp)
"""

################################################################################
#region Imports

#===============================================================================
#region stdlib

# import sys
from os import (
    environ                         as os_environ,
)
from os.path import (
    dirname                         as os_path_dirname,
    join                            as os_path_join,
)
from subprocess import (  # nosec
    run                             as subprocess_run,
)
from typing import (
    Any,
    Dict,
    List,
)

#endregion stdlib
#===============================================================================

#===============================================================================
#region third party

from pytest import (
    mark                            as pytest_mark,
    MonkeyPatch                     as pytest_MonkeyPatch,
    param                           as pytest_param,
)

#endregion third party
#===============================================================================

#===============================================================================
#region ours (internal)


#endregion ours (internal)
#===============================================================================

#endregion Imports
################################################################################

################################################################################
#region Helper Functions

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
#region Command Line

#===============================================================================
class Test_CommandLine():
    """
    Invoke via command line.
    """

    #----------------------------------bfi-----------------------------------------
    @pytest_mark.parametrize(
        (
            "extra_args," +
            "expected_ret," +
            "expected_stdout," +
            "not_expected_stdout"
        ),
        [
            pytest_param(
                [],
                2,
                [
                    b"usage:",
                    b"batteries-forking-included",
                ],
                [
                    b"Error: SUBCOMMAND required.",
                ],
                id="no_args",
            ),
            pytest_param(
                ["--help"],
                0,
                [
                    b"usage:",
                    b"batteries-forking-included",
                ],
                [
                    b"Error: SUBCOMMAND required.",
                ],
                id="args_help",
            ),
            pytest_param(
                ["--version"],
                0,
                [
                    b"batteries-forking-included",
                ],
                [
                    b"usage:",
                    b"Error: SUBCOMMAND required.",
                ],
                id="args_version",
            ),
            pytest_param(
                ["run", "echo", "foo"],
                0,
                [
                    b"Executing:",
                    b"run.sh echo foo",
                    b"Executing: /usr/bin/env echo foo",
                ],
                [
                    b"usage:",
                    b"Error: SUBCOMMAND required.",
                ],
                id="args_echo_foo",
            ),
        ],
    )
    def test_commandLine(
        self,
        extra_args: List[str],
        expected_ret: int,
        expected_stdout: List[bytes],
        not_expected_stdout: List[bytes],
        monkeypatch: pytest_MonkeyPatch,
    ) -> None:
        """
        Invoke command line with different args.
        """
        monkeypatch.delenv("_IS_UNDER_TEST", raising=False)

        python_path_str = get_project_python_path()

        cmd = [
            python_path_str,
            "./bin/convert-to-webp.py",
        ]
        cmd = cmd + extra_args
        env: Dict[str, Any] = {
        }
        for k, v in os_environ.items():
            env[k] = v
        p = subprocess_run(cmd, capture_output=True, env=env)

        assert p.returncode == expected_ret
        for x in expected_stdout:
            assert x in p.stdout
        for x in not_expected_stdout:
            assert x not in p.stdout

#endregion Command Line
################################################################################
