import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

PROJECT_NAME = "ANN_implementation_Python_scripting"
USERNAME = "arjunaju123"

setuptools.setup(
    name="src",
    version="0.0.1",
    author=USERNAME,
    author_email="54721arjun@gmail.com",
    description="It's an implementation of ANN",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USERNAME}/{PROJECT_NAME}",
    packages=["src"], #same as name
    python_requires=">=3.7",
    install_requires=["tensorflow",
                        "matplotlib",
                        "pandas",
                        "numpy", 
                        "seaborn",
                        "PyYAML"]
)