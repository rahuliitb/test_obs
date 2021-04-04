from setuptools import setup

setup(
    name='test_obs',
    version='0.0.1',
    description='My private package from private github repo',
    url='git@github:git@github.com:rahuliitb16/test_pakage.git',
    author='Rahul Kumar',
    author_email='rahuliitb16@gmail.com',
    license='unlicense',
    packages=['test_obs'],
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3.6'],
    zip_safe=False
)
