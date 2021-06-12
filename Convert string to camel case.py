def camel(text):
    tmp = [char for char in text]
    for i in range(len(text)):
        if tmp[i] == '-' or tmp[i] == '_':
            tmp[i + 1] = tmp[i + 1].capitalize()
            tmp[i] = ''

    string = ''.join([str(item) for item in tmp])
    return string


if __name__ == '__main__':
    text = 'The-stealth-warrior'
    print(camel(text))
