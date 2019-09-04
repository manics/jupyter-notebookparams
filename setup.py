from distutils.core import setup

setup(
    name='jupyter_notebookparams',
    version='0.0.1',
    author='Simon Li',
    author_email='spli@dundee.ac.uk',
    packages=[
        'jupyter_notebookparams',
    ],
    # url='http://pypi.python.org/pypi/TODO/',
    license='MIT',
    package_data={
        'jupyter_notebookparams': ['jupyter_notebookparams/static/main.js'],
    },
    description='Pass URL parameters to a Jupyter notebook',
    long_description=open('README.md').read(),
    install_requires=[
        'notebook>=5.0.0',
    ],
    data_files=[(
            'share/jupyter/nbextensions/jupyter-notebookparams', [
                'jupyter_notebookparams/static/main.js'
        ]),
        ('etc/jupyter/nbconfig/notebook.d' , ['jupyter_notebookparams.json'])
    ],
    zip_safe=False,
    include_package_data=True,
)