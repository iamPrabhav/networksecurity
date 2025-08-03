'''
The setup.py file is an essential part of packaging and distributiing python project, it is used by 
setuptools(distutils in older python versions) to define the configuration of your project,
 such as its metadata , dependencies and more
'''
from setuptools import find_packages,setup
## the find_package will scan through the repo and find __init__.py and consider it as package
from typing import List

def get_requirements() -> List[str]:
    '''
    This function will return list of requirements
    ''' 
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            # read lines from the file
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                ## ignore the empty line and -e.
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print('requirement.txt file not found')    
    return requirement_lst
            
setup(
    name="NetworkSecurity",
    version="0.0.1",
    author_email="prabhavjoshi31@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)