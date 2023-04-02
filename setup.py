from setuptools import find_packages,setup
from typing import List

Hyphen_e="-e ."
def get_requirements(file_path:str)->List[str]:
    requiremnets=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requiremnets]

        if Hyphen_e in requirements:
            requirements.remove(Hyphen_e)
    
    return requirements

setup( 
    name="Regressor",
    version="0.0.1",
    author="Rahul",
    author_email="rrahulsrinivas@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    packages=find_packages()
)