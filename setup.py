import setuptools

setuptools.setup(
    name='coingeckoapi',
    version='2.2.0',
    packages=['coingeckoapi',],
    license='MIT',
    description = 'Python wrapper around the CoinGecko API',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Emre Bekar',
    author_email = 'emre.bekar@hotmail.com.tr',
    install_requires=['requests'],
    url = 'https://github.com/man-c/pycoingecko',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )