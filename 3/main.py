

def sort_files(file_list):
    sort_dict = dict()
    for file in file_list:
        with open(file, 'r', encoding='utf-8') as read_file:
            lines = read_file.read()
            len_lines = len(lines.split('\n'))
            sort_dict[len_lines] = [file, lines]
    with open('final_file.txt', 'w+', encoding='utf-8') as write_file:
        while len(sort_dict.keys()) > 0:
            write_string = f'{sort_dict[min(sort_dict.keys())][0]}\n{min(sort_dict.keys())}\n' \
                           f'{sort_dict[min(sort_dict.keys())][1]}\n'
            del sort_dict[min(sort_dict.keys())]
            write_file.write(write_string)
sort_files(['1.txt', '2.txt'])
