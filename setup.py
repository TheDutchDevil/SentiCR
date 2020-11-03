from setuptools import setup, find_packages

setup(
    name='SentiCR-package',
    version='0.1.0',
    packages=find_packages(include=['SentiCR']),
    install_requires=[
        "nltk",
        "sklearn",
        "xlrd",
        "imblearn"
    ],
    package_data = {'SentiCR': [
                'Contractions.txt',
                'EmoticonLookupTable.txt',
                'Oracle.xlsx']}
)