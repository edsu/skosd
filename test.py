#!/usr/bin/env python

import unittest

import skosd

class SimpleTest(unittest.TestCase):

    def test_dict(self):
        d = skosd.skosd("http://id.loc.gov/vocabulary/relators.rdf")

    def test_list(self):
        l = skosd.skosd("http://metadataregistry.org/vocabulary/show/id/147.rdf")

if __name__ == "__main__":
    unittest.main()
