# froggy
Simple Python+YAML system to generate potentially large hierarchical web content structures suited for static websites.
Such sites (web content structures) are outstanding for things like SEO or locally-browsable (serverless) sites.
There is no simpler system to generate and organize large amounts of content from friendly YAML files.

Why 'froggy'? Froggy is named after cute little tree frogs who navigate trees extremely well and live simple, elegant
lives. Informational content also comes in the form of a tree. Froggy the program is also simple and elegant while
being very powerful in translating potentially large hierarchies (trees) into your desired content. My favorite tree
frog is the California Sierran Tree Frog and a handful of them climb around my yard every night.

## Setup

I strongly recommend using PyEnv for your Python virtual environment. There is already a .python-version file in place
for PyEnv to use.
Name your Virtual Environment (using PyEnv Virtualenv) and call it:

ve.froggy

I am developing under Python 3.12.7, the latest as of October 2024 and if you want to match the same version, you would
install Python 3.12.7 into PyEnv and then you would create your virtual env like this:

    pyenv virtualenv 3.12.7 ve.froggy

As a first step to any and all virtual environments, please update your pip and setuptools like this:

    pip install --upgrade setuptools
    pip install --upgrade pip

Then you have two options, you can install simply the latest version of all modules like this:

    pip install -r requirements.txt

or you can install the exact versions I am developing and testing with like this:

    pip install -r pinned-requirements.txt

(This is the 'version-pinned' file. If you want the versions guaranteed to test good.
But the latest versions of everything will almost always work great for most apps so I recommend just using
the requirements.txt file.)

Again, this project includes a PyEnv .python-version file containing the name of the virtual environment 've.froggy'
so as soon as PyEnv creates this virtual env, it will show as active (assuming you have a nice prompt 'like oh my zsh'.
Your IDE like PyCharm or VSCode should also show the VE active status but you might have to re-launch and you
might have to manually configure the VE inside your IDE. In my case, I had the VE active before opening the project
in PyCharm for the first time and it automatically picked up the PyEnv VE. Slick!)

## Usage

Create your source directory structure with its root directory as the /input/ directory already in this project.
This means your home page or the root of the rest of your content would be directly inside /input/.
You need not and should not make a new single root under /input/ unless you have some special case.

Your generated content will logically have its root at /output/ and depending on your other parameters,
you should generally be able to start browsing your content at your home or index (root) page by opening the /output/
directory in your web browser.

TODO: Go into details about each node here. ... 

Now you can run froggy with a variety of options or in default mode, when positioned in the project directory root,
by simply typing:

    ./froggy.py
    or
    python ./froggy.py

The default mode of operation is the simplest and typically the most useful mode for a large number of users. In
the defauly mode, the /input/ structure is turned into a static website navigable without a webserver, rooted at
the base directory of /output/. The links are relative filesystem-compatible URLs. This content format might also
work great when simply put in place in a web servers document structure and if not, then some simple command-line
options can enable this. Many common use-cases are covered through the application of simple command-line options.




## Design

Froggy uses the standard library os module for directory walking and file path manipulation because this allows great
cross-platform compatibility. For the template engine,

Jinja2 is used allowing compatibility with many existing sites/templates and allowing an existing workflow to easily
incorporate froggy, possibly to generate large SEO-potent hierarchies of content in a site that might be mostly dynamic
and experiencing SEO challenges.

YAML is the most human-friendly language for encasulating potentially complex structured data in an extremely readable
and easily-editable/maintainable format. YAML can be used an an excellent, human-accessible, serialization format for
essentially any kind of data. YAML is a lot like JSON but even much friendlier. YAML is all about letting humands
easily see, understand and get their hands on and edit potentially complex data. This data is usually in a text format,
but you can easily encode and mix some binary data in with your human-readable text data in your YAML. A lot of systems
benefit from having the primary data accessible, even if most operations are automated, most of the time. The usage of
JSON and YAML can be intermixxed with translations back and forth as part of an integration strategy between sub-systems
where one also benefits from the increased accessibility of YAML. JSON is of course ubiquitiously used and dominant in
web backends and other areas, so expect to go back and forth between YAML and JSON frequently. There can be small
edge case issues in such translations and related conversions, en/de-coding, but the issues are minor. Most use cases
for Froggy will likely involve simpler schemas meaning fewer fields and a simple YAML data structure. Froggy can
however support any complexity level in the data or the hierarchy structure as simple/basic principles aways apply and
the design of froggy is traditional, best-practice, intuitive with good default behaviors and simple/logical options
to enable complex behavior. Froggy can be integrated in to complex automated site generateion workflows as an early,
intermediate or final content generation/publishing step.



#### Jinja2
https://pypi.org/project/Jinja2/



#### Jinja2 Documentation
https://jinja.palletsprojects.com/en/3.1.x/



#### PyYAML Documentation
https://pypi.org/project/PyYAML/



#### PyYAML Documentation
https://pyyaml.org/wiki/PyYAMLDocumentation



#### os.path, os.walk Documentation
https://docs.python.org/3/library/os.path.html

https://docs.python.org/3/library/os.html#os.walk



#### argparse Documentation
https://docs.python.org/3/library/argparse.html



