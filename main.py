def count_char(f):
    dict_counter = {}
    for char in f:
        if char.lower() not in dict_counter:
            dict_counter[f'{char.lower()}'] = 1
        else:
            dict_counter[f'{char.lower()}'] += 1
    return dict_counter


def get_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    return len(text.split())


def dict_to_list(my_dict):
    return [{"char":k, "num":v} for k, v in my_dict.items()]


def sort_on(dict):
    return dict["num"]


def sort_letters(my_dict):
    li_dict = dict_to_list(my_dict)
    return li_dict.sort(reverse=True, key=sort_on)


def print_report(dic, num_words, path):
    print(f'--- Begin report of {path} ---')
    print(f'{num_words} words found in the document')
    print()
    for i in dic:
        if i["char"].isalpha():
            print(f"The '{i["char"]}' character was found {i["num"]} times")
    print('--- End report ---')

def main():
    path = 'books/frankenstein.txt'
    text = get_text(path)
    dict_1 = count_char(text) # create dictionary of chars: count
    dict_2 = dict_to_list(dict_1) # convert dictionary to a list of dictionaries
    dict_2.sort(reverse=True, key=sort_on)
    # print(dict_2)
    
    num_words = get_num_words(text)
    # dict_chars = count_char(text)
    # sorted_chars = sort_letters(dict_chars)
    print_report(dict_2, num_words, path)

if __name__ == '__main__':
    main()