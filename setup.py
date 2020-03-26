
from setuptools import setup, find_packages


with open('README.md') as file:
    description = file.read()


setup(
    name='naeval',
    version='0.2.0',

    description='Comparing quality and performance of NLP systems for Russian language',
    long_description=description,
    long_description_content_type='text/markdown',

    url='https://github.com/natasha/naeval',
    author='Alexander Kukushkin',
    author_email='alex@alexkuk.ru',
    license='MIT',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='nlp, russian, evaluation',

    packages=find_packages()
)
