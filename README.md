Jupyter Notebook Params
=======================
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/manics/jupyter-notebookparams/master?urlpath=notebooks%2Fexample.ipynb%3Fa%3D1%26b%3D%22whatever%22%26autorun%3Dtrue)

Takes query parameters from a url to update a parameter cell of a jupyter notebook.


Installation
------------

    pip install jupyter-notebookparams

This should automatically enable the extension. If it is not listed in `jupyter nbextension list` install and enable it:

    jupyter nbextension install --py jupyter_notebookparams --sys-prefix
    jupyter nbextension enable --py jupyter_notebookparams --sys-prefix


Usage
-----

Create a notebook cell that starts with the exact string `# Parameters:`
Add parameters to the URL of a notebook, e.g. `http://example.org/notebook.ipynb?a=1&b=False`.
The content of the first cell starting with `# Parameters:` will be replaced with the passed parameters, e.g.

    # Parameters:
    a = 1
    b = False

Add the parameter `autorun=true` to automatically run the notebook.

**WARNING**: This extension does not parse the parameter values so arbitrary code can be executed in the parameter value.
