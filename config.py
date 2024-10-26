# config.py

import os


# ###############################################    CONFIGURATION    ##################################################

# Main Settings
ABSOLUTE: bool = False  # Default mode is to use only/all relative paths. Set this true when using absolute paths.
# For BASE or any path, always specify ABSOLUTE PATHS beginning with a slash (OS-appropriate delimiter) and ending
# with no slash or delimiter. Simply put, you do not need any trailing slashes anywhere.
# For relative paths, you can simply state a directory name or a . and no starting slash is needed for any relative
# path (nor should there ever be a starting slash for any relative path) and again, you should not include any
# trailing slashes as os.path.join will handle any that might be needed and will do so in the cross-platform way.

# TODO: If ABSOLUTE is True we can just compose an absolute BASE here. We could re-use the BASE var or add a var.
BASE: str = ''
DEFAULT_INPUT: str = 'input'  # * TODO: Not currently used but likely will be when we add cmd-line option processing.
INPUT = os.path.join(BASE, 'catalogs/world')
OUTPUT: str = 'output'
TEMPLATES: str = 'templates'


# Logging
LOG_INFO: bool = True  # Minimal general info. If all LOG_* below are False, setting this False makes Froggy silent.
LOG_INIT: bool = True  # Early initialization, setup details, possibly from a few phases that occur, mostly at startup.
LOG_SKIPPING_DEBUG: bool = True  # Some steps skip special dirs/files. E.g.: /common/ dir is skipped for YAML parsing.

LOG_DEBUG: bool = True  # Lots of debugging output, but excluding the most extreme full detail, which is excessive.
LOG_TRACE: bool = True  # Extreme detail, possibly excessive logging for most cases but shows nearly complete details.





##
#


# NOTES:

# TODO: This looks like a cool way to apply type-hinting to literal enums like this (constant lists, dicts etc):
# PygameSurfaceFormatType = Union[
#     Literal["P"], Literal["RGB"], Literal["RGBX"], Literal["RGBA"], Literal["ARGB"]
# ]
# USAGE: format: PygameSurfaceFormatType = "RGBA"


##
#
