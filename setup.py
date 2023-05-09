from setuptools import setup

setup(name='example_codes',
      version='0.1',
      description='learning_gpt_samples,
      url='http://github.com/mayashavin/openai-learning',
      author='Maya Shavin',
      author_email='dpnminh@gmail.com',
      license='MIT',
      packages=['learning_gpt_samples'],
      install_requires=[
        'openai',
        'IPython',
        'os',
        'dotenv',
        'panel'
      ],
      zip_safe=False)