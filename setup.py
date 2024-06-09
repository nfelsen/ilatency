from setuptools import setup, find_packages

setup(
    name='iLatency',
    version='0.1.0',
    description='A simple network latency measurement tool similar to iperf',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Nathaniel Felsen',
    author_email='nfelsen@gmail.com',
    url='https://github.com/nfelsen/ilatency',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ilatency=ilatency.ilatency:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
