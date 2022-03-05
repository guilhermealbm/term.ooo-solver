from cgi import test
import reader
import pandas as pd
import numpy as np
from itertools import zip_longest

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_values = []


def best_initial_words(testing=False):
    # read json
    strings_series = pd.Series(reader.read_json())

    # clean special characters such as áãô...
    strings_series = strings_series.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    # create df
    df = pd.DataFrame(np.stack(strings_series.apply(list).values))
    df['word'] = strings_series

    # create letters frequency dict (exact positions)
    sliced_series = list(zip_longest(df[0].value_counts().sort_index(), df[1].value_counts().sort_index(), 
                                     df[2].value_counts().sort_index(), df[3].value_counts().sort_index(), 
                                     df[4].value_counts().sort_index(), fillvalue=0))
    letters_frequency_exact = dict(zip(letters, sliced_series))

    # create letters frequency dict (non-exact positions)
    for letter_values_tuples in sliced_series:
        letters_values.append(sum(letter_values_tuples))

    letters_frequency_general = dict(zip(letters, letters_values))

    # calculate scores
    df['exact_score'] = df.apply(lambda x: (letters_frequency_exact[x[0]][0]) + letters_frequency_exact[x[1]][1] + letters_frequency_exact[x[2]][2] + letters_frequency_exact[x[3]][3] + letters_frequency_exact[x[4]][4], axis = 1)
    df['general_score'] = df.apply(lambda x: (letters_frequency_general[x[0]]) + letters_frequency_general[x[1]] + letters_frequency_general[x[2]] + letters_frequency_general[x[3]] + letters_frequency_general[x[4]], axis = 1)

    # remove words with repeated letters
    df['word_set'] = df.apply(lambda x: ("".join(set(x['word']))), axis = 1)
    df_set = df[df['word_set'].map(len) == 5]

    # print(df.nlargest(5, 'exact_score'))
    print("Top 5 palavras: ")
    print(df_set.nlargest(5, 'general_score'))

    if testing:
        return df, letters_frequency_exact, letters_frequency_general
    receive_status(df, letters_frequency_exact, letters_frequency_general, first_time = True)


def receive_status(df, letters_frequency_exact, letters_frequency_general, first_time = False):
    print("Status: 1 = verde, 2 = amarelo e 3 = vermelho")
    status1 = ""
    if first_time:
        status1 = input("1a letra e status (ex: a1): ")
    else:
        status1 = input("1a letra e status: ")
    status2 = input("2a letra e status: ")
    status3 = input("3a letra e status: ")
    status4 = input("4a letra e status: ")
    status5 = input("5a letra e status: ")

    letters_tuple = (status1[0], status2[0], status3[0], status4[0], status5[0])
    status_tuple = (status1[1], status2[1], status3[1], status4[1], status5[1])
    guess_next_word(df, letters_frequency_exact, letters_frequency_general, letters_tuple, status_tuple)


def guess_next_word(df, letters_frequency_exact, letters_frequency_general, letters_tuple, 
                    status_tuple, testing=False):
    print(letters_tuple)
    print(status_tuple)
    discovered_letters = 0
    for attempt in status_tuple:
        discovered_letters += len([t for t in attempt if t != '3'])
    print(discovered_letters)

    if discovered_letters < 3:
        print("Continuar explorando")
        try_new_letters(df, letters_frequency_exact, letters_frequency_general, letters_tuple, status_tuple)
    else:
        print("Vamos tentar acertar")
        try_guess_word(df, letters_frequency_exact, letters_frequency_general, letters_tuple, status_tuple)

    if not testing:
        gameover = input("Acertou? S/n: ")
        if gameover != 'S':
            receive_status(df, letters_frequency_exact, letters_frequency_general, first_time = False)


def try_new_letters(df, letters_frequency_exact, letters_frequency_general, letters_tuple, status_tuple):
    for attempt in letters_tuple:
        df_set = df[df['word_set'].map(len) == 5]
        df_set = df_set[~df_set['word'].str.contains(attempt[0]) & ~df_set['word'].str.contains(attempt[1]) & 
                ~df_set['word'].str.contains(attempt[2]) & ~df_set['word'].str.contains(attempt[3]) & 
                ~df_set['word'].str.contains(attempt[4])]
    print("Top 5 palavras: ")
    print(df_set.nlargest(5, 'general_score'))


def try_guess_word(df, letters_frequency_exact, letters_frequency_general, letters_tuple, status_tuple):
    for i, attempt in enumerate(letters_tuple):
        for j, letter in enumerate(attempt):
            if status_tuple[i][j] == '1':
                df = df[df['word'].str[j] == letter]
            elif status_tuple[i][j] == '2':
                df = df[~(df['word'].str[j] == letter) & df['word'].str.contains(letter)]
            else:
                df = df[~df['word'].str.contains(letter)]

    print("Top 5 palavras: ")
    print(df.nlargest(5, 'exact_score'))


if __name__ == "__main__":
    best_initial_words()
