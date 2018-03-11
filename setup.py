from setuptools import setup, find_packages

tests_require = [
    'pytest'
]

setup_args = dict(
    name='ttest',
    version="0.1",
    packages = find_packages(),
    python_requires = ">= 2.7",
    install_requires = [
        'param' # just to have something
    ]
    extras_require = {
        # pip does not support tests_require
        'tests': tests_require
    },
    url = "http://",
    license = "BSD",
    description = "Example"
)


if __name__=="__main__":
    setup(**setup_args)
