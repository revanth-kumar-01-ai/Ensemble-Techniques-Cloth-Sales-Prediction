import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Ensemble-Techniques-Cloth-Sales-Prediction"
AUTHOR_USER_NAME = "revanth-kumar-01-ai"
SRC_REPO = "Ensemble_cloth_Sales_prediction"
AUTHOR_EMAIL = "revanthj486@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="🛍️ Ensemble Learning: Apply Bagging, Boosting, Stacking, and Voting to enhance accuracy. 📊 Optimize with GridSearchCV for best performance. 🚀",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)