# setup.py defines how this project is packaged and installed.
# It specifies metadata (name, version, author) and dependencies.
# Allows installing with "pip install ." or "pip install -e ."
# Makes the project portable, reusable, and easy to distribute as a Python package.



from setuptools import setup, find_packages
from typing import List


HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Reads a requirements file and returns a list of dependencies."""
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements ]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='buhtigexa',
    author_email='mrodriguez@alumnos.unicen.exa.edu.ar',
    packages=find_packages(),
    install_requires=[get_requirements('requirements.txt')],)
