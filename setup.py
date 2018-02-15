from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='funniest',
    version='0.1',
    description='The funniest joke in the world',
    long_description=readme(),
    classifiers=[
        'Development Status:: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Text Processing :: Linguistic',
    ],
    keywords='funniest joke comedy flying circus',
    url='https://github.com/nctl144/funniest',
    author='chau tung lam nguyen',
    author_email='nctl144@gmail.com',
    license='MIT',
    install_requires=[
        'markdown',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    packages=['funniest'],
    zip_safe=False)
