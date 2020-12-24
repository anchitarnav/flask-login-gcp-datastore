import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="flask-login-gcp-datastore", # Replace with your own username
    version="0.0.2",
    author="Anchit Arnav",
    author_email="arnavanchit@gmail.com",
    description="Implement flask-login with Google Cloud Datastore",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/anchitarnav/flask-login-gcp-datastore",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    # Additional
    keywords='gcp datastore flask-login flask login google cloud',
    install_requires=['google-cloud-ndb'],
    license='Apache Software License'

)