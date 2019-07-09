import json


weapon_dict = {}


def get_console_input(weapon_index):
    weapon = "weapon {}".format(weapon_index)
    name = input("Enter weapon name: ")
    flavour = input("Enter weapon type: ")
    damage = int(input("Enter max weapon damage: "))
    effect = input("Enter special effect: ")
    unique = input("Unique? (T/F): ")

    if unique == "T" or "t":
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


def print_info(attr_dict):
    key = list(attr_dict.keys())[0]
    print("Name: {}\n".format(attr_dict[key]["name"]),
          "Type: {}\n".format(attr_dict[key]["type"]),
          "Damage: {}\n".format(attr_dict[key]["damage"]),
          "Effect: {}\n".format(attr_dict[key]["aux_effect"]),
          "Unique: {}\n".format(attr_dict[key]["unique"]))


def append_dictionary(dictionary):
    dictionary.update(get_console_input(len(dictionary)))


def dump_to_json(dict):
    outfile = open('weapons.json', 'w')
    json.dump(dict, outfile)
    outfile.close()
    print(json.dumps(dict, indent=4))


def read_json_from_file():
    infile = open('weapons.json', 'r')
    dictionary = json.load(infile)
    infile.close()
    return dictionary


weapon_dict = read_json_from_file()
append_dictionary(weapon_dict)
dump_to_json(weapon_dict)
