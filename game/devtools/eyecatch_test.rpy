label eyecatch_test:
    $ i = 0
    while i < len(eyecatch_labels):
        "[eyecatch_labels[i]]:"
        call expression eyecatch_labels[i]
        $ i += 1
    return