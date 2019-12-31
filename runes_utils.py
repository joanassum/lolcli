paths = ['Precision','Domination','Sorcery','Resolve','Inspiration']
colour = ['yellow', 'red', 'purple', 'green', 'lightblue']

keystones = {
    "Precision": ["Press the Attack", "Lethal Tempo", "Fleet Footwork", "Conqueror"],
    "Domination": ["Electrocute", "Predator", "Dark Harvest", "Hall of Blades"],
    "Sorcery": ["Summon Aery", "Arcane Comet", "Phase Rush"],
    "Resolve": ["Grasp of the Undying", "Aftershock", "Guardian"],
    "Inspiration": ["Glacial Augment", "Unsealed Spellbook", "Prototype: Omnistone"],
}

slot1 = {
    "Precision": ["Overheal", "Triumph", "Presence of Mind"],
    "Domination": ["Cheap Shot", "Taste of Blood", "Sudden Impact"],
    "Sorcery": ["Nullifying Orb", "Manaflow Band", "Nimbus Cloak"],
    "Resolve": ["Demolish", "Font of Life", "Shield Bash"],
    "Inspiration": ["Hextech Flashtraption", "Magical Footware", "Perfect Timing"],
}
slot2 = {
    "Precision": ["Legend: Alacrity", "Legend: Tenacity", "Legend: Bloodline"],
    "Domination": ["Zombie Ward", "Ghost Poro", "Eyeball Collection"],
    "Sorcery": ["Transcendence", "Celerity", "Absolute Focus"],
    "Resolve": ["Conditioning", "Second Wind", "Bone Plating"],
    "Inspiration": ["Future's Market", "Minion Dematerializer", "Biscuit Delivery"],
}
slot3 = {
    "Precision": ["Coup de Grace", "Cut Down", "Last Stand"],
    "Domination": ["Ravenous Hunter", "Ingenious Hunter", "Relentless Hunter", "Ultimate Hunter"],
    "Sorcery": ["Scorch", "Waterwalking", "Gathering Storm"],
    "Resolve": ["Overgrowth", "Revitalize", "Unflinching"],
    "Inspiration": ["Cosmic Insight", "Approach Velocity", "Time Warp Tonic"],
}

def get_keystones(answers):
    return keystones[answers['primarypath']]

def get_primary_slot1(answers):
    return slot1[answers['primarypath']]

def get_primary_slot2(answers):
    return slot2[answers['primarypath']]

def get_primary_slot3(answers):
    return slot3[answers['primarypath']]

def get_secondary_path(answers):
    return [x for x in paths if x != answers['primarypath']]

def get_secondary_slot1(answers):
    return slot1[answers['secondarypath']] + slot2[answers['secondarypath']] + slot3[answers['secondarypath']]

def get_secondary_slot2(answers):
    all_slots = slot1[answers['secondarypath']] + slot2[answers['secondarypath']] + slot3[answers['secondarypath']]
    return [x for x in all_slots if x != answers['secondaryslot1']]

def get_questions():
    return [
        {
            'type': 'list',
            'name': 'primarypath',
            'message': 'Primary Path?',
            'choices': paths
        },
        {
            'type': 'list',
            'name': 'keystone',
            'message': 'Keystone?',
            'choices': get_keystones
        },
        {
            'type': 'list',
            'name': 'primaryslot1',
            'message': 'Primary slot 1?',
            'choices': get_primary_slot1
        },
        {
            'type': 'list',
            'name': 'primaryslot2',
            'message': 'Primary slot 2?',
            'choices': get_primary_slot2
        },
        {
            'type': 'list',
            'name': 'primaryslot3',
            'message': 'Primary slot 3?',
            'choices': get_primary_slot3
        },
        {
            'type': 'list',
            'name': 'secondarypath',
            'message': 'Secondary Path?',
            'choices': get_secondary_path
        },
        {
            'type': 'list',
            'name': 'secondaryslot1',
            'message': 'Secondary slot 1?',
            'choices': get_secondary_slot1
        },
        {
            'type': 'list',
            'name': 'secondaryslot2',
            'message': 'Secondary slot 2?',
            'choices': get_secondary_slot2
        },
        {
            'type': 'list',
            'name': 'offensive',
            'message': 'Shard -- Offensive?',
            'choices': [
                "1. +9 Adaptive Force",
                "2. +10%% Attack Speed",
                "3. +1%%-10%% (based on level) Cooldown Reduction"
            ]
        },
        {
            'type': 'list',
            'name': 'flex',
            'message': 'Shard -- Flex?',
            'choices': [
                "1. +9 Adaptive Force",
                "2. +6 Armor",
                "3. +8 Magic Resistance"
            ]
        },
        {
            'type': 'list',
            'name': 'defence',
            'message': 'Shard -- Defence?',
            'choices': [
                "1. +15-90 (based on level) Health",
                "2. +6 Armor",
                "3. +8 Magic Resistance"
            ]
        },
    ]

def simplify_output(runes):
    # Get the colour of the primary path
    primarypath = runes['primarypath']
    primarypathcolour = colour[paths.index(primarypath)]

    # Get the index of selected keystone and slots of the primary path
    keystoneindex = str(keystones[primarypath].index(runes['keystone'])+1)
    primaryslot1index = str(slot1[primarypath].index(runes['primaryslot1'])+1)
    primaryslot2index = str(slot2[primarypath].index(runes['primaryslot2'])+1)
    primaryslot3index = str(slot3[primarypath].index(runes['primaryslot3'])+1)

    # Get the colour of the secondary path
    secondarypath = runes['secondarypath']
    secondarypathcolour = colour[paths.index(secondarypath)]

    # Get the index of slots of the secondary path
    second_slots = slot1[secondarypath] + slot2[secondarypath] + slot3[secondarypath]
    secondaryslot1index = str(second_slots.index(runes['secondaryslot1'])+1)
    secondaryslot2index = str(second_slots.index(runes['secondaryslot2'])+1)

    # Construct the simplified output
    output = primarypathcolour + " " + keystoneindex + " " + primaryslot1index  + " " + primaryslot2index  + " " + primaryslot3index 
    output += " || " + secondarypathcolour + " " + secondaryslot1index + " " + secondaryslot2index 
    output += " || " + runes['offensive'][0] + " " + runes['flex'][0] + " " + runes['defence'][0]
    return output


