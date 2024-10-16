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

# TODO: If ABSOLUTE is True we can just compose an absolute BASE here. We could re-use the BASE var or add a var.
BASE: str = '.'
INPUT: str = 'input'
OUTPUT: str = 'output'
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
        outfile: str = ''
        content: str = ''
        project: str = ''
        title: str = ''
        name: str = ''
        directory: str = ''
        description: str = ''
        for root, dirs, files in os.walk(os.path.join(BASE, INPUT)):
            print(root, "consumes", end=" ")
            print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=" ")
            print("bytes in", len(files), "non-directory files")
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            project = wrap_warn_html('----PROJECT----')
            title = wrap_warn_html('----TITLE----')
            name = wrap_warn_html('----NAME----')
            directory = wrap_warn_html('----DIRECTORY----')
            description = wrap_warn_html('----DESCRIPTION----')
            # if 'index.yaml' in files:
            #     # files.remove('file-to-ignore.txt')  # ignore some things
            #     print(f"An index.yaml file is present in this dir: {root}")
            # TODO: Read YAML file here. Wrap it in a try-catch. Don't die but issue an informative WARNING/ERROR.
            #        Also, output a WARNNING/ERROR file in the place of the index.html we could not generate.

            yamldoc: str = ''
            if not exclude_from_yaml_parse(root):
                with open(os.path.join(root, 'index.yaml'), 'r') as yamlfh:
                    yamldoc = yamlfh.read()
                print(yamldoc)

            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            outfile = os.path.join(BASE, OUTPUT, 'index.html')
            content = tmpl_item.render(
                    project=project,
                    title=title,
                    name=name,
                    directory=directory,
                    description=description,
                )
            with open(outfile, mode="w", encoding="utf-8") as outfh:
                outfh.write(content)
                print(f"Writing: {outfile}")

            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')

            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')


    # end def go()  -  #
# end class Froggy  -  #


# #############################################    FUNCTION DEFINITIONS    #############################################

def wrap_warn_html(instr: str) -> str:
    return f"<DIV style='font-weight: bold; color: red;'>--{instr}--</DIV>"
# end def wrap_warn_html()  -  #


def exclude_from_yaml_parse(inpath: str) -> bool:
    path_parts: tuple = os.path.split(inpath)
    if path_parts[-1] == 'common':
        print(f"Skipping 'common' dir, which is not involved in YAML parsing.")
        return True
    else:
        return False
# end def exclude_from_yaml_parse()  -  #


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
