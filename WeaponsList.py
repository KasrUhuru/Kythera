# This is a rundown of all possible weapons and their associated stats
# Remember that all DnD ATTACK rolls to determine hit success use a d20.
# What changes across weapons is the DAMAGE roll based on weapon type

# Dexterity-based weapons defined using a Tuple
weapon_tuple = ("Damage Stat", "Damage Dice", "Damage Type", "Minimum Stat")

# Ranged Weapons
shortbow = (weapon_tuple, ["Dexterity", "d6", "Pierce", "10"])

longbow = (weapon_tuple, ["Dexterity", "d8", "Pierce", "12"])

crossbowLight = (weapon_tuple, ["Dexterity", "d8", "Pierce", "12"])

crossbowMedium = (weapon_tuple, ["Dexterity", "d10", "Pierce", "14"])

crossbowHeavy = (weapon_tuple, ["Dexterity", "d12", "Pierce", "14"])

ranged_weapons = {
    "shortbow": shortbow,
    "longbow": longbow,
    "crossbowLight": crossbowLight,
    "crossbowMedium": crossbowMedium,
    "crossbowHeavy": crossbowHeavy,
}

# Melee Dexterity Weapons
dagger = (weapon_tuple, ["Dexterity", "d4", "Pierce", "10"])

whip = (weapon_tuple, ["Dexterity", "d6", "Slash", "14"])

escrima = (weapon_tuple, ["Dexterity", "d6", "Blunt", "14"])

scimitar = (weapon_tuple, ["Dexterity", "d6", "Slash", "12"])

shortsword = (weapon_tuple, ["Dexterity", "d6", "Pierce", "10"])

rapier = (weapon_tuple, ["Dexterity", "d8", "Pierce", "14"])

quarterstaff = (weapon_tuple, ["Dexterity", "d8", "Blunt", "14"])

melee_STRweapons = {
    "dagger": dagger,
    "whip": whip,
    "escrima": escrima,
    "scimitar": scimitar,
    "shortsword": shortsword,
    "rapier": rapier,
    "quarterstaff": quarterstaff,
}

# /////////////////////////////////////////////////////////// #

# Melee Strength weapons list

hatchet = (weapon_tuple, ["Strength", "d6", "Slash", "10"])

machete = (weapon_tuple, ["Strength", "d6", "Slash", "10"])

mace = (weapon_tuple, ["Strength", "d6", "Blunt", "10"])

pickaxe = (weapon_tuple, ["Strength", "d6", "Pierce", "10"])

longsword = (weapon_tuple, ["Strength", "d8", "Slash", "12"])

warhammer = (weapon_tuple, ["Strength", "d8", "Blunt", "10"])

spear = (weapon_tuple, ["Strength", "d8", "Pierce", "10"])

claymore = (weapon_tuple, ["Strength", "d10", "Slash", "16"])

battleaxe = (weapon_tuple, ["Strength", "d10", "Slash", "14"])

maul = (weapon_tuple, ["Strength", "2d6", "Blunt", "16"])

horsechopper = (weapon_tuple, ["Strength", "2d6", "Slash", "16"])

melee_DEXweapons = {
    'hatchet': hatchet,
    'machete': machete,
    'mace': mace,
    'pickaxe': pickaxe,
    'longsword': longsword,
    'warhammer': warhammer,
    'spear': spear,
    'claymore': claymore,
    'battleaxe': battleaxe,
    'maul': maul,
    'horsechopper': horsechopper,
}

# /////////////////////////////////////////////////////////// #

# Intelligence-based weapons list.
# Intelligence weapons are as strong as the user's ability to visualize their intent.

# Lesser talismans are uncommon, yet extremely useful for travelers with no combat skills.
nen_talisman = (weapon_tuple, ["Intelligence", "d4", "Fire", "8"])

anut_talisman = (weapon_tuple, ["Intelligence", "d4", "Sonic", "8"])

wiv_talisman = (weapon_tuple, ["Intelligence", "d4", "Cold", "8"])

# Magic foci are intended for skilled practitioners of magical arts.
# These are favored by those who have gaps in arcane education.
runic_lantern = (weapon_tuple, ["Intelligence", "2d4", "Fire", "14"])

runic_quartz = (weapon_tuple, ["Intelligence", "2d4", "Cold", "14"])

tuning_alloy = (weapon_tuple, ["Intelligence", "2d4", "Sonic", "14"])

melee_INTweapons = {
    "nen talisman": nen_talisman,
    "anut talisman": anut_talisman,
    "wiv talisman": wiv_talisman,
    "runic lantern": runic_lantern,
    "runic quartz": runic_quartz,
    "tuning alloy": tuning_alloy,
}

all_weapons = [ranged_weapons,melee_STRweapons,melee_DEXweapons, melee_INTweapons]