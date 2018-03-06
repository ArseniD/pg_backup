from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.0.1',
    description='Database backups locally or to AWS S3.',
    long_description=readme,
    author='Arseni Dudko',
    author_email='arseni_dudko@mail.ru',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'pgbackup=pgbackup.cli:main',
        ]}
        )
