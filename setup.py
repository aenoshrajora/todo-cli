import codecs
import os

from setuptools import setup, find_packages


def read(*parts):
    return codecs.open(os.path.join(os.path.abspath(os.path.dirname(__file__)), *parts), 'r').read()


long_description = read('README.md')


setup(
    name='todo',
    version='1.0.0',
    description='Command-line tool to manage Todo lists',
    long_description=long_description,
    keywords='todo list task productivity project management',
    author='Aenosh Rajora',
    author_email='aenoshrajora79@gmail.com',
    url='https://github.com/aenoshrajora/todo-cli',
    license='MIT',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'todo=todo:main'
        ]
    }
)
