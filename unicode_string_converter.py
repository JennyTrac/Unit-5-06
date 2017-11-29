# created by jenny trac
# created on nov 27 2017
# program takes a string and converts it to unicode values

import ui

def get_unicode_value(letter):
    # function to convert single letter to unicode number
    
    # create dictionary
    values_array = {'A': '65', 'B': '66', 'C': '67', 'D': '68', 'E': '69', 'F': '70',
                    'G': '71', 'H': '72', 'I': '73', 'J': '74', 'K': '75', 'L': '76',
                    'M': '77', 'N': '78', 'O': '79', 'P': '80', 'Q': '81', 'R': '82',
                    'S': '83', 'T': '84', 'U': '85', 'V': '86', 'W': '87', 'X': '88',
                    'Y': '89', 'Z': '90', 'a': '97', 'b': '98', 'c': '99', 'd': '100',
                    'e': '101', 'f': '102', 'g': '103', 'h': '104', 'i': '105', 'j': '106',
                    'k': '107', 'l': '108', 'm': '109', 'n': '110', 'o': '111', 'p': '112',
                    'q': '113', 'r': '114', 's': '115', 't': '116', 'u': '117', 'v': '118',
                    'w': '119', 'x': '120', 'y': '121', 'z': '122'}
    
    unicode_letter = values_array[letter]
    
    return unicode_letter

def get_unicode_values_touch_up_inside(sender):
    # button to get values
    
    # input
    the_word = str(view['word_textfield'].text)
    view['unicode_values_textview'].text = str(the_word)
    
    # process
    unicode_values = ' '
    for every_letter in the_word:
        next_unicode_value = get_unicode_value(every_letter)
        unicode_values = str(unicode_values) + str(next_unicode_value) + ", "
    
    # output
    view['unicode_values_textview'].text = str(unicode_values)

view = ui.load_view()
view.present('sheet')
