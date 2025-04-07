from setuptools import setup, find_packages

setup(
    name="quickshador",
    version="0.1",
    description="A Python library for image shadow generation and optimization.",
    author="Your Name",
    packages=find_packages(),
    install_requires=["Pillow"],
    entry_points={
        'console_scripts': [
            'quickshador-demo=quickshador.core:main'
        ]
    }
)
