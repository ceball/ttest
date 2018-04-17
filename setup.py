from setuptools import setup, find_packages

setup_args = dict(
    name='ttest',
    version="0.1",
    packages = find_packages(),
    python_requires = ">= 2.7",
    install_requires = [
        'param'
        # just to have some time consuming stuff to install...
#        'bokeh',
#        'dask',
#        'numba',
#        'pandas',
#        'pillow',
    ],
    extras_require = {
        # pip does not support tests_require
        'tests': [
            'pytest',
        ]
    },
    url = "http://",
    license = "BSD",
    description = "Example"
)


if __name__=="__main__":
    setup(**setup_args)
