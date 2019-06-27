from bs4 import BeautifulSoup
import requests
import re
import time
import monster as mn
#import actions as ac 
import csv

def scrape_monster(monster_link):
    page_link = 'http://www.orcpub.com' + monster_link
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    monster_name = soup.find_all('span',itemprop = 'name')[-1].get_text()
    
    monster = mn.Monster(monster_name)
    
    monster_info    = soup.find_all(class_ = 'char-details-section')
    monster.size    = monster_info[0].find_all('em')[0].get_text()
    monster.type    = monster_info[0].find_all('em')[1].get_text()
    monster.align   = monster_info[0].find_all('em', class_='m-l-5')[1].get_text()
    
    monster.armor_class     = soup.find(string='Armor Class').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    monster.hp      = soup.find(string='Hit Points').find_parent(class_='char-details-field').find(class_='m-l-5').get_text().split('(')[0]
    monster.hit_die         = '(' + soup.find(string='Hit Points').find_parent(class_='char-details-field').find(class_='m-l-5').get_text().split('(')[1]
    monster.speed           = soup.find(string='Speed').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    #str = soup.find_all('span')
    monster.str = soup.find(string='str').find_parent(class_='ability-label').find('div').get_text()
    monster.dex = soup.find(string='dex').find_parent(class_='ability-label').find('div').get_text()
    monster.con = soup.find(string='con').find_parent(class_='ability-label').find('div').get_text()
    monster.int = soup.find(string='int').find_parent(class_='ability-label').find('div').get_text()
    monster.wis = soup.find(string='wis').find_parent(class_='ability-label').find('div').get_text()
    monster.cha = soup.find(string='cha').find_parent(class_='ability-label').find('div').get_text()

    monster.proficiency = soup.find(string='Proficiency Bonus').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    #saving throws are redundant
    
    try:
        monster.skills = soup.find(string='Skills').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    except:
        monster.skills = ''

    try:
        monster.resistances = soup.find(string='Damage Resistances').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    except:
        monster.resistances = ''

    try:
        monster.immunities = soup.find(string='Damage Immunities').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    except:
        monster.immunities = ''

    try:
        monster.cond_immunities = soup.find(string='Condition Immunities').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    except:
        monster.cond_immunities = ''

    try:
        monster.senses = soup.find(string='Senses').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    except:
        monster.senses = ''

    try:
        monster.languages = soup.find(string='Languages').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    except:
        monster.languages = ''

    monster.challenge = soup.find(string='Challenge').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()

    monster.extras = ''
    monster.actions = ''
    monster.leg_actions = ''

    try:
        extra_html = soup.find_all(class_='col-xs-12 col-md-6')[0].find_all('strong')
        for i in extra_html:
            monster.extras += i.get_text()
        action_html = soup.find(string='Actions').find_parent('div').find_all('strong')
    except:
        monster.extras = ''

    try:
        action_html = soup.find(string='Actions').find_parent('div').find_all('strong')
        for i in action_html:
            monster.actions += i.get_text()
    except:
        monster.actions = ''

    try:
        leg_action_html = soup.find(string='Legendary Actions').find_parent('div').find_all('strong')
        for i in leg_action_html:
            monster.leg_actions += i.get_text()
    except:
        monster.leg_actions = ''

    return monster

page_link = 'http://www.orcpub.com/dungeons-and-dragons/5th-edition/monsters'
monster_filename = 'monsters.csv'
action_filename = 'actions.csv'


#Fetch the content from the url
page_response = requests.get(page_link, timeout=5)
#Use the html parser to parse the url content and store it in a variable.

soup = BeautifulSoup(page_response.content, "html.parser")
textContent = []


counter = 0

with open(monster_filename,'w') as monster_file, open(action_filename,'w') as action_file:
    csv_monster_writer = csv.writer(monster_file)
    csv_action_writer = csv.writer(action_file)
    csv_monster_writer.writerow(mn.Monster.header())
    csv_action_writer.writerow(['Monster Name'] + mn.Action.header())
    for link in soup.find_all('a'):
        if link.get('href') is not None and '/monsters/' in link.get('href'):
            #        print(link.get('href'))
            monster = scrape_monster(link.get('href'))
            monster.show()
            #csv_monster_writer.writerow(monster.property_list())
            break
            time.sleep(3) #Be nice to the website



