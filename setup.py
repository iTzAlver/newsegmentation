# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                                                           #
#   This file was created by: Alberto Palomo Alonso         #
# Universidad de Alcalá - Escuela Politécnica Superior      #
#                                                           #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='src',
    version='0.3.2',
    author='Alberto Palomo Alonso',
    author_email='a.palomo@uah.es',
    description='Package for news segmentation architecture.',
    keywords='deeplearning, ml, api',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/iTzAlver/newsegmentation',
    project_urls={
        'Documentation': 'https://github.com/iTzAlver/newsegmentation/blob/master/README.md',
        'Bug Reports': 'https://github.com/iTzAlver/newsegmentation/issues',
        'Source Code': 'https://github.com/iTzAlver/newsegmentation.git',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Text Editors :: Text Processing',
        'Topic :: Text Processing',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    python_requires='>=3.6',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
    },
)
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
#                        END OF FILE                        #
# - x - x - x - x - x - x - x - x - x - x - x - x - x - x - #
