import setuptools

setuptools.setup(
    name='cg_api',
    version='1.0.1',
    packages=['src',],
    license='MIT',
    description = 'Python project for CoingeckoAPI',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Emre Bekar',
    author_email = 'emre.bekar@hotmail.com.tr',
    install_requires=['requests'],
    url = 'https://github.com/emrebekar/cg_api',
    download_url = 'https://github.com/emrebekar/coingeckoapi/archive/cg_api-1.0.1.tar.gz',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )