from setuptools import setup, find_packages

__version__ = 0.52

setup(
    name="Keyboard_Handler",
    version=__version__,
    description="Hook global and local keystrokes on multiple platforms",
    author="Christopher Toth",
    packages=find_packages(),
)
