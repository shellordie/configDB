from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = "A database like , dynamic config file generator to enable more customization in your python project . From games to ML notebooks and everything between."

setup(
        name="configDB", 
        version=VERSION,
        author="charles TCHANAKE",
        author_email="shellordie@gmail.com",
        url="https://github.com/shellordie/configDB",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=open("README.md","r",encoding="utf-8").read(),
        packages=find_packages(),
        keywords=["Config file","DB","customization"],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)
