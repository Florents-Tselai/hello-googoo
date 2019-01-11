from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hello-googoo',
    version='v0.1.0',
    packages=find_packages(),
    license='BSD',
    description='Google Search via Command Line',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Florents Tselai',
    author_email='florents@tselai.com',
    url='https://github.com/Florents-Tselai/hello-googoo',
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': ['googoo=hello_googoo.googoo:main',
                            'hello-googoo=hello_googoo.googoo:main']
    }
)
