class Action:
    def __init__(self, name, description, type):
        self.name = name
        self.description = description
        self.type = type
    
    def header():
        return ['Name','Description','Type']

    def tolist(self):
        return [self.name,self.description,self.type]


class Monster:
    def __init__(self, name):
        self.name = name
        self.size = None
        self.type = None
        self.align= None
        self.armor_class = None
        self.hp = None
        self.hit_die = None
        self.speed = None
        self.str = None
        self.dex = None
        self.con = None
        self.int = None
        self.wis = None
        self.cha = None
        self.proficiency = None
        self.skills = None
        self.resistances = None
        self.immunities = None
        self.cond_immunities = None
        self.senses = None
        self.languages = None
        self.challenege = None
        self.extras = None
        self.actions = None
        self.leg_actions = None
        self.action_list = []

    def show(self):
        print(self.name)
        print(self.size + ' ' + self.type + ', ' + self.align)
        print('AC = ' + self.armor_class)
        print('HP = ' + self.hp + ' ' + self.hit_die)
        print('Speed = ' + self.speed)
        print('str = ' + self.str)
        print('dex = ' + self.dex)
        print('con = ' + self.con)
        print('int = ' + self.int)
        print('wis = ' + self.wis)
        print('cha = ' + self.cha)
        print('proficiency bonus = ' + self.proficiency)
        print('skills = ' + self.skills )
        print('resistances = ' + self.resistances)
        print('dam immunities = ' + self.immunities)
        print('cond immunities = ' + self.cond_immunities)
        print('senses = ' + self.senses )
        print('languages = ' + self.languages)
        print('challenge = ' + self.challenge)
        print('extras = ' + self.extras)
        print('actions = ' + self.actions)
        print('legendary = ' + self.leg_actions)
    
    def property_list(self):
        return [self.name,self.size,self.type,self.align,self.armor_class,self.hp,self.hit_die,self.speed,self.str,self.dex,self.con,self.int,self.wis,self.cha,self.proficiency,self.skills,self.resistances,self.immunities,self.cond_immunities,self.senses,self.languages,self.challenge,self.extras,self.actions,self.leg_actions]

    def header():
        return ['Name','Size','Type','Alignment','AC','HP','Hit Die','Speed','Str','Dex','Con','Int','Wis','Cha','Proficiency','Skills','Resistance','Immunity','Condition Immunity','Senses','Languages','CR','Extras','Actions','Leg Actions']

    def add_action(self,action):
        self.action_list.append(action)


