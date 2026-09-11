testsuite testcases:
    teardown:
        exit

    testcase run_first_scene:
        run Jump('start')
        # last line of the scene
        advance until "Kono bangumi wa, goran no suponsaa no teikyou de okurishimasu."
        # and then one more
        advance

    testcase run_second_scene:
        run Jump('scene03')
        advance until "...we have a lot of work to do."
        advance

    testcase run_full_show:
        run Jump('start')
        advance until "We set out to save the world, but it turns out the world’s greatest threat is a kid who calls me mom." timeout 30
        advance