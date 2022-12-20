"""
convert-to-webp/__impl.py
"""
################################################################################
#region Python Library Preamble

# we know that the repo path is ./../../ b/c we should be in ./src/<project name>/
import os.path as os_path
MY_DIR_FULLPATH = os_path.dirname(__file__)
MY_REPO_FULLPATH = os_path.dirname(os_path.dirname(MY_DIR_FULLPATH))
del os_path

from logging import (  # noqa: F401
    FATAL                           as logging_FATAL,
    getLogger                       as logging_getLogger,
)
logger = logging_getLogger(__name__)
logger_log = logger.log

#endregion Python Library Preamble
################################################################################

###############################################################################
#region Imports

#===============================================================================
#region stdlib

from importlib.metadata import (
    version                         as importlib_metadata_version,
    PackageNotFoundError            as importlib_metadata_PackageNotFoundError,
)

from os.path import (
    abspath                         as os_path_abspath,
    expanduser                      as os_path_expanduser,
    expandvars                      as os_path_expandvars,
    join                            as os_path_join,
    splitext                        as os_path_splitext,
)
import sys
from typing import (
    Any,
    List,
    Optional,
)

#endregion stdlib
#===============================================================================

#===============================================================================
#region third party

from PIL.Image import (
    open                            as PIL_Image_open,
)

#endregion third party
#===============================================================================

#endregion Imports
################################################################################

################################################################################
#region Public Functions

def convertToWebp(
    *args: Any,
    extras: Optional[List[str]] = None,
    **kwargs: Any,
) -> int:
    """
    Converts list of image filepaths to webp in same folder, replacing existing
    extensions with .webp.

    Args:
        extras (Optional[List[str]], optional): _description_. Defaults to None.

    Returns:
        int: return code
    """
    # silence the "variable not used" complaints in function signature
    if False:  # pylint: disable=using-constant-test
        args = args  # type: ignore[unreachable]  # noqa: F841,E501,B950  # pylint: disable=self-assigning-variable
        kwargs = kwargs  # noqa: F841  # pylint: disable=self-assigning-variable

    if extras is None:
        extras = []

    for x in extras:
        x = os_path_abspath(
            os_path_expandvars(
                os_path_expanduser(
                    x,
                ),
            ),
        )
        no_ext_filepath, _ = os_path_splitext(x)
        out_filepath = f"{no_ext_filepath}.webp"
        img = PIL_Image_open(x).convert("RGB")
        img.save(out_filepath, "WEBP")

    return 0

#-------------------------------------------------------------------------------
def getVersionNumber() -> str:
    """
    Get version number of library.

    Returns:
        _type_: version number as str
    """
    try:
        version = importlib_metadata_version("batteries_forking_included")
    except importlib_metadata_PackageNotFoundError:
        try:
            with open(
                os_path_join(MY_REPO_FULLPATH, "pyproject.toml"),
                "r",
                encoding="utf-8",
            ) as f:
                f_data: List[str] = []
                for _ in range(10):  # pragma: no branch
                    line = f.readline()
                    if line == "":
                        break
                    f_data.append(line)
                f_data = [x for x in f_data if "version = " in x]
                version = f_data[0][len("version = "):]
                version = version[1:-2]
        except Exception:  # pylint: disable=broad-except
            version = "UNKNOWN"

    return version

#endregion Public Functions
################################################################################

################################################################################
#region Private Functions

#-------------------------------------------------------------------------------
def __main(argv: List[str]) -> int:
    """
    Entry point.

    Args:
        argv (list[str]): command line arguments

    Returns:
        int: return code
    """
    # ignore unused vars from func signature
    argv = argv  # pylint: disable=self-assigning-variable

    logger_log(logging_FATAL, "This module should not be run directly.")

    return 1

#endregion Private Functions
################################################################################

################################################################################
#region Immediate

if __name__ == "__main__":  # pragma: no cover
    __ret = __main(sys.argv[1:])  # pylint: disable=invalid-name
    sys.exit(__ret)

#endregion Immediate
################################################################################
