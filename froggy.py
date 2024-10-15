#! /usr/bin/env -vS python
# Shebang note: The env -S option was only needed on Windows in some cases. -v is optional.

import argparse
import os
import time
import yaml
import jinja2


# ###############################################    CONFIGURATION    ##################################################

ABSOLUTE: bool = False  # Default mode is to use only/all relative paths. Set this true when using absolute paths.
# For BASE or any path, always specify ABSOLUTE PATHS beginning with a slash (OS-appropriate delimiter) and ending
# with no slash or delimiter. Simply put, you do not need any trailing slashes anywhere.
# For relative paths, you can simply state a directory name or a . and no starting slash is needed for any relative
# path (nor should there ever be a starting slash for any relative path) and again, you should not include any
# trailing slashes as os.path.join will handle any that might be needed and will do so in the cross-platform way.

INPUT: str = 'input'
OUTPUT: str = 'output'
BASE: str = os.path.join('.', INPUT)
TEMPLATES: str = 'templates'


# ###################################    TYPE DEFINITIONS, GLOBAL INITIALIZATION    ####################################


print('###############################################################')
print('Froggy initializing.')
print(f"Loading jinja2 templates from dir: {TEMPLATES}")
environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES))
tmpl_menu = environment.get_template("menu.txt")
tmpl_item = environment.get_template("item.txt")


# #############################################    CLASS DEFINITIONS    ################################################

class Froggy():
    def __init__(self):
        pass
    # end def Froggy.__init__()  -  #

    def go(self) -> None:
        print('###############################################################')
        print(f"Froggy running at {time.strftime('%c')}")
        for root, dirs, files in os.walk(BASE):
            print(root, "consumes", end=" ")
            print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=" ")
            print("bytes in", len(files), "non-directory files")
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            if 'index.yaml' in files:
                # files.remove('file-to-ignore.txt')  # ignore some things
                print(f"An index.yaml file is present in this dir: {root}")
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


    # end def go()  -  #
# end class Froggy  -  #


# #############################################    FUNCTION DEFINITIONS    #############################################

def ensure_one_trail_slash(pathstr: str) -> str:
    pass
    # If I use os.path, I should not need this.
# end def ensure_one_trail_slash()  -  #


# ###############################################    INITIALIZATION    #################################################



# ################################################    INSTANTIATION    #################################################



# ###############################################    MAIN EXECUTION    #################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='Froggy',
        description='Simple Python+YAML system to generate potentially large hierarchical web content structures ' \
            'suited for static websites.',
        epilog='Text at the bottom of help')




    froggy: Froggy = Froggy()
    froggy.go()
    # Kick it off from here.
    # Not much code will be here.
# end if __name__ main  -  #


###################################################    NOTES    ######################################################


##
#
