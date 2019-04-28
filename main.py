import os
import sys
from collections import Counter

#rearrange file read path

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
    love_words = {"love", "lovesick", "lovestruck", "crush", "infatuation", "romantic", "darling", "marriage",
                  "proposal", "loved", "sweet", "honey", "kiss", "miss", "heart"}
    num = 0
    for word in words.keys():
        if word in love_words:
            num += 1
    return 1.0 * num / 5

#mood description
def mood(words):
    happy_words = {"happy", "excited", "high", "proud", "perfect", "joy", "joyful", "hope", "confiedent", "powerful", "sweet", "nice", "love", "exciting", "amuse", "amazing", "happily", "great", "lucky"}
    sad_words = {"sad", "down", "low", "sorry", "tear", "war", "bitter",'bad', 'annoy','hard','hate','cry', 'cold','criminal','cruel','dirty','fell','guilty','hurt','jealous','lose','lost','poor','scared','scary','sinister','terrible',
                'unhappy','ugly','wary'}
    happy_num = 0
    sad_num = 0

    for word in words.keys():
        if word in happy_words:
            happy_num += 1
        if word in sad_words:
            sad_num += 1
    if sad_num == 0:
        if happy_num == 0:
            return 0.5
        return 1

    return min(1.0, 1.0 * happy_num / sad_num)

#added length function
def length(words):
    # print (sum(words.values())/300)
    
    a=sum(words.values()) / 300
    return min(1.0,"{0:.2f}".format(a))


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
    
    return min(1.0, "%.2f" % a 1.0 * num / 5)

#Reading lyrics file and giving output
def read_data(file_path):
    data = {"characterizations": []}
    for i in os.listdir(file_path):
        item = {}
        infos = i.split("~")
        item["id"] = int(infos[0])
        item['artist'] = infos[1].replace("-", " ")
        item["title"] = infos[2].replace("-", " ")
        file_name = os.path.join(file_path, i)
        words = []
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
    print (data)
    
    
    
    #file_path = sys.argv[1]
    #data = read_data(file_path)
    #print(data)
