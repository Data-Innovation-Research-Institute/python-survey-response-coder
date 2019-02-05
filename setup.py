import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="python-survey-response-coder",
    version="0.0.1",
    author="Jeffrey Morgan",
    description="Code survey responses.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrJeffreyMorgan/python-survey-response-coder.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
