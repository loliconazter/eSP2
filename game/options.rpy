init -1 python hide:
    config.developer = False
    config.screen_width = 1280
    config.screen_height = 720
    style.default.size = 30
    config.window_title = u"eSP2"
    config.name = ""
    config.version = "0.0"
    theme.marker(
        widget = "#003c78",
        widget_hover = "#0050a0",
        widget_text = "#c8ffff",
        widget_selected = "#ffffc8",
        disabled = "#404040",
        disabled_text = "#c8c8c8",
        label = "#ffffff",
        frame = "#6496c8",
        mm_root = "#dcebff",
        gm_root = "#dcebff",
        rounded_window = True,
        )
    config.has_sound = True
    config.has_music = True
    style.button.activate_sound = "click.wav"
    style.imagemap.activate_sound = "click.wav"
    config.enter_sound = "click.wav"
    config.exit_sound = "click.wav"
    config.sample_sound = "click.wav"
    config.enter_transition = Dissolve(.25)
    config.exit_transition = Dissolve(.25)
    config.intra_transition = Dissolve(.25)
    config.main_game_transition = Dissolve(.25)
    config.game_main_transition = Dissolve(.25)
    config.end_splash_transition = Dissolve(.25)
    config.end_game_transition = Dissolve(.25)
    config.window_show_transition = Dissolve(.25)
    config.window_hide_transition = Dissolve(.25)
    config.enter_yesno_transition = Dissolve(.25)
    config.exit_yesno_transition = Dissolve(.25)
    config.enter_replay_transition = Dissolve(.25)
    config.exit_replay_transition = Dissolve(.25)
    config.main_menu_music = "menu.ogg"
init -1 python hide:
    config.default_fullscreen = True
    config.default_text_cps = 100
    config.default_afm_time = 100
    config.default_afm_enable = True
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
init python:
    build.directory_name = "loliconazterProject"
    build.executable_name = "eSP2"
    build.include_update = True
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    