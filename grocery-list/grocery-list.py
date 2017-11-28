import itertools
import yaml

docs = yaml.load(open("recipes.yml", "r"))
options = dict((i, (name, values)) for i, (name, values) in enumerate(docs.items(), 1))

print "What would you like to cook on weekend?"
print "Here are the options:"
for option, (name, ingredients) in iter(sorted(options.iteritems())):
    print str(option) + ". " + str(name)

choose = raw_input("> ")

try:
    shopping_list = [options[int(choice.strip())][1] for choice in choose.split(",")]
    print "Buy " + ", ".join(itertools.chain.from_iterable(shopping_list)) + "."
except (IndexError, ValueError):
    print "Hmmm. No such food on the list."