from setuptools import setup, find_packages

setup(
    name='pyqt-vertical-tab-widget',
    version='0.0.1',
    author='Jung Gyu Yoon',
    author_email='yjg30737@gmail.com',
    license='MIT',
    packages=find_packages(),
    description='PyQt Vertical Tab Widget (text is horizontal)',
    url='https://github.com/yjg30737/pyqt-vertical-tab-widget.git',
    install_requires=[
        'PyQt5>=5.8'
    ]
)