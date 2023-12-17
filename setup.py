from setuptools import setup, find_packages

setup(
    name='argosos',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # List your project dependencies here
        'fastapi==0.104.1',
        'Markdown==3.5.1',
        'Jinja2==3.1.2',
        'uvicorn==0.24.0.post1'
    ],
    entry_points={
        'console_scripts': [
            'my_project = my_module.main:main',  # Adjust based on your project structure
        ],
    },
)