def heading(txt_str):
    while True:
        try:
            level = int(input('Level: '))
            if 1 <= level <= 6:
                text = input('Text: ')
                if txt_str == '':
                    heading = level * '#' + ' ' + text + '\n'
                    return heading
                else:
                    heading = '\n' + level * '#' + ' ' + text + '\n'
                    return heading
            else:
                print('The level should be within the range of 1 to 6')
                continue
        except ValueError:
            print('Provide int value not string')


def un_ordered_list(list_name='unordered', row_num=0, str_txt=None):
    if str_txt is None:
        str_txt = ''
    while True:
        try:
            row_num = int(input('Number of rows: '))
            if row_num <= 0:
                print('The number of rows should be greater than zero')
                continue
            break
        except ValueError:
            print('The number of rows should be greater than zero')
            continue

    if list_name == 'ordered':
        for i in range(row_num):
            row_text = input(f'Row #{i + 1}: ')
            str_txt += f'{i + 1}. {row_text}\n'
        return str_txt
    elif list_name == 'unordered':
        for i in range(row_num):
            row_text = input(f'Row #{i + 1}: ')
            str_txt += f'* {row_text}\n'
        return str_txt


def plain():
    text = input('Text: ')
    return text


def bold():
    bold_synt = '**'
    text = input('Text: ')
    return bold_synt + text + bold_synt


def italic():
    italic_symb = '*'
    text = input('Text: ')
    return italic_symb + text + italic_symb


def inline_code():
    code_symb = '`'
    text = input('Text: ')
    return code_symb + text + code_symb


def new_line():
    return '\n'


def link():
    label = input('Label: ')
    url = input('URL: ')
    return f'[{label}]({url})'


options_list = ('plain', 'bold', 'italic', 'header', 'link',
                'inline-code', 'new-line', 'unordered-list', 'ordered-list')
spec_comm = ('!help', '!done')

markdown_txt = ''

while True:
    usr_input = input('Choose a formatter:')
    if usr_input in options_list:
        if usr_input == 'header': markdown_txt += heading(markdown_txt)
        if usr_input == 'plain': markdown_txt += plain()
        if usr_input == 'bold': markdown_txt += bold()
        if usr_input == 'italic': markdown_txt += italic()
        if usr_input == 'inline-code': markdown_txt += inline_code()
        if usr_input == 'new-line': markdown_txt += new_line()
        if usr_input == 'link': markdown_txt += link()
        if usr_input == 'unordered-list': markdown_txt += un_ordered_list()
        if usr_input == 'ordered-list': markdown_txt += un_ordered_list('ordered')
        print(markdown_txt)
        continue
    elif usr_input == spec_comm[0]:
        print('Available formatters:', *options_list)
        print('Special commands:', *spec_comm)
    elif usr_input == spec_comm[1]:
        with open('output.md', 'w+') as f:
            f.write(markdown_txt)
        break
    else:
        print('Unknown formatting type or command')
