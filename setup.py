from setuptools import  setup, find_packages


setup(name='otus-opencart-testing',
      version='1.0',
      author='Ivan Chistov',
      license='MIT',
      description='Different tests for Opencart',
      url='https://github.com/Darksol89/dz8_selenium',
      packages=find_packages(),
      install_requires=['pytest', 'selenium'],
      long_description=open('README.md').read(),
      zip_safe=False)