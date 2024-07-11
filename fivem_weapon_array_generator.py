import re

# OX INVENTORY CODE FROM ox_inventory/data/weapons.lua
commented_code = """
weapons = {
	['WEAPON_BATTLERIFLE'] = {
		label = 'Battle Rifle',
		weight = 3300,
		durability = 0.03,
		ammoname = 'ammo-rifle2',
	},
}
"""
weapon_names = re.findall(r"\['(WEAPON_[A-Z0-9_]+)'\]", commented_code)
weapon_names.sort()
formatted_output = "local weapons = {\n    '" + "',\n    '".join(weapon_names) + "'\n}"

print(formatted_output)
