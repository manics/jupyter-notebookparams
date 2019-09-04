Jupyter Notebook Params
=======================

Takes query parameters from a url to create the first cell of a jupyter notebook.

Installation
------------

    pip install .
    jupyter nbextension install --py notebookparams --sys-prefix
    jupyter nbextension enable --py notebookparams --sys-prefix

Usage
-----

Add parameters to the URL of a notebook, e.g. `http://example.org/notebook.ipynb?a=1&b=False`.
The second cell of the notebook will be **created or replaced** with the query parameters from the URL.
Include the parameter `autorun=True` to automatically run the notebook.
