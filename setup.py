from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='hypertrack-sdk',
      version='1.0.0',
      description='Hypertrack API SDK',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url='https://github.com/sartim/hypertrack-sdk',
      author='sartim',
      license='MIT',
      packages=find_packages(),
      install_requires=[
            'python-dotenv',
            'requests',
            'tox',
      ],
      zip_safe=False,
      classifiers=[
          "Programming Language :: Python :: 2 :: Python :: 3",
          "Operating System :: OS Independent",
        ]
      )
