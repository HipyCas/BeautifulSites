import setuptools
import os

# Open and read README.md
with open("README.md", "r") as fh:
    long_description = fh.read()

# Open and read requirements.txt
baseDir = os.path.dirname(os.path.realpath(__file__))
requirements_path = baseDir + '/requirements.txt'
install_requires = []
if os.path.isfile(requirements_path):
    with open(requirements_path, 'r') as f:
        install_requires = f.read().splitlines()

setuptools.setup(
    name="BeautifulSites4",
    version="1.1.1-alpha",
    author="HipyCas",
    author_email="hipycas+python@gmail.com",
    description="An implementation of BeautifulSoup4 for some popular webpages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HipyCas/BeautifulSites",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
