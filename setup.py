from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys

requirements = [line.strip() for line in open('requirements.txt').readlines()]

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(['block_avg/tests/tests.py'])
        sys.exit(errcode)


setup(name='block_avg',
      version='beta',
      description='Calculate block averages',
      url='http://github.com/tcmoore3/block_avg',
      author='Timothy C. Moore',
      author_email='timothy.c.moore@vanderbilt.edu',
      license='MIT',
      packages=find_packages(),
      #package_data={'linear_solver.testing': ['reference/*']},
      install_requires=requirements,
      zip_safe=False,
      test_suite='block_avg',
      cmdclass={'test': PyTest},
      extras_require={'utils': ['pytest']},
)
