from setuptools import find_packages, setup

setup(
    name="go2_extreme",
    version="0.1.0",
    description="Extreme RL suite for Unitree Go2 on Isaac Lab",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    install_requires=[
        "torch",
        "gymnasium",
        "hydra-core",
        "omegaconf",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    python_requires=">=3.10",
)
