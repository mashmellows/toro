import os

def create_pos_n_neg():
    for file_type in ['neg']:

        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt','a') as f:
                    f.write(line)

create_pos_n_neg()
