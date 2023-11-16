from setuptools import setup

setup(
    name='geo',
    version='1.0.0',
    description='Get coordinates from the title of the place',
    author='Igor Lashkov',
    author_email='rwrotson@yandex.ru',
    install_requires=[
        'geopy==2.2.0'
    ],
    entry_points={
        "console_scripts": [
            "geo = geo.main:get_location",
        ]
    },
)