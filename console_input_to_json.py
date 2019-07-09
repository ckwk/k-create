import json


def get_console_input_weapon(index):
    weapon = 'weapon {}'.format(index)
    name = input('Enter weapon name: ')
    flavour = input('Enter weapon type: ')
    damage = int(input('Enter max weapon damage: '))
    effect = input('Enter special effect: ')
    unique = input('Unique? (t/f): ')

    if unique == "t":
        unique = True
    else:
        unique = False

    attributes = {"name": name,
                  "type": flavour,
                  "damage": damage,
                  "aux_effect": effect,
                  "unique": unique
                  }
    attributes = {weapon: attributes}
    return attributes


def print_weapon_info(attr_dict):
    key = list(attr_dict.keys())[0]
    print("Name: {}\n".format(attr_dict[key]["name"]),
          "Type: {}\n".format(attr_dict[key]["type"]),
          "Damage: {}\n".format(attr_dict[key]["damage"]),
          "Effect: {}\n".format(attr_dict[key]["aux_effect"]),
          "Unique: {}\n".format(attr_dict[key]["unique"]))


def append_dictionary(dictionary, dict_type):
    switch_dict = {
        'classes': dictionary.update(get_console_input_class(len(dictionary))),
        'races': dictionary.update(get_console_input_race(len(dictionary))),
        'weapons': dictionary.update(get_console_input_weapon(len(dictionary))),
        'armour': dictionary.update(get_console_input_armour(len(dictionary))),
        'traits': dictionary.update(get_console_input_trait(len(dictionary))),
        'weapon_traits': dictionary.update(get_console_input_weapon_trait(len(dictionary))),
        'armour_traits': dictionary.update(get_console_input_armour_trait(len(dictionary))),
        'item_traits': dictionary.update(get_console_input_item_trait(len(dictionary))),
        'items': dictionary.update(get_console_input_items(len(dictionary))),
        'characters': dictionary.update(get_console_input_character(len(dictionary))),
    }
    switch_dict[dict_type]()


def dump_to_json(dictionary, directory):
    outfile = open(directory, 'w')
    json.dump(dictionary, outfile)
    outfile.close()
    print(json.dumps(dictionary, indent=4))


def read_json_from_file(directory):
    infile = open(directory, 'r')
    dictionary = json.load(infile)
    infile.close()
    return dictionary


class_dict = read_json_from_file('classes.json')
race_dict = read_json_from_file('races.json')
weapon_dict = read_json_from_file('weapons.json')
armour_dict = read_json_from_file('armour.json')
trait_dict = read_json_from_file('traits.json')
weapon_trait_dict = read_json_from_file('weapon_traits.json')
armour_trait_dict = read_json_from_file('armour_traits.json')
item_trait_dict = read_json_from_file('item_traits.json')
item_dict = read_json_from_file('items.json')
character_dict = read_json_from_file('characters.json')

append_dictionary(weapon_dict, 'weapons')
dump_to_json(weapon_dict, 'weapons.json')
