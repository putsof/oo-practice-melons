############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""
        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.name = name

        # Fill in the rest

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []
    musk = MelonType('musk',
                    1998,
                    'green',
                    True,
                    True,
                    'Muskmelon',)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas',
                    2003,
                    'orange',
                    True,
                    True,
                    'Casaba')
    cas.add_pairing(['strawberries', 'mint'])
    all_melon_types.append(cas)

    cren = MelonType('cren',
                    1996,
                    'green',
                    False,
                    False,
                    'Crenshaw')
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)

    yw = MelonType('yw',
                    2013,
                    'yellow',
                    True,
                    False,
                    'Yellow Watermelon')
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with - {melon.pairings}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    dict_ = {}
    for melon in melon_types:
        dict_[melon.code] = melon.name
    return dict_

# print_pairing_info(make_melon_types())
# print(make_melon_type_lookup(make_melon_types()))
############
# Part 2   #
############


class Melon:
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods
    def __init__(self, m_type, shape, color, field, harvester):
        self.m_type = m_type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester

    def is_sellable(self):
        if self.shape > 5 and self.color > 5:
            return True
        else:
            return False



def make_melons(melon_types):
    """Returns a list of Melon objects."""
    melon_by_id = make_melon_type_lookup(melon_types)
    melons_list = []

    melon_one = Melon(melon_by_id['yw'],8,7,2,'Sheila')
    melons_list.append(melon_one)

    melon_two = Melon(melon_by_id['yw'],3,4,2,'Sheila')
    melons_list.append(melon_two)

    melon_three = Melon(melon_by_id['yw'],9,8,3,'Sheila')
    melons_list.append(melon_three)

    melon_four = Melon(melon_by_id['cas'], 10,6,35,'Sheila')
    melons_list.append(melon_four)

    melon_five = Melon(melon_by_id['cren'],8,9,35,'Michael')
    melons_list.append(melon_five)

    melon_six = Melon(melon_by_id['cren'],8,2,35,'Michael')
    melons_list.append(melon_six)

    melon_seven = Melon(melon_by_id['cren'],2,3,4,'Michael')
    melons_list.append(melon_seven)

    melon_eight = Melon(melon_by_id['musk'],6,7,4,'Michael')
    melons_list.append(melon_eight)

    melon_nine = Melon(melon_by_id['yw'],7,10,3,'Sheila')
    melons_list.append(melon_nine)

    return melons_list



def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    for melon in melons:
        if melon.is_sellable == True:
            print(f"Harvested by {melon.harvester} from Field {melon.field} (CAN BE SOLD)")
        else:
            print(f"Harvested by {melon.harvester} from Field {melon.field} (NOT SELLABLE)")


get_sellability_report(make_melons(make_melon_type_lookup(make_melon_types())))
