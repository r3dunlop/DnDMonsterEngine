from bs4 import BeautifulSoup
import requests
#import urllib2
import re

def scrape_monster(monster_link):
    page_link = 'http://www.orcpub.com' + monster_link
    page_response = requests.get(page_link, timeout=5)
    soup = BeautifulSoup(page_response.content, "html.parser")
    monster_name = soup.find_all('span',itemprop = 'name')[-1].get_text()
    
    monster_info    = soup.find_all(class_ = 'char-details-section')
    monster_size    = monster_info[0].find_all('em')[0].get_text()
    monster_type    = monster_info[0].find_all('em')[1].get_text()
    monster_align   = monster_info[0].find_all('em', class_='m-l-5')[1].get_text()
    
    armor_class     = soup.find(string='Armor Class').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    hit_points      = soup.find(string='Hit Points').find_parent(class_='char-details-field').find(class_='m-l-5').get_text().split('(')[0]
    hit_die         = '(' + soup.find(string='Hit Points').find_parent(class_='char-details-field').find(class_='m-l-5').get_text().split('(')[1]
    speed           = soup.find(string='Speed').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    #str = soup.find_all('span')
    ability_label_str = soup.find(string='str').find_parent(class_='ability-label').find('div').get_text()
    ability_label_dex = soup.find(string='dex').find_parent(class_='ability-label').find('div').get_text()
    ability_label_con = soup.find(string='con').find_parent(class_='ability-label').find('div').get_text()
    ability_label_int = soup.find(string='int').find_parent(class_='ability-label').find('div').get_text()
    ability_label_wis = soup.find(string='wis').find_parent(class_='ability-label').find('div').get_text()
    ability_label_cha = soup.find(string='cha').find_parent(class_='ability-label').find('div').get_text()

    proficiency_bonus = soup.find(string='Proficiency Bonus').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    #saving throws are redundant
    skills = soup.find(string='Skills').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    senses = soup.find(string='Senses').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    languages = soup.find(string='Languages').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    challenge = soup.find(string='Challenge').find_parent(class_='char-details-field').find(class_='m-l-5').get_text()
    extra_html = soup.find_all(class_='col-xs-12 col-md-6')[0].find_all('strong')
    extras = ''
    actions = ''
    leg_actions = ''
    for i in extra_html:
        extras += i.get_text()
    action_html = soup.find(string='Actions').find_parent('div').find_all('strong')
    for i in action_html:
        actions += i.get_text()
    leg_action_html = soup.find(string='Legendary Actions').find_parent('div').find_all('strong')
    for i in leg_action_html:
        leg_actions += i.get_text()

    print(monster_name)
    print(monster_size + ' ' + monster_type + ', ' + monster_align)
    print('AC = ' + armor_class)
    print('HP = ' + hit_points + ' ' + hit_die)
    print('Speed = ' + speed)
    print('str = ' + ability_label_str)
    print('dex = ' + ability_label_dex)
    print('con = ' + ability_label_con)
    print('int = ' + ability_label_int)
    print('wis = ' + ability_label_wis)
    print('cha = ' + ability_label_cha)
    print('proficiency bonus = ' + proficiency_bonus)
    print('skills = ' + skills )
    print('senses = ' + senses )
    print('languages = ' + languages)
    print('challenge = ' + challenge)
    print('extras = ' + extras)
    print('actions = ' + actions)
    print('legendary = ' + leg_actions)
    print('*********')


page_link = 'http://www.orcpub.com/dungeons-and-dragons/5th-edition/monsters'

#Fetch the content from the url
page_response = requests.get(page_link, timeout=5)
#Use the html parser to parse the url content and store it in a variable.

soup = BeautifulSoup(page_response.content, "html.parser")
textContent = []

counter = 0
for link in soup.find_all('a'):
    if link.get('href') is not None and '/monsters/' in link.get('href'):
        #        print(link.get('href'))
        scrape_monster(link.get('href'))
        break


