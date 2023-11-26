# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="flask_oa3",  # Required
    version="0.0.1",  # Required
    description="A Flask wrapper to programmatically define openapi 3 spec documentation",  # Optional
    long_description=long_description,  # Optional
    long_description_content_type="text/markdown",  # Optional (see note above)
    url="https://github.com/mfkaroui/flask_oa3",  # Optional
    author="Mohamed Karoui",  # Optional
    author_email="mfkaroui@gmail.com",  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: API Tools :: Open API 3 :: REST",
        # Pick your license as you wish
        "License :: OSI Approved :: GPL 3.0 License",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="flask rest openapi oa3",  # Optional
    packages=find_packages(exclude=["contrib", "docs", "tests"]),  # Required
    python_requires=">=3.11",
    install_requires=[
        "blinker==1.7.0; python_version >= '3.8'",
        "click==8.1.7; python_version >= '3.7'",
        "colorama==0.4.6; platform_system == 'Windows'",
        "flask==3.0.0; python_version >= '3.8'",
        "itsdangerous==2.1.2; python_version >= '3.7'",
        "jinja2==3.1.2; python_version >= '3.7'",
        "markupsafe==2.1.3; python_version >= '3.7'",
        "werkzeug==3.0.1; python_version >= '3.8'",
    ],  # Optional
    extras_require={"dev": []},  # Optional
    dependency_links=[],
    project_urls={  # Optional
        "Bug Reports": "https://github.com/mfkaroui/flask_oa3/issues",
        "Source": "https://github.com/mfkaroui/flask_oa3",
    },
)
