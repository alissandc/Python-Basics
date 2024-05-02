import re
result = re.search(r"aza", "plaza")
print(result)
#<_sre.SRE_Match object; span=(2, 5), match='aza'>
#------------------------------------------------------------------------------------
result = re.search(r"aza", "bazaar")
print(result)
#<_sre.SRE_Match object; span=(1, 4), match='aza'>
#------------------------------------------------------------------------------------
result = re.search(r"aza", "maze")
print(result)
#None

print(re.search(r"^x", "xenon"))
#<_sre.SRE_Match object; span=(0, 1), match='x'>
#------------------------------------------------------------------------------------
print(re.search(r"p.ng", "clapping"))
#<_sre.SRE_Match object; span=(4, 8), match='ping'>
print(re.search(r"p.ng", "sponge"))
#<_sre.SRE_Match object; span=(1, 5), match='pong'>
#------------------------------------------------------------------------------------
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))
#<_sre.SRE_Match object; span=(0, 4), match='Pang'>
#------------------------------------------------------------------------------------   
print(re.search(r"[Pp]ython", "Python"))
#<_sre.SRE_Match object; span=(0, 6), match='Python'>
#------------------------------------------------------------------------------------
print(re.search(r"[a-z]way", "The end of the highway"))
#<_sre.SRE_Match object; span=(18, 22), match='hway'>
print(re.search(r"[a-z]way", "What a way to go"))
#None
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
#<_sre.SRE_Match object; span=(0, 6), match='cloudy'>
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))
#<_sre.SRE_Match object; span=(0, 6), match='cloud9'>
#------------------------------------------------------------------------------------
print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
#<_sre.SRE_Match object; span=(4, 5), match=' '>
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
#<_sre.SRE_Match object; span=(30, 31), match='.'>

print(re.search(r"cat|dog", "I like cats."))
#<_sre.SRE_Match object; span=(7, 10), match='cat'>
print(re.search(r"cat|dog", "I love dogs!"))
#<_sre.SRE_Match object; span=(7, 10), match='dog'>
print(re.search(r"cat|dog", "I like both dogs and cats."))
#<_sre.SRE_Match object; span=(12, 15), match='dog'>
print(re.findall(r"cat|dog", "I like both dogs and cats."))
#['dog', 'cat']
#------------------------------------------------------------------------------------
print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))
#------------------------------------------------------------------------------------
print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))
#------------------------------------------------------------------------------------
print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------