from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    '''
    This function returns the list of requirements from a file.
    '''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]
    return requirements

setup(
    name='ML Project',
    version='0.0.1',
    author='Suveer Upasani',
    author_email='suveerupasani@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
