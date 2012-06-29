#!/usr/bin/env python

import sys
import json

sys.path.append('..')

import skosd


concept_schemes = {
    "marc-rel":  "http://id.loc.gov/vocabulary/relators.rdf",
    "marc-countries": "http://id.loc.gov/vocabulary/countries.rdf",
    "marc-geo": "http://id.loc.gov/vocabulary/geographicAreas.rdf",
    "marc-lang": "http://id.loc.gov/vocabulary/languages",
    "iso639-1": "http://id.loc.gov/vocabulary/iso639-1",
    "iso639-2": "http://id.loc.gov/vocabulary/iso639-2",
    "iso639-5": "http://id.loc.gov/vocabulary/iso639-5",
    "pbcore": "http://metadataregistry.org/vocabulary/show/id/147.rdf",
}

for name in concept_schemes.keys():
    url = concept_schemes[name]
    fh = open("%s.json" % name, "w")
    fh.write(json.dumps(skosd.skosd(url), indent=2).encode("utf-8"))
    fh.close()
