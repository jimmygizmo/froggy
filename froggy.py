#! /usr/bin/env -vS python
# Shebang note: The env -S option was only needed on Windows in some cases. -v is optional.

import argparse
import os
import time
import yaml
import jinja2


# ###############################################    CONFIGURATION    ##################################################

VERBOSE: bool = True

ABSOLUTE: bool = False  # Default mode is to use only/all relative paths. Set this true when using absolute paths.
# For BASE or any path, always specify ABSOLUTE PATHS beginning with a slash (OS-appropriate delimiter) and ending
# with no slash or delimiter. Simply put, you do not need any trailing slashes anywhere.
# For relative paths, you can simply state a directory name or a . and no starting slash is needed for any relative
# path (nor should there ever be a starting slash for any relative path) and again, you should not include any
# trailing slashes as os.path.join will handle any that might be needed and will do so in the cross-platform way.

# TODO: If ABSOLUTE is True we can just compose an absolute BASE here. We could re-use the BASE var or add a var.
BASE: str = ''
DEFAULT_INPUT: str = 'input'
INPUT = os.path.join(BASE, 'catalogs/world')
OUTPUT: str = 'output'
TEMPLATES: str = 'templates'

CLEAN_SLATE: bool = False  # TODO: Not implemented yet. Will allow deletion of all output inside /output/
# Output will be completely cleaned before the start of each Froggy run when this is true. The /output/common/
# directory and it's about file as they come from the repository, will be left in place.


# ###################################    TYPE DEFINITIONS, GLOBAL INITIALIZATION    ####################################

# There are no type definitions or global-level (early) initializations to put here .. yet.


# #############################################    CLASS DEFINITIONS    ################################################

# TODO: The plan is to have an in-memory cache of all input structure data and this will be a tree structure. For this
#         we will use a Node class. Such a cache will concentrate File IO more efficiently to occur in bulk at startup.
class Node:
    def __init__(self):
        pass
    # end def Node.__init__()  -  #

    def somefunc(self):
        pass
    # end def somefunc()  -  #
# end class Node  -  # Nodes of the input tree structure with all info needed for program operation contained in a Node.
#   Whithout building a comprehensive in-memory cache ahead of time, a lot of excessive File IO results and occurs
#   throughout main processing which is not desireable. With the help of Node instances we can move a lot of File IO
#   out of main processing and into a loading/validation phase for the entire input structure. Also, importantly,
#   there are a number of different validations which can only occur when you have all of the input tree data assembled
#   and accessible in memory. This in-memory startup-initialized cache is a proven design pattern used in many
#   applications dealing with a large amount of data and/or critical performance concerns. I think in addition to
#   validations which are only possible with a complete picture of the input structure (after loading into such a
#   cache) there are also valuable features which you can only implement when you can see all of the input structure
#   data at once. What will NOT be loaded into this in-memory cache is bulky digital content. Only parameters and for
#   content (like image or audio files as resource objects inside the item type of node) only file specs and not the
#   actual data. There will be a link list type of YAML file and the full contents of that will be loaded into the
#   cache, but this is a Froggy meta-information file and not user content. Content obhects/resources will be assembled
#   over into the growing/generating output structure by copying and won't need to be in the cache, other than to
#   have their file names/paths and possibly some other specs in the cahce. The cache is for ALL input information
#   and meta information just not any bulky digital content.


class Froggy:
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
        valid_node: bool = False
        valid_node_type: str | None = None
        for root, dirs, files in os.walk(INPUT):
            print(root, "consumes", end=" ")
            print(sum(os.path.getsize(os.path.join(root, name)) for name in files), end=" ")
            print("bytes in", len(files), "non-directory files")
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            project = wrap_warn_html('----PROJECT----')
            title = wrap_warn_html('----TITLE----')
            name = wrap_warn_html('----NAME----')
            directory = wrap_warn_html('----DIRECTORY----')
            description = wrap_warn_html('----DESCRIPTION----')
            ######## SANITY CHECKS:
            valid_node = False
            valid_node_type = None
            if 'item.yaml' in files and 'menu.yaml' in files:
                raise Exception('Cannot have BOTH item.yaml AND menu.yaml in an input node directory. Nodes '
                                'are either an item OR a menu so they will only have ONE of those files.')
            if 'item.yaml' in files and len(dirs) > 0:
                raise Exception('Node dir is an ITEM but has dirs inside it. item.yaml file is present so this'
                                'ITEM dir should contain NO other directories inside it.')
            if 'menu.yaml' in files and len(dirs) == 0:
                raise Exception(f"Node dir [{root}] is a MENU but does not have any dirs inside it. menu.yaml file "
                                "is present so this MENU dir should contain at least one node dir inside it.")
            if 'menu.yaml' in files and len(dirs) > 0:
                valid_node = True
                valid_node_type = 'menu'
            if 'item.yaml' in files and len(dirs) == 0:
                valid_node = True
                valid_node_type = 'item'

            # TODO: This is not the best sanity check logic between here and the below. We can streamline this.
            yamldoc: str = ''

            if not exclude_from_yaml_parse(root):
                if valid_node_type == 'menu':
                    with open(os.path.join(root, 'menu.yaml'), 'r') as yamlfh:
                        yamldoc = yamlfh.read()
                    print(yamldoc)
                elif valid_node_type == 'item':
                    with open(os.path.join(root, 'item.yaml'), 'r') as yamlfh:
                        yamldoc = yamlfh.read()
                    print(yamldoc)
                else:
                    raise Exception("Invalid node_type. Must be either 'item' or 'menu'.")

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
        if VERBOSE:
            print(f"Skipping 'common' dir, which is not a node for YAML parsing and HTML generation. The common "
                  "directory is not actually a node, just a directory for shared images or other resources to live.")
        return True
    else:
        return False
# end def exclude_from_yaml_parse()  -  #


# ###############################################    INITIALIZATION    #################################################

print('###############################################################')
print('Froggy initializing.')
print(f"Loading jinja2 templates from dir: {TEMPLATES}")
environment = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES))
tmpl_menu = environment.get_template("menu.txt")
tmpl_item = environment.get_template("item.txt")


# ################################################    INSTANTIATION    #################################################

froggy: Froggy = Froggy()


# ###############################################    MAIN EXECUTION    #################################################

if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        prog='Froggy',
        description='Simple Python+YAML system to generate potentially large hierarchical web content structures ' \
            'suited for static websites.',
        epilog='Text at the bottom of help')

    froggy.go()
    # Kick it off from here.
    # Not much code will be here.
# end if __name__ main  -  #


###################################################    NOTES    ######################################################


##
#
