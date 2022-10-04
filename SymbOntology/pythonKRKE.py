import rdflib
from rdflib import Graph 

Symbontology = Graph()
Symbontology.parse("/Users/ahi.maria/Documents/GitHub/KRKE/SymbOntology/symbo.ttl", format="ttl")

print(Symbontology)

CompetencyQuestion1 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#> 
SELECT ?Line 
WHERE { ?Line symbo:express symbo:Spleen}
'''
CompetencyQuestion2 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:express symbo:Musicality} 
'''

CompetencyQuestion3 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:express symbo:Vague} 
'''

CompetencyQuestion4 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:express symbo:Journey} 
'''

CompetencyQuestion5 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:express symbo:SeerPoet} 
'''

CompetencyQuestion6 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:express symbo:Escape} 
'''

CompetencyQuestion7 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:express symbo:Purity} 
'''

CompetencyQuestion8 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Theme(COUNT(?Line) as?Theme_count)
WHERE{?Line symbo:express ?Theme.} 
GROUP BY ?Theme 
ORDER BY DESC(?Theme_count) 
LIMIT 1
'''

CompetencyQuestion9 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Author 
WHERE { symbo:Voyelles symbo:hasAuthor ?Author} 
'''

CompetencyQuestion10 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Author 
WHERE { symbo:BriseMarine symbo:hasAuthor ?Author} 
'''

CompetencyQuestion11 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Author 
WHERE { symbo:ArtPoetique symbo:hasAuthor ?Author} 
'''

CompetencyQuestion12 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Exponent
WHERE { ?Exponent symbo:isExponentOf symbo:Symbolism} 
'''

CompetencyQuestion13 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Exponent
WHERE { ?Exponent symbo:isExponentOf symbo:Decadentism} 
'''

CompetencyQuestion14 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT distinct ?Poet 
WHERE { ?Poet symbo:isInfluencedBy symbo:StéphaneMallarmé} 
UNION
{ ?Poet symbo:isInfluencedBy symbo:ArthurRimbaud} 
UNION
{ ?Poet symbo:isInfluencedBy symbo:PaulVerlaine} }
'''

CompetencyQuestion15 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT distinct ?Poet 
WHERE { symbo:StéphaneMallarmé symbo:influences ?Poet} 
UNION
{ symbo:ArthurRimbaud symbo:influences ?Poet} 
UNION
{ symbo:PaulVerlaine symbo:influences ?Poet} }
'''


CompetencyQuestion16 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?FigureOfSpeech (COUNT(?Line) as ?FigureOfSpeech_count)
WHERE{?Line symbo:contains ?FigureOfSpeech.
?Line symbo:belongsTo symbo:Voyelles.}
GROUP BY ?FigureOfSpeech
ORDER BY DESC(?FigureOfSpeech_count)
LIMIT 1
'''


CompetencyQuestion17 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?FigureOfSpeech (COUNT(?Line) as ?FigureOfSpeech_count)
WHERE{?Line symbo:contains ?FigureOfSpeech.
?Line symbo:belongsTo symbo:ArtPoetique.}
GROUP BY ?FigureOfSpeech
ORDER BY DESC(?FigureOfSpeech_count)
LIMIT 1
'''


CompetencyQuestion18 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?FigureOfSpeech (COUNT(?Line) as ?FigureOfSpeech_count)
WHERE{?Line symbo:contains ?FigureOfSpeech.
?Line symbo:belongsTo symbo:BriseMarine.}
GROUP BY ?FigureOfSpeech
ORDER BY DESC(?FigureOfSpeech_count)
LIMIT 1
'''


CompetencyQuestion19 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Theme 
WHERE { symbo:Symbolism symbo:hasSubject ?Theme}
'''

CompetencyQuestion20 = 
'''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/blob/main/SymbOntology/SymbOntology.owl#>
SELECT ?Theme 
WHERE { symbo:Symbolism symbo:hasSubject ?Theme}
'''



results = Symbontology.query(CompetencyQuestion11)
for result in results:
    print(result)
