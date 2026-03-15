from setuptools import setup, find_packages

setup(
    name='advanced_calculator',
    version='1.0.0',
    description='A dual-mode advanced calculator CLI tool (Simple & Scientific)',
    author='Your Name',
    packages=find_packages(),
    py_modules=['calculator'],
    install_requires=[
        'colorama',
    ],
    entry_points={
        'console_scripts': [
            'advanced-calculator=calculator:main',
        ],
    },
    include_package_data=True,
    python_requires='>=3.6',
)
