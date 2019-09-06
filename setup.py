from setuptools import setup

setup(
    name='jupyter-notebookparams',
    version='0.0.2',
    author='Simon Li',
    author_email='spli@dundee.ac.uk',
    packages=[
        'jupyter_notebookparams',
    ],
    url='https://github.com/manics/jupyter-notebookparams',
    license='MIT',
    package_data={
        'jupyter_notebookparams': ['jupyter_notebookparams/static/main.js'],
    },
    description='Pass URL parameters to a Jupyter notebook',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'notebook',
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