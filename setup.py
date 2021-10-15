from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'License :: OSI Approved :: MIT License',
    "Operating System :: Unix",
    "Operating System :: MacOS :: MacOS X",
    "Operating System :: Microsoft :: Windows",
    'Programming Language :: Python :: 3'
]

setup(
    name='mystorage',
    version='1.0',
    description='A simple solution to storage data in your python project using json tables and collections.',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/anthony16t/pystorage',  
    author='anthony16t',
    author_email='info@anthony16t.com',
    license='MIT', 
    classifiers=classifiers,
    keywords=['storage','json','table','database'], 
    packages=find_packages()
)