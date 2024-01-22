from setuptools import setup, find_packages
# apikey=AIzaSyCXEwoavVZD14DNMOf-_I6Wtm3QFvFiu34
from typing import List
HIFEN="-e ."
def get_packages(file_path:str)->List[str]:
    """
    This will return a list of functions
    """
    pckages=[]
    with open(file_path) as f:
        packages=f.readlines()
        # remove the escape squence char("\n")
        packages=[pkg.replace("\n","") for pkg in packages]
        if(HIFEN in packages):
            packages.remove(HIFEN)
    return packages

# Set up 
setup(
    name="Gpt Clone",
    version="3.12.0",
    author='Samiullah',
    author_email='sami606713@gmail.com',
    description='Build a end to end project on titanic dataset with complete dash-board and webapp',
    url='https://github.com/Sami606713/Chat_Gpt_Clone.git',
    packages=find_packages(),
    install_requires=get_packages("requrienments.txt")

)
