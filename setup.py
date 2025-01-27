import setuptools


__version__ = "0.0.0"

REPO_NAME = "Kidney-Disease-Classification"
AUTHOR_USER_NAME = "MalikArslanBashir"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "malikarslaninfo575@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)