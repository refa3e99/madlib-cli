import re

welcome_message = '''
welcome to midlab game
enjoy the game!
'''

print(welcome_message)

def read_template(path):
    try:
        with open(path,'r') as file:
            content = file.read()
        return content
    except  FileNotFoundError as err:
        raise err

def parse_template(string):
    regx = r'{([^}]+)}'
    language_parts = tuple(re.findall(regx,string))
    initStr = re.sub(regx, "{}", string)
    return initStr, language_parts

def merge(bare_tmplt,user_input):
    string = parse_template(bare_tmplt)[0]
    "invoked_tmplt = bare_tmplt.format(*user_input)"
    return string.format(*user_input)


def start_game():
    word0 = input('give me an adjective : ')
    word1 = input('give me an adjective : ')
    word2 = input('give me a name : ')
    word3 = input('give me a Past Tense Verb : ')
    word4 = input('give me a name : ')
    word5 = input('give me an adjective : ')
    word6 = input('give me an adjective : ')
    word7 = input('give me a Plural Noun : ')
    word8 = input('give me a Large Animal : ')
    word9 = input('give me a Small Animal : ')
    word10 = input('give me A Girl\'s Name : ')
    word11 = input('give me an adjective : ')
    word12 = input('give me a Plural Noun : ')
    word13 = input('give me an adjective : ')
    word14 = input('give me a Plural Noun : ')
    word15 = input('give me a number between 1 and 50 : ')
    word16 = input('give me a name : ')
    word17 = input('give me a number : ')
    word18 = input('give me a Plural Noun : ')
    word19 = input('give me a Number : ')
    word20 = input('give me a Plural Noun : ')
    user_input = (word0,word1,word2,word3,word4,word5,word6,word7,word8,word9,word10,word11,word12,word13,word14,word15,word16,word17,word18,word19,word20)

    path = "../assets/template.txt"

    content = read_template(path)
    parsed_content = parse_template(content)
    readable_content = merge(parsed_content,user_input)

    # Uncomment to copy text to a new file
    #f = open("newFile.txt", "w")
    #f.write(readable_content)
    #f.close()

    print(readable_content)