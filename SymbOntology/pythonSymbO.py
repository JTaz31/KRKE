import rdflib
from rdflib import Graph 

Symbontology = Graph()
Symbontology.parse("/Users/ahi.maria/Documents/GitHub/KRKE/SymbOntology/ontologygraph.ttl", format="ttl")

CompetencyQuestion1 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#> 
SELECT ?Line 
WHERE { ?Line symbo:expresses symbo:Spleen}
'''
CompetencyQuestion2 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:expresses symbo:Musicality} 
'''

CompetencyQuestion3 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:expresses symbo:Vague} 
'''

CompetencyQuestion4 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:expresses symbo:Journey} 
'''

CompetencyQuestion5 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:expresses symbo:SeerPoet} 
'''

CompetencyQuestion6 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:expresses symbo:Escape} 
'''

CompetencyQuestion7 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Line 
WHERE {?Line symbo:expresses symbo:Purity} 
'''

CompetencyQuestion8 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Theme(COUNT(?Line) as?Theme_count)
WHERE{?Line symbo:express ?Theme.} 
GROUP BY ?Theme 
ORDER BY DESC(?Theme_count) 
LIMIT 1
'''

CompetencyQuestion9 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Author 
WHERE { symbo:Voyelles symbo:hasAuthor ?Author} 
'''

CompetencyQuestion10 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Author 
WHERE { symbo:BriseMarine symbo:hasAuthor ?Author} 
'''

CompetencyQuestion11 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Author 
WHERE { symbo:ArtPoetique symbo:hasAuthor ?Author} 
'''

CompetencyQuestion12 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Exponent
WHERE { ?Exponent symbo:isExponentOf symbo:Symbolism} 
'''

CompetencyQuestion13 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Exponent
WHERE { ?Exponent symbo:isExponentOf symbo:Decadentism} 
'''

CompetencyQuestion14 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT distinct ?Poet 
WHERE { { symbo:StéphaneMallarmé symbo:isInfluencedBy ?Poet} 
UNION
{ symbo:ArthurRimbaud symbo:isInfluencedBy ?Poet} 
UNION
{symbo:PaulVerlaine symbo:isInfluencedBy ?Poet} }
'''

CompetencyQuestion15 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT distinct ?Poet 
WHERE { { symbo:StéphaneMallarmé symbo:influences ?Poet} 
UNION
{ symbo:ArthurRimbaud symbo:influences ?Poet} 
UNION
{ symbo:PaulVerlaine symbo:influences ?Poet} }
'''


CompetencyQuestion16 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?FigureOfSpeech (COUNT(?Line) as ?FigureOfSpeech_count)
WHERE{?Line symbo:contains ?FigureOfSpeech.
?Line symbo:belongsTo symbo:Voyelles.}
GROUP BY ?FigureOfSpeech
ORDER BY DESC(?FigureOfSpeech_count)
LIMIT 1
'''


CompetencyQuestion17 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?FigureOfSpeech (COUNT(?Line) as ?FigureOfSpeech_count)
WHERE{?Line symbo:contains ?FigureOfSpeech.
?Line symbo:belongsTo symbo:ArtPoetique.}
GROUP BY ?FigureOfSpeech
ORDER BY DESC(?FigureOfSpeech_count)
LIMIT 1
'''


CompetencyQuestion18 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?FigureOfSpeech (COUNT(?Line) as ?FigureOfSpeech_count)
WHERE{?Line symbo:contains ?FigureOfSpeech.
?Line symbo:belongsTo symbo:BriseMarine.}
GROUP BY ?FigureOfSpeech
ORDER BY DESC(?FigureOfSpeech_count)
LIMIT 1
'''


CompetencyQuestion19 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?Theme 
WHERE { symbo:Symbolism symbo:hasSubject ?Theme}
'''

CompetencyQuestion20 = '''PREFIX symbo:<https://github.com/giorgimariachiara/KRKE/main/SymbOntology/SymbOntology.owl#>
SELECT ?FigureOfSpeech (COUNT(?Line) as ?Figure_count)
WHERE{?Line symbo:contains ?FigureOfSpeech.} 
GROUP BY ?FigureOfSpeech
ORDER BY DESC(?Figure_count) 
LIMIT 1
'''

listofcompetencyquestions = [CompetencyQuestion1, CompetencyQuestion2, CompetencyQuestion3, CompetencyQuestion4, CompetencyQuestion5, CompetencyQuestion6, CompetencyQuestion7, CompetencyQuestion8,CompetencyQuestion9, CompetencyQuestion10, CompetencyQuestion11, CompetencyQuestion12, CompetencyQuestion13, CompetencyQuestion14, CompetencyQuestion15, CompetencyQuestion16, CompetencyQuestion17, CompetencyQuestion18, CompetencyQuestion19, CompetencyQuestion20 ]
competency = ["In which lines is the Spleen theme present?", "In which lines is the Musicality theme present?", "In which lines is the Vague theme present?", "In which lines is the Journey theme present?","In which lines is the SeerPoet theme present?", "In which lines is the Escape theme present?", "In which lines is the Purity theme present?", "Which is the most frequent theme in the poems?", "Who is the author of Voyelles?", "Who is the author of Brise Marine?", "Who is the author of Art poetique?", "Which are the exponents of Symbolism?", "Which are the exponents of Decadentism?","Which Poets have influenced the Authors?", "Which Poet is influenced by the Authors?", "Which is the most frequent figure of speech in Voyelles?", "Which is the most frequent figure of speech in Art Poetique?", "Which is the most frequent figure of speech in Brise Marine?", "Which are the themes of Symbolism?", "Which is the most frequent figure of speech in the poems?" ]

for idx, competencyquestion in enumerate(listofcompetencyquestions):
    print("Competency question " + str(idx+1) + "- " + competency[idx] + ":")
    results = Symbontology.query(competencyquestion)
    for result in results:
        print(result)
