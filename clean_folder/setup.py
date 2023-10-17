from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.1',
    packages=find_packages(),
    author='Taras',
    author_email='TarasGOIT@gmail.com',
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:clean_folder'
        ]
    },
)
