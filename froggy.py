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
        for node_path, dirs, files in os.walk(INPUT):
            print(node_path, "consumes", end=" ")
            print(sum(os.path.getsize(os.path.join(node_path, name)) for name in files), end=" ")
            print("bytes in", len(files), "non-directory files")
            print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
            if exclude_from_yaml_parse(node_path):
                print(f"Skipping: {node_path}")
                continue
            y_type = wrap_warn_html('----TYPE----')
            y_title = wrap_warn_html('----TITLE----')
            y_description = wrap_warn_html('----DESCRIPTION----')
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
                raise Exception(f"Node dir [{node_path}] is a MENU but does not have any dirs inside it. menu.yaml file "
                                "is present so this MENU dir should contain at least one node dir inside it.")

            if 'menu.yaml' in files and len(dirs) > 0 and not exclude_from_yaml_parse(node_path):
                valid_node = True
                valid_node_type = 'menu'
                self.do_node_menu(node_path, dirs)

            if 'item.yaml' in files and len(dirs) == 0 and not exclude_from_yaml_parse(node_path):
                valid_node = True
                valid_node_type = 'item'
                self.do_node_item(node_path)

            if not valid_node:
                raise Exception(
                    f"Invalid node. [{node_path}] Must be either 'item' or 'menu' type. "
                     "Some criteria was not met."
                )
    # end def go()  -  #

    # TODO: Lacking a better name "do_node" means we parse the YAML, create output dir and possibly HTML, possibly
    #         compose menu sub-content and finally, copy over all content object files.

    def do_node_menu(self, node_path: str, dirs: list[str]) -> None:
        # menu_content: str = generate_menu_content(node_path, dirs)  # Classic: Effective old-school HTML composition
        menu_content: str = render_menu_nav(node_path, dirs)  # Modern: Uses Jinja2 and looping within the template
        yamldoc: str = ''
        # TODO: Load this tmpl once at startup. I just slammed this do_item code in here Q & D. Will completely change.
        with open(os.path.join(node_path, 'menu.yaml'), 'r') as yamlfh:
            yamldoc = yamlfh.read()
        print(yamldoc)
        # TODO: Load YAML and get values. y_type, y_title
        y_type = wrap_warn_html('y_type')
        y_title = wrap_warn_html('y_title')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        outfile_base = os.path.join(BASE, OUTPUT, node_path)
        if not os.path.exists(outfile_base):
            os.makedirs(outfile_base)
        outfile = os.path.join(outfile_base, 'index.html')
        content = gx_tmpl_menu.render(
            type=y_type,
            title=y_title,
            menu_content=menu_content,
        )
        with open(outfile, mode="w", encoding="utf-8") as outfh:
            outfh.write(content)
            print(f"Writing: {outfile}")

    # end def do_node_menu()  -  #

    def do_node_item(self, node_path: str) -> None:
        yamldoc: str = ''
        # TODO: Load this tmpl once at startup. I just slammed this do_item code in here Q & D. Will completely change.
        with open(os.path.join(node_path, 'item.yaml'), 'r') as yamlfh:
            yamldoc = yamlfh.read()
        print(yamldoc)
        # TODO: Load YAML and get values. y_type, y_title, y_description
        y_type = wrap_warn_html('y_type')
        y_title = wrap_warn_html('y_title')
        y_description = wrap_warn_html('y_description')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -')
        outfile_base = os.path.join(BASE, OUTPUT, node_path)
        if not os.path.exists(outfile_base):
            os.makedirs(outfile_base)
        outfile = os.path.join(outfile_base, 'index.html')
        content = gx_tmpl_item.render(
            type=y_type,
            title=y_title,
            description=y_description,
        )
        with open(outfile, mode="w", encoding="utf-8") as outfh:
            outfh.write(content)
            print(f"Writing: {outfile}")

    # end def do_node_item()  -  #
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


def generate_menu_content(node_path: str, dirs: list[str]) -> str:
    c: str = "\n<LIST>\n"
    farleft: str = "<LI>"
    left: str = "<A HREF=\'"
    mid: str = "/index.html\'>"
    right: str = '</A></LI>'
    link_type: str = ''
    link_text: str = ''
    for thisdir in dirs:
        if not exclude_from_yaml_parse(thisdir):
            # TODO: Open each dir and get the title from the YAML.
            # We don't know if the dir is an item or menu. The canonical indicator of my design is the presence of the
            # YAML file of the specific type. (Right now it is one or the other. Later both might be supported.)
            menu_yaml_path = os.path.join(node_path, thisdir, 'menu.yaml')
            item_yaml_path = os.path.join(node_path, thisdir, 'item.yaml')
            if os.path.isfile(menu_yaml_path):
                with open(menu_yaml_path, 'r') as yamlfh:
                    menu_yaml_doc = yamlfh.read()
                print(menu_yaml_doc)
                # TODO: HACK:
                link_text = menu_yaml_doc
                link_type = 'CATEGORY'
            # TODO: At this point in the design there should not be both but we'll code it a little bit to allow both.
            #         Later I might allow both item and menu in a single node but not currently. Still, I'm not going
            #         to code this if-else (exclusionary) I need to see it run and think more about his aspect.
            if os.path.isfile(item_yaml_path):
                with open(item_yaml_path, 'r') as yamlfh:
                    item_yaml_doc = yamlfh.read()
                print(item_yaml_doc)
                # TODO: HACK:
                link_text = item_yaml_doc
                link_type = 'ITEM'

            c += farleft + link_type + left + thisdir + mid + link_text + right + "\n"
    c += "</LIST>\n\n"
    return c


def render_menu_nav(node_path: str, dirs: list[str]) -> str:
    nav_links: list[tuple] = []
    for thisdir in dirs:
        nav_link: tuple = ()
        link_type: str = ''
        link_text: str = ''
        if not exclude_from_yaml_parse(thisdir):
            menu_yaml_path = os.path.join(node_path, thisdir, 'menu.yaml')
            item_yaml_path = os.path.join(node_path, thisdir, 'item.yaml')
            if os.path.isfile(menu_yaml_path):
                with open(menu_yaml_path, 'r') as yamlfh:
                    menu_yaml_doc = yamlfh.read()
                print(menu_yaml_doc)
                # TODO: HACK:
                link_text = menu_yaml_doc
                link_type = 'CATEGORY'
            if os.path.isfile(item_yaml_path):
                with open(item_yaml_path, 'r') as yamlfh:
                    item_yaml_doc = yamlfh.read()
                print(item_yaml_doc)
                # TODO: HACK:
                link_text = item_yaml_doc
                link_type = 'ITEM'
        nav_link = (link_type, node_path, link_text)
        nav_links.append(nav_link)
    return gx_tmpl_links.render(nav_links=nav_links)


# ###############################################    INITIALIZATION    #################################################

print('###############################################################')
print('Froggy initializing.')
print(f"Loading jinja2 templates from dir: {TEMPLATES}")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES))
gx_tmpl_menu = jinja_env.get_template("menu.txt")
gx_tmpl_item = jinja_env.get_template("item.txt")
gx_tmpl_links = jinja_env.get_template("menu-nav-links.txt")
print(f"Jinja templates loaded: {jinja_env.list_templates()}")


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

# Prefixes for global objects/variables:
# gr_ Global object will be primarily or exclusively READ from. Client code will not modify it or not critically/much.
#     For example, in some cases you might have a complex structure, almost 100% READ from, but some small piece of
#     data might be written to, such as an instance ID, but there are no race conditions to worry about.
# gw_ Global object will be WRITTEN to. This implies race conditions. So this is one of the first things to formalize
#     when the time is right.
# gx_ Global object whiich will be executed such as an imported library related object or instance which might do
#     lots of things, but which does not necessarily need to be in global space and can find a tighter local space
#     to call a home later (for better garbage collection and better general practice perhaps.)

##
#
