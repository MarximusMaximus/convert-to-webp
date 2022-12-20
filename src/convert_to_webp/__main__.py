"""\
convert-to-webp/__main__
"""

################################################################################
#region __main__.py Preamble

# insert our repo base dir into the sys.path so that we can import our library
# we know that the repo path is ./../.. b/c we should be in ./src/<project name>/
import sys
import os
import os.path as os_path
MY_DIR_FULLPATH = os_path.dirname(__file__)
MY_REPO_FULLPATH = os_path.dirname(os_path.dirname(MY_DIR_FULLPATH))
sys.path.insert(0, MY_REPO_FULLPATH)
MY_LIB_FULLPATH = os_path.join(MY_REPO_FULLPATH, "src")
sys.path.insert(0, MY_LIB_FULLPATH)

MY_PROGRAM_NAME = os.environ.get("BFI_ORIGINAL_EXEC_NAME", os_path.basename(sys.argv[0]))
if (  # pragma: no cover
    "." not in os_path.basename(MY_PROGRAM_NAME) or
    ".py" in os_path.basename(MY_PROGRAM_NAME)
):
    MY_PROGRAM_NAME = os_path.basename(MY_PROGRAM_NAME)  # type: ignore[reportConstantRedefinition]  # noqa: E501,B950  # pragma: no cover
del os
del os_path

#endregion __main__.py Preamble
################################################################################


################################################################################
#region Imports

#===============================================================================
#region stdlib

import argparse
from typing import (
    List,
)

#endregion stdlib
#===============================================================================

#===============================================================================
#region ours (internal)

from convert_to_webp import (
    convertToWebp                   as convert_to_webp_convertToWebp,
    getVersionNumber                as convert_to_webp_getVersionNumber,
)

#endregion ours (internal)
#===============================================================================

#endregion Imports
################################################################################

################################################################################
#region Constants


#endregion Constants
################################################################################

################################################################################
#region Subcommands



#endregion Subcommands
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
    # do argparse stuff
    version = convert_to_webp_getVersionNumber()

    parser = argparse.ArgumentParser(
        prog=MY_PROGRAM_NAME,
        description=f"convert-to-webp {version}",
    )
    _ = parser.add_argument(
        "--version",
        action="version",
        version=f"convert-to-webp {version}",
    )

    options, extras = parser.parse_known_args(argv)

    ret = convert_to_webp_convertToWebp(extras=extras, **vars(options))

    # exit with useful code
    return ret

#endregion Private Functions
################################################################################

################################################################################
#region Script Entry Point

def scriptEntryPoint() -> None:  # pragma: no cover
    """
    Script entry point. Used by tool.poetry.scripts.

    Returns:
        int: return code
    """
    ret = __main(sys.argv[1:])
    sys.exit(ret)

#endregion Script Entry Point
################################################################################

################################################################################
#region Immediate

if __name__ == "__main__":  # pragma: no cover
    scriptEntryPoint()

#endregion Immediate
################################################################################
