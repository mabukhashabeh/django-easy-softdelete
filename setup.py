from setuptools import find_packages, setup

with open('README.md', 'r') as f_readme:
    long_description = f_readme.read()

setup(
    name='django-easy-softdelete',
    packages=find_packages(),
    version="1.0",
    description="""Some users want a “recycling bin” or “archival” feature which allows
                    segregating active objects from non-active ones, 
                    and soft-deletion is one way of accomplishing this. 
                    The capability to delete and restore data needs to be available.
                    That is what django-easy-softdelete package offer.""",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mohammad Abu Khashabeh',
    author_email='abukhashabehmohammad@gmail.com',
    url='https://github.com/mabukhashabeh/djagno-softdelete',
    keywords=['django-easy-softdelete', 'delete', 'safedelete', 'softdelete', 'django'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Development Status :: 4 - Beta',
    ],
    license='BSD',
    install_requires=['Django'],
    include_package_data=True,
)
