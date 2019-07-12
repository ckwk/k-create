import json


def get_console_input_race(index):
    race = 'race {}'.format(index)
    name = input('Enter race name: ')
    description = input('Enter description: ')

    # Add traits
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}
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
                  'description': description,
                  'traits': t_dict
                  }
    attributes = {race: attributes}
    return attributes


def get_console_input_weapon(index):
    weapon = 'weapon {}'.format(index)
    name = input('Enter weapon name: ')
    flavour = input('Enter weapon type: ')
    description = input('Enter description: ')
    damage = int(input('Enter max weapon damage: '))

    # Add requirements to the 'requirements' dictionary
    requirements = {'req_0': '', 'req_1': '', 'req_2': ''}
    for i in range(len(requirements)):
        current_req = 'req_{}'.format(i)
        if requirements[current_req] != 'none':
            req = input('Enter stat requirement: ')
            if req == 'none':
                for j in range(i, len(requirements)):
                    requirements['req_{}'.format(j)] = 'none'
            else:
                requirements[current_req] = req

    # Add traits
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}
    for i in range(len(t_dict)):
        current_trait = 'trait_{}'.format(i)
        if t_dict[current_trait] != 'none':
            trait = input('Enter possible trait: ')
            if trait == 'none':
                for j in range(i, len(t_dict)):
                    t_dict['trait_{}'.format(j)] = 'none'
            else:
                for key in trait_dict:
                    if trait_dict[key]["name"] == trait and trait_dict[key]["type"] == 'weapon':
                        trait = trait_dict.get(key)

    # Add enchantments
    enchantment = input('Enter enchantment: ')
    if enchantment != 'none':
        for key in weapon_ench_dict:
            if weapon_ench_dict[key]["name"] == enchantment:
                enchantment = weapon_ench_dict.get(key)

    # Is the item unique?
    unique = input('Unique? (t/f): ')
    if unique == "t":
        unique = True
    else:
        unique = False

    attributes = {'name': name,
                  'type': flavour,
                  'description': description,
                  'damage': damage,
                  'requirements': requirements,
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
    description = input('Enter description: ')
    resistance = int(input('Enter armour resistance: '))

    # Add requirements to the 'requirements' dictionary
    requirements = {'req_0': '', 'req_1': '', 'req_2': ''}
    for i in range(len(requirements)):
        current_req = 'req_{}'.format(i)
        if requirements[current_req] != 'none':
            req = input('Enter stat requirement: ')
            if req == 'none':
                for j in range(i, len(requirements)):
                    requirements['req_{}'.format(j)] = 'none'
            else:
                requirements[current_req] = req

    # Add traits
    t_dict = {'trait_0': '', 'trait_1': '', 'trait_2': '', 'trait_3': '', 'trait_4': ''}
    for i in range(len(t_dict)):
        current_trait = 'trait_{}'.format(i)
        if t_dict[current_trait] != 'none':
            trait = input('Enter possible trait: ')
            if trait == 'none':
                for j in range(i, len(t_dict)):
                    t_dict['trait_{}'.format(j)] = 'none'
            else:
                for key in trait_dict:
                    if trait_dict[key]["name"] == trait and trait_dict[key]["type"] == 'armour':
                        trait = trait_dict.get(key)

    # Add enchantments
    enchantment = input('Enter enchantment: ')
    if enchantment != 'none':
        for key in armour_ench_dict:
            if armour_ench_dict[key]["name"] == enchantment:
                enchantment = armour_ench_dict.get(key)

    # Is the item unique?
    unique = input('Unique? (t/f): ')
    if unique == "t":
        unique = True
    else:
        unique = False

    attributes = {'name': name,
                  'type': flavour,
                  'description': description,
                  'resistance': resistance,
                  'requirements': requirements,
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
    description = input('Enter description: ')

    # Add effects to the 'effects' dictionary
    effects = {'effect_0': '', 'effect_1': '', 'effect_2': ''}
    for i in range(len(effects)):
        current_effect = 'effect_{}'.format(i)
        if effects[current_effect] != 'none':
            effect = input('Enter trait effect: ')
            if effect == 'none':
                for j in range(i, len(effects)):
                    effects['effect_{}'.format(j)] = 'none'
            else:
                effects[current_effect] = effect

    attributes = {'name': name,
                  'type': flavour,
                  'description': description,
                  'effects': effects,
                  }
    attributes = {trait: attributes}
    return attributes


def get_console_input_ability(index):
    ability = 'ability {}'.format(index)
    name = input('Enter ability name: ')
    description = input('Enter description: ')

    # Add requirements to the 'requirements' dictionary
    requirements = {'req_0': '', 'req_1': '', 'req_2': ''}
    for i in range(len(requirements)):
        current_req = 'req_{}'.format(i)
        if requirements[current_req] != 'none':
            req = input('Enter stat requirement: ')
            if req == 'none':
                for j in range(i, len(requirements)):
                    requirements['req_{}'.format(j)] = 'none'
            else:
                requirements[current_req] = req

    # Add effects to the 'effects' dictionary
    effects = {'effect_0': '', 'effect_1': '', 'effect_2': ''}
    for i in range(len(effects)):
        current_effect = 'effect_{}'.format(i)
        if effects[current_effect] != 'none':
            effect = input('Enter ability effect: ')
            if effect == 'none':
                for j in range(i, len(effects)):
                    effects['effect_{}'.format(j)] = 'none'
            else:
                effects[current_effect] = effect

    attributes = {'name': name,
                  'description': description,
                  'requirements': requirements,
                  'effects': effects,
                  }
    attributes = {ability: attributes}
    return attributes


def get_console_input_enchantment(index):
    enchantment = 'enchantment {}'.format(index)
    name = input('Enter enchantment name: ')
    flavour = input('Enter enchantment type: ')

    # Add positive effects to the 'pros' dictionary
    pros = {'pro_0': '', 'pro_1': '', 'pro_2': ''}
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
    cons = {'con_0': '', 'con_1': '', 'con_2': ''}
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

    # Is the item unique?
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
        'abilities': lambda: dictionary.update(get_console_input_ability(len(dictionary))),
        'armours': lambda: dictionary.update(get_console_input_armour(len(dictionary))),
        'armour_enchantments': lambda: dictionary.update(get_console_input_enchantment(len(dictionary))),
        'characters': lambda: dictionary.update(get_console_input_character(len(dictionary))),
        'items': lambda: dictionary.update(get_console_input_item(len(dictionary))),
        'item_enchantments': lambda: dictionary.update(get_console_input_enchantment(len(dictionary))),
        'races': lambda: dictionary.update(get_console_input_race(len(dictionary))),
        'race_traits': lambda: dictionary.update(get_console_input_race(len(dictionary))),
        'weapons': lambda: dictionary.update(get_console_input_weapon(len(dictionary))),

        'traits': lambda: dictionary.update(get_console_input_trait(len(dictionary))),

        'enchantments': lambda: dictionary.update(get_console_input_enchantment(len(dictionary))),


    }
    switch_dict[dict_type]()


def dump_to_json(dic, directory):
    outfile = open(directory, 'w')
    json.dump(dic, outfile)
    outfile.close()
    print(json.dumps(dic, indent=4))


def read_json_from_file(directory):
    infile = open(directory, 'r')
    dictionary = json.load(infile)
    infile.close()
    return dictionary


def add_to_database(dictionary):
    switch_dict = {
        'abilities': ability_dict,
        'armours': armour_dict,
        'armour_enchantments': armour_ench_dict,
        'characters': character_dict,
        'items':  item_dict,
        'item_enchantments': item_ench_dict,
        'races': race_dict,
        'race_traits': race_trait_dict,
        'traits': trait_dict,
        'weapons': weapon_dict,
        'weapon_enchantments': weapon_ench_dict
    }
    if dictionary in switch_dict.keys():
        append_dictionary(switch_dict[dictionary], '{}'.format(dictionary))
        dump_to_json(switch_dict[dictionary], 'data/{}.json'.format(dictionary))
    else:
        options = []
        for key in switch_dict:
            options.append(key)
        dictionary = input('valid options are {}, pick one: '.format(options))
        add_to_database(dictionary)


ability_dict = read_json_from_file('data/abilities.json')
armour_dict = read_json_from_file('data/armours.json')
armour_ench_dict = read_json_from_file('data/armour_enchantments.json')
character_dict = read_json_from_file('data/characters.json')
item_dict = read_json_from_file('data/items.json')
item_ench_dict = read_json_from_file('data/item_enchantments.json')
race_dict = read_json_from_file('data/races.json')
race_trait_dict = read_json_from_file('data/race_traits.json')
trait_dict = read_json_from_file('data/traits.json')
weapon_dict = read_json_from_file('data/weapons.json')
weapon_ench_dict = read_json_from_file('data/weapon_enchantments.json')

if __name__ == '__main__':
    dictionary = input('I want to add new: ')
    while dictionary != 'done':
        add_to_database(dictionary)
        dictionary = input('I want to add new: ')
