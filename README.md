skosd is a little utility for turning a SKOS vocabulary into a simple
datastructure perfect for serializing as JSON. If the SKOS vocabulary
uses skos:notation you will end up with a dictionary like:

    {
      "ab": "Abkhazian", 
      "aa": "Afar", 
      "lo": "Lao", 
      "af": "Afrikaans", 
      "ae": "Avestan", 
      "ve": "Venda", 
      "is": "Icelandic", 
      ...
    }

And if the SKOS lacks skos:notations you will get a flat list of labels:

    [
      "Original", 
      "Duplicate magnetic track", 
      "Composite work print", 
      "Original a & b negative", 
      "Drawing", 
      "Dub: window", 
      "Receipts", 
      "Voiceover", 
      ...
    ]
