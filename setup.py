import setuptools

setuptools.setup(
    name='coingeckoapi',
    version='1.0.0',
    packages=['coingeckoapi',],
    license='MIT',
    description = 'Python project for CoingeckoAPI',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author = 'Emre Bekar',
    author_email = 'emre.bekar@hotmail.com.tr',
    install_requires=['requests'],
    url = 'https://github.com/emrebekar/coingeckoapi',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    )