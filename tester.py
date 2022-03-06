import main


def testMarch2():
    df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio'], status=['11133'], testing=True)


def testMarch3():
    df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio'], status=['33331'], testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio', 'shunt'], 
            status=['33331', '23232'], testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio', 'shunt', 'custo'], 
            status=['33331', '23232', '31111'], testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio', 
                'shunt', 
                'custo',
                'busto'], 
            status=['33331', 
                '23232', 
                '31111',
                '31111'], testing=True)

def testMarch4():
        df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio'], status=['11321'], testing=True)

def testMarch5():
        df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio'], status=['22323'], testing=True)
        df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio', 
            'caiar'], 
            status=['22323', 
            '32132'], testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio', 
            'caiar',
            'ruina'], 
            status=['22323', 
            '32132',
            '11131'], testing=True)

def testMarch6():
        df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio'], status=['23313'], testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            words=['areio', 'shunt'], status=['23313', '33233'], testing=True)

if __name__ == "__main__":
    testMarch6()