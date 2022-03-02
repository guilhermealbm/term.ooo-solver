import reader
import pandas as pd
import numpy as np
from itertools import zip_longest

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
letters_values = []

def best_initial_words():
    # read json
    strings_series = pd.Series(reader.read_json())

    # clean special characters such as áãô...
    strings_series = strings_series.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8')

    # create df
    df = pd.DataFrame(np.stack(strings_series.apply(list).values))
    df['word'] = strings_series

    # create letters frequency dict (exact positions)
    sliced_series = list(zip_longest(df[0].value_counts().sort_index(), df[1].value_counts().sort_index(), df[2].value_counts().sort_index(), df[3].value_counts().sort_index(), df[4].value_counts().sort_index(), fillvalue=0))
    letters_frequency_exact = dict(zip(letters, sliced_series))

    # create letters frequency dict (non-exact positions)
    for letter_values_tuples in sliced_series:
        letters_values.append(sum(letter_values_tuples))

    letters_frequency_general = dict(zip(letters, letters_values))

    # remove words with repeated letters
    df['word_set'] = df.apply(lambda x: ("".join(set(x['word']))), axis = 1)
    df = df[df['word_set'].map(len) == 5]

    # calculate scores
    df['exact_score'] = df.apply(lambda x: (letters_frequency_exact[x[0]][0]) + letters_frequency_exact[x[1]][1] + letters_frequency_exact[x[2]][2] + letters_frequency_exact[x[3]][3] + letters_frequency_exact[x[4]][4], axis = 1)
    df['general_score'] = df.apply(lambda x: (letters_frequency_general[x[0]]) + letters_frequency_general[x[1]] + letters_frequency_general[x[2]] + letters_frequency_general[x[3]] + letters_frequency_general[x[4]], axis = 1)

    # print(df.nlargest(5, 'exact_score'))
    print(df.nlargest(5, 'general_score'))


if __name__ == "__main__":
    best_initial_words()
