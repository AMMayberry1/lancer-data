import json

with open('LancerEngine\LancerEngine\lancer-data\lib\mods_orig.json') as f:
    systemData = json.load(f)

for system in systemData:
    if type(system["effect"]) is str:
        systemStr = system["effect"]
        system["effect"] = [{ "effect_type": "Generic", "detail" : systemStr }]
    elif type(system["effect"]) is dict:
        system["effect"] = [system["effect"]]
    elif type(system["effect"]) is not list:
        raise Exception(f"System {system['name']} has unexpected effect type: {type(system['effect'])}")

with open("LancerEngine\LancerEngine\lancer-data\lib\mods.json",'w') as f:
    json.dump(systemData, f, indent=4)