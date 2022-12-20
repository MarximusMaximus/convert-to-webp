#! false
# pylint: disable=duplicate-code
"""
tests/src/batteries_forking_included/test___main__.py (batteries-forking-included)
"""

################################################################################
#region Imports

#===============================================================================
#region stdlib

from os import (
    environ                         as os_environ,
)
from os.path import (
    abspath                         as os_path_abspath,
    dirname                         as os_path_dirname,
    expanduser                      as os_path_expanduser,
    join                            as os_path_join,
    relpath                         as os_path_relpath,
)
from subprocess import (
    run                             as subprocess_run,
)
from typing import (
    Any,
    List,
    Dict,
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

from convert_to_webp import (
    __main__                          as MODULE_UNDER_TEST,
)

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
#region Command Line Tests

class Test_CommandLine():
    """
    Invoke via command line.
    """

    #-------------------------------------------------------------------------------
    def test_CommandLine_Version_FromRepoRoot(self) -> None:
        """
        Invoke from repo root.
        """
        cwd = MODULE_UNDER_TEST.MY_REPO_FULLPATH

        python_path_str = get_project_python_path()

        script_path_str = os_path_join(
            ".",
            os_path_relpath(MODULE_UNDER_TEST.MY_DIR_FULLPATH, cwd),
            "__main__.py",
        )

        cmd = [
            python_path_str,
            script_path_str,
            "--version",
        ]

        env: Dict[str, Any] = {
        }
        for k, v in os_environ.items():
            env[k] = v

        p = subprocess_run(cmd, capture_output=True, cwd=cwd, env=env)

        assert p.returncode == 0

    #-------------------------------------------------------------------------------
    def test_CommandLine_Version_FromSrc(self) -> None:
        """
        Invoked from src dir.
        """
        cwd = os_path_abspath(os_path_join(MODULE_UNDER_TEST.MY_DIR_FULLPATH, ".."))

        python_path_str = get_project_python_path()

        script_path_str = os_path_join(
            ".",
            os_path_relpath(MODULE_UNDER_TEST.MY_DIR_FULLPATH, cwd),
            "__main__.py",
        )

        cmd = [
            python_path_str,
            script_path_str,
            "--version",
        ]

        env: Dict[str, Any] = {
        }
        for k, v in os_environ.items():
            env[k] = v

        p = subprocess_run(cmd, capture_output=True, cwd=cwd, env=env)

        assert p.returncode == 0

    #-------------------------------------------------------------------------------
    def test_CommandLine_Version_FromSrcMod(self) -> None:
        """
        Invoked from it's own dir.
        """
        cwd = MODULE_UNDER_TEST.MY_DIR_FULLPATH

        python_path_str = get_project_python_path()

        cmd = [
            python_path_str,
            "./__main__.py",
            "--version",
        ]

        env: Dict[str, Any] = {
        }
        for k, v in os_environ.items():
            env[k] = v

        p = subprocess_run(cmd, capture_output=True, cwd=cwd, env=env)

        assert p.returncode == 0

    #-------------------------------------------------------------------------------
    def test_CommandLine_Version_FromHome(self) -> None:
        """
        Invoked from home dir.
        """
        cwd = os_path_expanduser("~")

        python_path_str = get_project_python_path()

        script_path_str = os_path_join(
            MODULE_UNDER_TEST.MY_DIR_FULLPATH,
            "__main__.py",
        )

        cmd = [
            python_path_str,
            script_path_str,
            "--version",
        ]

        env: Dict[str, Any] = {
        }
        for k, v in os_environ.items():
            env[k] = v

        p = subprocess_run(cmd, capture_output=True, cwd=cwd, env=env)

        assert p.returncode == 0

    #-------------------------------------------------------------------------------
    def test_CommandLine_RunEchoFoo_FromRepoRoot(
        self,
        mock_repo: str,
    ) -> None:
        """
        Invoke from repo root.
        """
        python_path_str = get_project_python_path()

        script_path_str_str = os_path_join(
            ".",
            "src",
            "batteries_forking_included",
            "__main__.py",
        )

        cmd = [
            python_path_str,
            script_path_str_str,
            "run",
            "echo",
            "foo",
        ]

        env: Dict[str, Any] = {
        }
        for k, v in os_environ.items():
            env[k] = v

        p = subprocess_run(cmd, capture_output=True, cwd=mock_repo, env=env)

        assert p.returncode == 0

#endregion Tests
################################################################################

################################################################################
#region __main Tests

#===============================================================================
class Test___main():
    """
    _summary_
    """

    #---------------------------------------------------------------------------
    @pytest_mark.parametrize(
        (
            "extra_args," +
            "expected_ret"
        ),
        [
            pytest_param(
                [],
                0,
                id="args0",
            ),
            pytest_param(
                ["asdf"],
                0,
                id="args1",
            ),
            pytest_param(
                [
                    "asdf",
                    "qwerty",
                ],
                0,
                id="args2",
            ),
        ],
    )
    def test___main(
        self,
        monkeypatch: pytest_MonkeyPatch,
        extra_args: List[str],
        expected_ret: int,
    ) -> None:
        """
        _summary_
        """
        def mock_func(
            extras: List[str],
            *args: Any,
            **kwargs: Any,
        ) -> int:
            # ignore unused vars in function signature
            args = args  # noqa: F841  # pylint: disable=self-assigning-variable
            kwargs = kwargs  # noqa: F841  # pylint: disable=self-assigning-variable

            expected_extras = extra_args[1:]
            assert extras == expected_extras

            return expected_ret

        monkeypatch.setattr(
            MODULE_UNDER_TEST,
            "convert_to_webp_convertToWebp",
            mock_func
        )

        __main = getattr(MODULE_UNDER_TEST, "__main")  # noqa: B009
        try:
            ret = __main(extra_args)
        except SystemExit as e:  # pragma: no cover
            ret = e.code
            pass

        assert ret == expected_ret

#endregion __main Tests
################################################################################
