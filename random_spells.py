from collections import namedtuple
import random
import sys


SOURCES = {'Players Handbook', 'Xanathars Guide To Everything', 'Source'}


Spell = namedtuple('Spell', ['name', 'level', 'source'])


def make_spell(spell_line):
    (name,
     level_str,
     school,
     time,
     is_ritual,
     is_concentration,
     clazz,
     source) = spell_line.strip().split(', ')
    return Spell(name, int(level_str), source)


def main():
    with open('current_spells.txt', 'r') as current_spells:
        known = set(map(lambda s: s.strip(), current_spells))
    try:
        max_level = int(sys.argv[1])
    except:
        # TODO usage
        exit()
    def check_spell(spell):
        (name, level, source) = spell
        return (source in SOURCES and
                level > 0 and
                level <= max_level and
                name not in known)
    with open('spells.csv', 'r') as spells:
        spells.readline() # discard header line
        all_spells = map(make_spell, spells.readlines())
        valid_spells = [spell for spell in all_spells if check_spell(spell)]
    for random_spell in random.choices(valid_spells, k=3):
        print(random_spell.name)

if __name__ == '__main__':
    main()
