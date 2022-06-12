from setuptools import setup, find_packages

version = "0.0.1"
setup(name='ShellyAPI',
      version=version,
      description='A Python class to interact with shellys',
      author='Tobias Rothlin',
      author_email='tobias@rothlin.com',
      url='https://github.com/TobiasRothlin/ShellyAPI',
      packages=find_packages(),
      install_requires=[
          'requests',
      ],
     )