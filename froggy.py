#! /usr/bin/env -vS python

import argparse
import yaml


# ###############################################    CONFIGURATION    ##################################################

ABSOLUTE: bool = False  # Default mode is to use only/all relative paths. Set this true when using absolute paths.
# For BASE or any path, always specify ABSOLUTE PATHS beginning with a slash (OS-appropriate delimiter) and ending
# with no slash or delimiter. Simply put, you do not need any trailing slashes anywhere.
# For relative paths, you can simply state a directory name or a . and no starting slash is needed for any relative
# path (nor should there ever be a starting slash for any relative path) and again, you should not include any
# trailing slashes as os.path.join will handle any that might be needed and will do so in the cross-platform way.

BASE: str = '.'


# ###################################    TYPE DEFINITIONS, GLOBAL INITIALIZATION    ####################################



# #############################################    CLASS DEFINITIONS    ################################################

class Froggy():
    pass

# #############################################    FUNCTION DEFINITIONS    #############################################



def ensure_one_trail_slash(pathstr: str) -> str:
    pass
    # If I use os.path, I should not need this.

# ###############################################    INITIALIZATION    #################################################



# ################################################    INSTANTIATION    #################################################



# ###############################################    MAIN EXECUTION    #################################################

if __name__ == '__main__':
    froggy: Froggy = Froggy()
    # Kick it off from here.
    # Not much code will be here.
# end if __name__ main  -  #


###################################################    NOTES    ######################################################


##
#
