from setuptools import setup
import os


version = '0.01'

try:  # this block doesn't work under tox
  here = os.path.abspath(os.path.dirname(__file__))
  README = open(os.path.join(here, 'README.md')).read()
#  HISTORY = open(os.path.join(here, 'HISTORY.md')).read()
except:
  pass


setup(name='pytest-virtualenv',
      version=version,
      description='py.test plugin to run tests under a virtual environment',
      author='Leah Klearman',
      author_email='lklrmn@gmail.com',
      url='https://github.com/klrmn/pytest-virtualenv',
      install_requires=['pytest>=2.2.3', 'virtualenv'],
      py_modules=['pytestvenv.plugin'],
      entry_points={'pytest11': ['pytest_random = pytestvenv.plugin']},
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest qa virtualenv',
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Software Development :: Quality Assurance',
        'Topic :: Software Development :: Testing',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'])
