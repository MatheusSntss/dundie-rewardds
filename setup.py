#setuptools
import os
from setuptools import setup, find_packages

def read(*path):
    rootpath = os.path.dirname(__file__)
    filepath = os.path.join(rootpath,*path)
    with open (filepath)as file_:
        return file_.read().strip()
    
def read_requirements(path):
    return[
        line.strip()
        for line in read(path).split("\n")
        if not line.startwith("#","git",'"',"-")
    ]


setup(
    name = "dundie",
    version= "0.2.0",
    description="Rewards Point System for Dunder Mifflin",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Matheus",
    packages=find_packages(),
    entry_points={
        "console_scripts":[
            "dundie = dundie.__main__:main"
        ]
    },
    install_requires=read_requirements("requeriments.txt"),
    extra_requires={
        "test":read_requirements("requeriments.test.txt"),
        "dev": read_requirements("requeriments.dev.txt")
    }
)
