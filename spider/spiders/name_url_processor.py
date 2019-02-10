import json


if __name__ == '__main__':
    f = open('books_url.json', 'r')
    list = f.readlines()
    result = {}
    for strs in list:
        if strs[:1] != '[' and strs[:1] != ']':
            jsondict = None
            if strs[len(strs) - 3] == '}':
                jsondict = json.loads(strs[:len(strs) - 2])
            else:
                jsondict = json.loads(strs[:len(strs) - 1])
            d = dict(zip(jsondict.get("title"), jsondict.get("url")))
            result.update(d)
            # print(result)
    f.close()
    print(len(result.values()))
    w = open('books_url_map.json', 'w')
    w.write(str(result))
    w.close()
