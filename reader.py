import json

def read_json():
    word_list = []
    f = open('dicionario.json', encoding='utf-8')

    data = json.load(f)

    for i in data:
        word_list.append(i['value'])
    
    f.close()
    return word_list

if __name__ == "__main__":
    print(read_json())