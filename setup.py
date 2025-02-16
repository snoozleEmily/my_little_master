import numpy as np
from setuptools import Extension, setup, find_packages


extensions = [
    Extension(
        "pygame_loads",
        [r"src\utils\pygame_loads.py"],
        include_dirs=[np.get_include()],
    ),
]

setup(
    name="My Little Master",
    version="1.2", # Change before updating
    description="Turn-based management game.",
    authors="snoozleEmily" "jluizcalonio",
    url="https://github.com/snoozleEmily/smy_little_master",
    # license="GNU GENERAL PUBLIC LICENSE", qual vamos usar ????
    install_requires=[
        "numpy>=1.18.0",
        "pygame>=2.0.0",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)
