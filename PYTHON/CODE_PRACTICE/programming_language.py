# dictionaries that are starting to look somewhat complex...
# yep...

favorite_languages = {
	'jen': ['python','ruby'],
	'sarah': ['c'],
	'edward': ['ruby','go'],
	'phil': ['python','haskell'],
}

for name, languages in favorite_languages.items():
	if len(languages) < 2:
		print("\n" + name.title() + "'s favorite language is:")
		for language in languages:
			print("\t" + language.title())
	else:
		print("\n" + name.title() + "'s favorite languages are:")
		for language in languages:
			print("\t" + language.title())
