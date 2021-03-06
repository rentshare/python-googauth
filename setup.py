from distutils.core import setup

setup(name='googauth',
      version='0.1.1',
      description='Python library for Google Authenticator.',
      author='RentShare Inc',
      url='https://github.com/rentshare/python-googauth',
      download_url='https://github.com/rentshare/python-googauth/' + \
                   'archive/0.1.1.zip',
      keywords='googauth, google authenticator, otp',
      packages=['googauth'],
      license='MIT',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Other Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2',
          'Topic :: Security',
      ],
     )
