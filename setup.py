import numpy as np
from setuptools import Extension, setup, find_packages


from config import __authors__
from config.requirements import get_requirements



extensions = [
    Extension(
        "pygame_loads",
        [r"src\utils\pygame_loads.py"],
        include_dirs=[np.get_include()],
    ),
]

setup(
    name="My Little Master",
    version="0.8",
    description="Procedural generation game",
    author=__authors__,  
    url="",
    license="GNU GENERAL PUBLIC LICENSE",
    install_requires=get_requirements(),
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
    ext_modules=extensions,
)