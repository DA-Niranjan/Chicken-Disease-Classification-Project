import setuptools

# Read the content of the README file
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define the version of the package
__version__ = "0.0.0"

# Define constants for the repository name, author, source repo, and author email
REPO_NAME = "Chicken-Disease-Classification-Project"
AUTHOR_USER_NAME = "DA-Niranjan"
SRC_REPO = "CNN_Classifier"
AUTHOR_EMAIL = "niranjansable18@gmail.com"

# Set up the package using setuptools
setuptools.setup(
    name=SRC_REPO,  # Name of the package
    version=__version__,  # Version of the package
    author=AUTHOR_USER_NAME,  # Author's username
    author_email=AUTHOR_EMAIL,  # Author's email address
    description="A small python package for CNN app",  # Short description of the package
    long_description=long_description,  # Long description read from the README file
    long_description_content="text/markdown",  # Format of the long description
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the project repository
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # URL of the bug tracker
    },
    package_dir={"": "src"},  # Directory where the packages are located
    packages=setuptools.find_packages(where="src")  # Automatically find packages in the specified directory
)
