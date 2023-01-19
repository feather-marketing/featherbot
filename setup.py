from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
  name="featherbot",
  version="0.0.12",
  license="GPL-3",
  author="Bailey de Villiers",
  author_email="bailey.devilliers@gmail.com",
  description = "Website audit tool for digital marketing.",
  long_description=open("README.md", 'r').read(),
  long_description_content_type='text/markdown',
  url='https://github.com/feather-marketing/featherbot',
  keywords="",

  packages = find_packages(),
  package_dir={"" : "."},
  install_requires=[
    "async-generator",
    "attrs",
    "beautifulsoup4",
    "certifi",
    "charset-normalizer",
    "exceptiongroup",
    "h11",
    "idna",
    "numpy",
    "outcome",
    "packaging",
    "pandas",
    "PySocks",
    "python-dateutil",
    "python-dotenv",
    "pytz",
    "requests",
    "selenium",
    "six",
    "sniffio",
    "sortedcontainers",
    "soupsieve",
    "tqdm",
    "trio",
    "trio-websocket",
    "urllib3",
    "webdriver-manager",
    "wsproto"
  ],
)

