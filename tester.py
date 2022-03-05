import main


def testMarch2():
    df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('a', 'r', 'e', 'i', 'o')], status_tuple=[('1', '1', '1', '3', '3')], testing=True)


def testMarch3():
    df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('a', 'r', 'e', 'i', 'o')], status_tuple=[('3', '3', '3', '3', '1')], testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('a', 'r', 'e', 'i', 'o'), ('s', 'h', 'u', 'n', 't')], 
            status_tuple=[('3', '3', '3', '3', '1'), ('2', '3', '2', '3', '2')], testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('a', 'r', 'e', 'i', 'o'), ('s', 'h', 'u', 'n', 't'), ('c', 'u', 's', 't', 'o')], 
            status_tuple=[('3', '3', '3', '3', '1'), ('2', '3', '2', '3', '2'), ('3', '1', '1', '1', '1')], testing=True)
    main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('a', 'r', 'e', 'i', 'o'), 
                ('s', 'h', 'u', 'n', 't'), 
                ('c', 'u', 's', 't', 'o'),
                ('b', 'u', 's', 't', 'o'),], 
            status_tuple=[('3', '3', '3', '3', '1'), 
                ('2', '3', '2', '3', '2'), 
                ('3', '1', '1', '1', '1'),
                ('3', '1', '1', '1', '1')], testing=True)

def testMarch4():
        df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('a', 'r', 'e', 'i', 'o')], status_tuple=[('1', '1', '3', '2', '1')], testing=True)

def testMarch5():
        df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('a', 'r', 'e', 'i', 'o')], status_tuple=[('2', '2', '3', '2', '3')], testing=True)
        df, letters_frequency_exact, letters_frequency_general = main.best_initial_words(testing=True)
        main.guess_next_word(df, letters_frequency_exact, letters_frequency_general, 
            letters_tuple=[('c', 'a', 'i', 'a', 'r')], status_tuple=[('3', '2', '1', '3', '2')], testing=True)

if __name__ == "__main__":
    #testMarch2()
    #testMarch3()
    #testMarch4()
    testMarch5()