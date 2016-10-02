from setuptools import setup

setup(name='Fireside',
      version='0.0.1',
      description='Talker-style MUD with card game features',
      long_description='Fireside is a talker-style MUD with card game '
                       'features built to use qtMUD',
      classifiers=['Development Status :: 3 - Alpha',
                   'Environment :: Console',
                   'Intended Audience :: End Users/Desktop',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 3',
                   'Topic :: Communications :: Chat',
                   'Topic :: Games/Entertainment :: Multi-User Dungeons (MUD)',
                   ],
      keywords='mud mmo mmorpg game',
      url='http://github.com/emsenn/fireside',
      author='emsenn',
      author_email='morgan.sennhauser@gmail.com',
      license='WTFPL',
      packages=['fireside'],
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      scripts=['bin/fireside_run'])