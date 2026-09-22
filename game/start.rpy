label start:
    call start_at(0)
    return

label start_at(i):
    $ quick_menu = False
    while i < len_scenes:
        call fx.log(f'# START {scenes[i]}')
        call expression scenes[i].label
        call fx.log(f"# END   {scenes[i]}")
        pause
        $ i += 1
    return