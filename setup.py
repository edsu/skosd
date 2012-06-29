from distutils.core import setup

setup( 
    name             = 'jskon',
    version          = '0.0.1',
    url              = 'http://github.com/edsu/jskon',
    author           = 'Ed Summers',
    author_email     = 'ehs@pobox.com',
    license          = 'http://creativecommons.org/licenses/publicdomain/',
    py_modules       = ['skosdict'],
    description      = "Turn SKOS into JSON",
    install_requires = ['rdflib'],
)

