languages = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}

#for entry, creator in languages.items():
#    print(entry, "was created by", creator)

for entry in languages:
    print(entry, "was created by", languages[entry])