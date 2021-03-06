import os
import sys
from collections import Counter
import json

#import language recognizer
#please enter "$ pip install cld2-cffi" in terminal before testing this program
import cld2


#kid safe description
def kid_safe(words):
    bad_words = set()
    with open("bad_words.txt") as fp:
        for line in fp.readlines():
            bad_words.add(line.replace("\n", ""))
    num = 0
    for word in words.keys():
        if word in bad_words:
            num += 1
    return min(1, 1 - num / 10)

# adding love function 
def love(words):
    love_words = ["love", 'loved', 'loving',"lovesick", 
                  "lovestruck", 'hug', 'sex', 'husband', 
                  'wife', 'affection', 'amour', 'amore',
                  "crush", "infatuation", "romantic", 'forever',
                  'passion', 'romance', "darling", "marriage",
                  "proposal", "sweet", "honey", "kiss", 
                  'kisses', "miss", "heart", 'caring', 'fancy']
    num = 0
    for word in words.keys():
        if word in love_words:
            num += 1
    return 1.0 * num / 5

#mood description
def mood(words):
    happy_words = ["happy", 'happiness', "excited", "high",
                   "proud", "perfect", "joy", "joyful",
                   "hope", "confident", "powerful", "sweet",
                   "nice", "love", "exciting", "amuse",
                   "amazing", "happily", "great", "lucky",
                   'beaming', 'cheerful', 'cheer', 'radiant',
                   'merry', 'wonder', 'wonderful', 'delight',
                   'delightful', 'glad', 'sprightly', 'felicity',
                   'glorified', 'nirvana', 'enlightenment',
                   'blessedness', 'blissful', 'bliss', 'upbeat',
                   'jubilant', 'glorious', 'fanciful', 'elated',
                   'exciting', 'excitement', 'pleased', 'blithe',
                   'exstatic', 'convival', 'cheery', 'dazed',
                   'chirpy', 'glorious', 'felicitous', 'laugh',
                   'laughing', 'laughter','hilarious', 'lively',
                   'mirth', 'mirthful', 'intoxicated', 'perky',
                   'sanguine', 'splendid', 'zestful', 'sybaritic',
                   'satisfied', 'optimistic', 'joyous', 'pleasant',
                   'content', 'jubilant', 'rejoicing', 'tickled',
                   'enraptured', 'euphoric', 'overjoyed', 'rapturous',
                   'thrilled', 'exuberant', 'animated', 'dynamic',
                   'spirited', 'gay', 'jaunty', 'resilient', 'vivacious',
                   'energized', 'zealous', 'hopeful']
    
    sad_words = ["sad", 'sadness', "down", "low", "sorry", 
                 "tear", "war", "bitter",'bad', 'annoy',
                 'hard','hate','cry', 'cold','criminal',
                 'cruel','dirty','fell','guilty','hurt',
                 'jealous','lose','lost','poor','scared',
                 'scary','sinister','terrible', 'unhappy',
                 'ugly','wary', 'depress', 'depressed',
                 'depressing', 'disappointed', 'unfriendly',
                 'hopeless', 'disturbed', 'grave',
                 'melancholy', 'miserable', 'sorrow',
                 'sorrowful', 'sorrowness', 'troubled', 'upset',
                 'discouraged', 'dissatisfied', 'forsaken',
                 'morose', 'pained', 'painful', 'unfortunate',
                 'pensive', 'wistful', 'deplorable', 'doleful',
                 'lamentable', 'mournful', 'pitiful', 'tragic',
                 'tragical', 'blue', 'brokenhearted', 'brokenheart',
                 'distressed', 'crestfallen', 'miserable', 'woeful',
                 'woe', 'dejected', 'despondent', 'disconsolate',
                 'downcast', 'downhearted', 'droopy', 'forlorn',
                 'gloomy', 'glum', 'hangdog', 'heartbroken',
                 'heartsick', 'heartsore', 'heavyhearted',
                 'inconsolable', 'joyless', 'low-spirited',
                 'melancholic', 'saddened', 'woebegone', 'wretched',
                 'aggrieved', 'distress', 'uneasy', 'unquiet',
                 'worried', 'worry', 'worries', 'despairing',
                 'sunk', 'disheartened', 'dispirited','suicidal',
                 'dolorous', 'lachrymose', 'lugubrious', 'plaintive',
                 'tearful', 'regretful', 'rueful', 'agonized', 'agony',
                 'agonize', 'anguished', 'grieving', 'grief', 'wailing',
                 'weeping', 'weep', 'weeps', 'bleak', 'cheerless',
                 'comfortless', 'dark', 'darkening', 'desolate',
                 'dismal', 'drear', 'dreary', 'elegiac', 'elegiacal',
                 'funereal', 'gray', 'grey', 'morbid', 'morose', 'murky',
                 'saturnine', 'somber', 'sombre', 'sullen', 'cried',
                 'cries', 'weep', 'weeping', 'weeps', 'crying']
    
    happy_num = 0
    sad_num = 0

    for word in words.keys():
        if word in happy_words:
            happy_num += 1
        if word in sad_words:
            sad_num += 1
    if (sad_num == 0 and happy_num == 0):
        return 0.5
    elif sad_num == 0 and happy_num != 0:
        return 1.0
        
    elif sad_num != 0 and happy_num == 0:
        return 0.0 #float(1.0 - sad_num/5.0)
    
    elif sad_num != 0 and happy_num!=0:
        if sad_num == happy_num:
            return 0.5
        else:
            ratio = float(happy_num / (sad_num + happy_num))
            return round(ratio, 1)

#added length function
def length(words):
    return round(min(1.0, sum(words.values()) / 300), 1)

#complexity description
def complexity(words):
    gre = set()
    with open("gre.txt") as fp:
        for line in fp.readlines():
            gre.add(line.replace("\n", ""))
    num = 0
    for word in words.keys():
        if word in gre:
            num += 1
    
    return min(1.0, 1.0 * num / 5)


#Reading lyrics file and giving output
def read_data(file_path):
    data = {"characterizations": []}
    for i in os.listdir(file_path):
        item = {}
        infos = i.split("~")
        item["id"] = int(infos[0])
        item['artist'] = infos[1].replace("-", " ")
        item["title"] = infos[2].replace("-", " ").strip('.txt')
        file_name = os.path.join(file_path, i)
        words = []
        
        with open(file_name, encoding='utf-8') as fp:
            for line in fp.readlines():
                if item.get("language"):
                    pass
                else:
                    item["language"] = cld2.detect(line)[2][0][0]
        
        with open(file_name, encoding='utf-8') as fp:
            for line in fp.readlines():
                line = line.replace("\n", "").split(" ")
                for word in line:
                    words.append(word.lower())
        words = Counter(words)
        item["kid_safe"] = kid_safe(words)
        item["love"] = love(words)
        item["mood"] = mood(words)
        item["length"] = length(words)
        item["complexity"] = complexity(words)
        data["characterizations"].append(item)
    return data


#read file path from command line
if __name__ == "__main__":
    
    import argparse
    parser = argparse.ArgumentParser('Input file path for lyrics')
    parser.add_argument('file_path', help='path where the lyrics are stored')
    args = parser.parse_args()

    data=read_data(args.file_path)
    
    with open('CSV-JSON-lyrics-out.json', 'w') as fp:
        json.dump(
            obj=data,
            fp=fp,
            indent=True,  # pretty printing
            #sort_keys=True,  # sorting for easier lookup by a human, sort alphebetically
        )
    with open('CSV-JSON-lyrics-out.json','r') as fp:
        print_data = json.load(fp)
    
        print(print_data)
