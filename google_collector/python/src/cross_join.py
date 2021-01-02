with open('cat_marine') as categ:
    for cat in categ:
        with open('mots_marine') as words:
            for word in words:
                print(f'{cat.rstrip()} {word.rstrip()}')
