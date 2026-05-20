from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''This function will return the list of requirements'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newlines and whitespace first
        requirements = [req.strip() for req in requirements]
        # Remove empty lines
        requirements = [req for req in requirements if req]
        # Remove '-e .' if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Rushikesh",
    author_email="rushirlandge@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)