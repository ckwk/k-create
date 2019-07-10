import json


def get_console_input_class(index):
    char_class = 'class {}'.format(index)
    name = input('Enter class name: ')
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}

    # Add traits
    for i in range(len(t_dict)):
        current_trait = 'trait_{}'.format(i)
        if t_dict[current_trait] != 'none':
            trait = input('Enter possible trait: ')
            if trait == 'none':
                for j in range(i, len(t_dict)):
                    t_dict['trait_{}'.format(j)] = 'none'
            else:
                for key in class_trait_dict:
                    if class_trait_dict[key]["name"] == trait:
                        trait = class_trait_dict.get(key)

    attributes = {'name': name,
                  'traits': t_dict,
                  }
    attributes = {char_class: attributes}
    return attributes


def get_console_input_race(index):
    race = 'race {}'.format(index)
    name = input('Enter race name: ')
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}

    # Add traits
    for i in range(len(t_dict)):
        current_trait = 'trait_{}'.format(i)
        if t_dict[current_trait] != 'none':
            trait = input('Enter possible trait: ')
            if trait == 'none':
                for j in range(i, len(t_dict)):
                    t_dict['trait_{}'.format(j)] = 'none'
            else:
                for key in race_trait_dict:
                    if race_trait_dict[key]["name"] == trait:
                        trait = race_trait_dict.get(key)

    attributes = {'name': name,
                  'traits': t_dict,
                  }
    attributes = {race: attributes}
    return attributes


def get_console_input_weapon(index):
    weapon = 'weapon {}'.format(index)
    name = input('Enter weapon name: ')
    flavour = input('Enter weapon type: ')
    damage = int(input('Enter max weapon damage: '))
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}

    # Add traits
    for i in range(len(t_dict)):
        current_trait = 'trait_{}'.format(i)
        if t_dict[current_trait] != 'none':
            trait = input('Enter possible trait: ')
            if trait == 'none':
                for j in range(i, len(t_dict)):
                    t_dict['trait_{}'.format(j)] = 'none'
            else:
                for key in trait_dict:
                    if trait_dict[key]["name"] == trait:
                        trait = trait_dict.get(key)

    # Add enchantments
    enchantment = input('Enter enchantment: ')
    if enchantment != 'none':
        for key in weapon_ench_dict:
            if weapon_ench_dict[key]["name"] == enchantment:
                enchantment = weapon_ench_dict.get(key)

    unique = input('Unique? (t/f): ')
    if unique == "t":
        unique = True
    else:
        unique = False

    attributes = {'name': name,
                  'type': flavour,
                  'damage': damage,
                  'traits': t_dict,
                  'enchantment': enchantment,
                  'unique': unique
                  }
    attributes = {weapon: attributes}
    return attributes


def get_console_input_armour(index):
    armour = 'armour {}'.format(index)
    name = input('Enter armour name: ')
    flavour = input('Enter armour type: ')
    resistance = int(input('Enter armour resistance: '))
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}

    # Add traits
    for i in range(len(t_dict)):
        current_trait = 'trait_{}'.format(i)
        if t_dict[current_trait] != 'none':
            trait = input('Enter possible trait: ')
            if trait == 'none':
                for j in range(i, len(t_dict)):
                    t_dict['trait_{}'.format(j)] = 'none'
            else:
                for key in trait_dict:
                    if trait_dict[key]["name"] == trait:
                        trait = trait_dict.get(key)

    # Add enchantments
    enchantment = input('Enter enchantment: ')
    if enchantment != 'none':
        for key in armour_ench_dict:
            if armour_ench_dict[key]["name"] == enchantment:
                enchantment = armour_ench_dict.get(key)

    unique = input('Unique? (t/f): ')
    if unique == "t":
        unique = True
    else:
        unique = False

    attributes = {'name': name,
                  'type': flavour,
                  'resistance': resistance,
                  'traits': t_dict,
                  'enchantment': enchantment,
                  'unique': unique
                  }
    attributes = {armour: attributes}
    return attributes


def get_console_input_trait(index):
    trait = 'trait {}'.format(index)
    name = input('Enter trait name: ')
    flavour = input('Enter trait type: ')
    pros = {'pro_0': '', 'pro_1': '', 'pro_2': ''}
    cons = {'con_0': '', 'con_1': '', 'con_2': ''}

    # Add positive effects to the 'pros' dictionary
    for i in range(len(pros)):
        current_pro = 'pro_{}'.format(i)
        if pros[current_pro] != 'none':
            pro = input('Enter positive trait effect: ')
            if pro == 'none':
                for j in range(i, len(pros)):
                    pros['pro_{}'.format(j)] = 'none'
            else:
                pros[current_pro] = pro

    # Add negative effects to the 'cons' dictionary
    for i in range(len(cons)):
        current_con = 'con_{}'.format(i)
        if cons[current_con] != 'none':
            con = input('Enter negative trait effect: ')
            if con == 'none':
                for j in range(i, len(cons)):
                    cons['con_{}'.format(j)] = 'none'
            else:
                cons[current_con] = con

    attributes = {'name': name,
                  'type': flavour,
                  'pros': pros,
                  'cons': cons
                  }
    attributes = {trait: attributes}
    return attributes


def get_console_input_enchantment(index):
    enchantment = 'enchantment {}'.format(index)
    name = input('Enter enchantment name: ')
    flavour = input('Enter enchantment type: ')
    pros = {'pro_0': '', 'pro_1': '', 'pro_2': ''}
    cons = {'con_0': '', 'con_1': '', 'con_2': ''}

    # Add positive effects to the 'pros' dictionary
    for i in range(len(pros)):
        current_pro = 'pro_{}'.format(i)
        if pros[current_pro] != 'none':
            pro = input('Enter positive enchantment effect: ')
            if pro == 'none':
                for j in range(i, len(pros)):
                    pros['pro_{}'.format(j)] = 'none'
            else:
                pros[current_pro] = pro

    # Add negative effects to the 'cons' dictionary
    for i in range(len(cons)):
        current_con = 'con_{}'.format(i)
        if cons[current_con] != 'none':
            con = input('Enter negative enchantment effect: ')
            if con == 'none':
                for j in range(i, len(cons)):
                    cons['con_{}'.format(j)] = 'none'
            else:
                cons[current_con] = con

    attributes = {'name': name,
                  'type': flavour,
                  'pros': pros,
                  'cons': cons
                  }
    attributes = {enchantment: attributes}
    return attributes


def get_console_input_item(index):
    weapon = 'item {}'.format(index)
    name = input('Enter item name: ')
    flavour = input('Enter item type: ')

    # Add enchantments
    enchantment = input('Enter enchantment: ')
    if enchantment != 'none':
        for key in item_ench_dict:
            if item_ench_dict[key]["name"] == enchantment:
                enchantment = item_ench_dict.get(key)

    unique = input('Unique? (t/f): ')
    if unique == "t":
        unique = True
    else:
        unique = False

    attributes = {'name': name,
                  'type': flavour,
                  'enchantment': enchantment,
                  'unique': unique
                  }
    attributes = {weapon: attributes}
    return attributes


def append_dictionary(dictionary, dict_type):
    switch_dict = {
        'classes': lambda: dictionary.update(get_console_input_class(len(dictionary))),
        'races': lambda: dictionary.update(get_console_input_race(len(dictionary))),
        'weapons': lambda: dictionary.update(get_console_input_weapon(len(dictionary))),
        'armour': lambda: dictionary.update(get_console_input_armour(len(dictionary))),
        'traits': lambda: dictionary.update(get_console_input_trait(len(dictionary))),
        'enchantments': lambda: dictionary.update(get_console_input_enchantment(len(dictionary))),
        'items': lambda: dictionary.update(get_console_input_item(len(dictionary))),
        'characters': lambda: dictionary.update(get_console_input_character(len(dictionary))),
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


class_dict = read_json_from_file('data/classes.json')
race_dict = read_json_from_file('data/races.json')
weapon_dict = read_json_from_file('data/weapons.json')
armour_dict = read_json_from_file('data/armour.json')
trait_dict = read_json_from_file('data/traits.json')
race_trait_dict = read_json_from_file('data/race_traits.json')
class_trait_dict = read_json_from_file('data/class_traits.json')
weapon_ench_dict = read_json_from_file('data/weapon_enchantments.json')
armour_ench_dict = read_json_from_file('data/armour_enchantments.json')
item_ench_dict = read_json_from_file('data/item_enchantments.json')
item_dict = read_json_from_file('data/items.json')
character_dict = read_json_from_file('data/characters.json')

# append_dictionary(weapon_ench_dict, 'enchantments')
# dump_to_json(weapon_ench_dict, 'data/weapon_enchantments.json')
append_dictionary(weapon_dict, 'weapons')
dump_to_json(weapon_dict, 'data/weapons.json')
