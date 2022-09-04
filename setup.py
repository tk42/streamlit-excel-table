import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="streamlit-excel-table",
    version="0.2.1",
    author="tk42",
    author_email="nsplat+pip@gmail.com",
    description="Streamlit component implementation of react-awesome-table",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tk42/streamlit-excel-table",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
