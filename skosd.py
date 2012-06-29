#!/usr/bin/env python

"""
Turn a SKOS vocab into a dictionary or list depending on whether the 
SKOS vocabulary uses skos:notation:

    % ./skosd.py http://id.loc.gov/vocabulary/relators.rdf

You can also use skosd programatically:

    .import skosd

    print skosd.skosd("http://id.loc.gov/vocabulary/relators.rdf")
  
"""

import sys
import json

from rdflib import Graph, RDF, Namespace

skos = Namespace("http://www.w3.org/2004/02/skos/core#")

def skosd(url, lang="en"):
    """
    Pass in a URL (can be a file protocol) for a SKOS file and get 
    back a dictionary of code => values.
    """
    graph = Graph()
    graph.parse(url)

    skos_dictionary = {}
    skos_list = []
    for concept in graph.subjects(RDF.type, skos.Concept):

        # determine the code
        code = graph.value(concept, skos.notation)

        # get the preferred language label, there could be more than one
        labels = list(graph.objects(concept, skos.prefLabel))
        if len(labels) > 1:
            for label in labels: 
                if label.language == lang:
                    break
        else:
            label = labels[0]

        if code:
            skos_dictionary[code] = label
        else:
            skos_list.append(label)

    if len(skos_dictionary.keys()) > 0:
        return skos_dictionary
    return skos_list

if __name__ == "__main__":
    url = sys.argv[1]
    print json.dumps(skosd(url), indent=2)
