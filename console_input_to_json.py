import json


def get_console_input_weapon(index):
    weapon = 'weapon {}'.format(index)
    name = input('Enter weapon name: ')
    flavour = input('Enter weapon type: ')
    damage = int(input('Enter max weapon damage: '))
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}

    for i in range(len(t_dict)):
        current_trait = 'trait_{}'.format(i)
        if t_dict[current_trait] != 'none':
            trait = input('Enter special effect: ')
            if trait == 'none':
                for j in range(i, len(t_dict)):
                    t_dict['trait_{}'.format(j)] = 'none'
            else:
                t_dict[current_trait] = trait

    unique = input('Unique? (t/f): ')

    if unique == "t":
        unique = True
    else:
        unique = False

    attributes = {'name': name,
                  'type': flavour,
                  'damage': damage,
                  'traits': t_dict,
                  'unique': unique
                  }
    attributes = {weapon: attributes}
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


def print_weapon_info(attr_dict):
    key = list(attr_dict.keys())[0]
    print("Name: {}\n".format(attr_dict[key]["name"]),
          "Type: {}\n".format(attr_dict[key]["type"]),
          "Damage: {}\n".format(attr_dict[key]["damage"]),
          "Effect: {}\n".format(attr_dict[key]["aux_effect"]),
          "Unique: {}\n".format(attr_dict[key]["unique"]))


def append_dictionary(dictionary, dict_type):
    switch_dict = {
        'classes': lambda: dictionary.update(get_console_input_class(len(dictionary))),
        'races': lambda: dictionary.update(get_console_input_race(len(dictionary))),
        'weapons': lambda: dictionary.update(get_console_input_weapon(len(dictionary))),
        'armour': lambda: dictionary.update(get_console_input_armour(len(dictionary))),
        'traits': lambda: dictionary.update(get_console_input_trait(len(dictionary))),
        'enchantments': lambda: dictionary.update(get_console_input_enchantment(len(dictionary)),
        'items': lambda: dictionary.update(get_console_input_items(len(dictionary))),
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
weapon_ench_dict = read_json_from_file('data/weapon_enchantments.json')
armour_ench_dict = read_json_from_file('data/armour_enchantments.json')
item_ench_dict = read_json_from_file('data/item_enchantments.json')
item_dict = read_json_from_file('data/items.json')
character_dict = read_json_from_file('data/characters.json')

#append_dictionary(weapon_dict, 'weapons')
append_dictionary(weapon_ench_dict, 'enchantments')
dump_to_json(weapon_ench_dict, 'weapon_enchantments.json')
#dump_to_json(weapon_dict, 'weapons.json')