label start:
    call start_at(0)
    return

label start_at(i):
    $ quick_menu = False
    while i < len_scenes:
        call fx.log(f'# {scenes[i]}')
        call expression scenes[i].label
        $ i += 1
    return