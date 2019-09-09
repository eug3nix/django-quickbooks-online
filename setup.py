import uuid
from setuptools import setup, find_packages

try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements

install_reqs = parse_requirements("requirements.txt", session=uuid.uuid1())
reqs = [str(req.req) for req in install_reqs]

setup(

    name = "django-quickbooks-online",

    version = '0.2.5',

    packages = find_packages(),

    install_requires = reqs,
    include_package_data = True,

    # metadata for upload to PyPI
    author = "Hans Kuder",
    author_email = "hans@hiidef.com",
    maintainer = "James O'Donnell",
    maintainer_email = "james@squarefactor.com",
    description = "Django Quickbooks App",
    license = "MIT License",
    keywords = "django quickbooks intuit",
    url = "http://github.com/eug3nix/django-quickbooks-online",

)
