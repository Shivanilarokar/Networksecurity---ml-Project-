'''
This setup.py file is used to install the package in the local environment.
It is essential part of packaging and distributing python project.
It is used by setuptools (or distutils in older python versions) to define the configuration
of your project. such as its name, version, dependencies, etc. & more

'''

from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:  # Corrected function name and type hint
    """
    This function returns the list of requirements from requirements.txt file.
    """
    requirement_list: List[str] = []
    try:
        with open("requirements.txt", "r") as file:  # Correct file name
            # Read and process each line
            for line in file:
                requirement = line.strip()  # Remove spaces and newlines
                # Ignore empty lines and '-e .'
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("Error: requirements.txt file not found.")
    
    return requirement_list

# Setup function
setup(
    name="Network_security",
    version="0.0.1",
    author="Shivani",
    author_email="shivani95larokar@gmail.com",
    packages=find_packages(),  # Fixed colon issue
    install_requires=get_requirements(),  # Fixed missing comma
)

                                