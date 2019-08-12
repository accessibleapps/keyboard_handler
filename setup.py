from setuptools import setup, find_packages

__version__ = 0.52

setup(
    name="Keyboard_Handler",
    version=__version__,
    description="Hook global and local keystrokes on multiple platforms",
    author="Christopher Toth",
    packages=find_packages(),
    extras_require={
        ':sys_platform == "win32"': ["pywin32",],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries",
    ],
)
