# froggy
Simple Python+YAML system to generate potentially large hierarchical web content structures suited for static websites. Such sites (web content structures) are outstanding for things like SEO or locally-browsable (serverless) sites. There is no simpler system to generate and organize large amounts of content from friendly YAML files.

Why 'froggy'? Froggy is named after cute little Tree Frogs who navigate trees extremely well and live simple, elegant lives. Informational content also comes in the form of a tree. Froggy the program is also simple and elegant as well as very powerful in translating potentially large hierarchies (trees) into your desired format.

## Usage

Create your source directory structure with its root directory as the /input/ directory already in this project. This means your home page or the root of the rest of your content would be directly inside /input/.
You need not and should not make a new single root under /input/ unless you have some special case.

Your generated content will logically have its root at /output/ and depending on your other parameters, you should generally be able to start browsing your content at your home or index (root) page by opening the /output/ directory in your web browser.

Each node in the 'tree' (froggy is named after the California Tree Frogs who navigate trees extremely well) 


## Setup
I strongly recommend using PyEnv for your Python virtual environment. There is already a .python-version file in place for PyEnv to use.
Name you Virtual Environment (using PyEnv Virtualenv) and call it:

ve.froggy

