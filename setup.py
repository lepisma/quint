from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name = 'quint',
	version = '0.1',
	description = 'Quint is a minimal path finding library useful for discrete state scenarios',
	long_description = readme(),
	keywords = 'q-learning reinforcement learning path finding',
	url = 'http://github.com/lepisma/quint',
	author = 'lepisma',
	author_email = 'abhinav.tushar.vs@gmail.com',
	license = 'MIT',
	packages = ['quint'],
	install_requires = ['numpy'],
	include_package_data = True,
	zip_safe = False)
