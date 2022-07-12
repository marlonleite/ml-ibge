import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mlibge',
    version='0.1.0',    
    description='',
    url='https://github.com/marlonleite/ml-ibge',
    author='Marlon Leite',
    author_email='marlon@marlonleite.com.br',
    license='',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',  
        "Operating System :: OS Independent",        
        "Programming Language :: Python",
        'Programming Language :: Python :: 3.5',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Logging",
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['requests'],
)