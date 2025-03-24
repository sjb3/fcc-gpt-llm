# From and check requirements.txt
# This is only an example for future references
# From terminal use '$ python3 setup.py develop'

from setuptools import setup, find_packages

setup(
    name='json_formatter',
    version='0.0.1',
    description='Reformats files to stdout',
    install_requirements=['click'],
    entry_point="""
    [console_scripts]
    json_formatter=json_formatter.main:main
    """,
    author='self',
    author_email='non of your biz',
    packages=find_packages(),
)


