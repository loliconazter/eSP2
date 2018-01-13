screen say(who, what, side_image=None, two_window=False):
    if not two_window:
        window:
            id "window"
            has vbox:
                style "say_vbox"
            if who:
                text who id "who"
            text what id "what"
    else:
        vbox:
            style "say_two_window_vbox"
            if who:
                window:
                    style "say_who_window"
                    text who:
                        id "who"
            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0
    use quick_menu


screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 20

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"
    use quick_menu
init -2:
    $ config.narrator_menu = False

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        yminimum int(config.screen_width * 0.1)
        ymaximum int(config.screen_width * 0.1)
        xminimum int(config.screen_width * 0.5)
        xmaximum int(config.screen_width * 0.5)


screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

screen main_menu():
    tag menu

    window:
        style "mm_root"

    frame:
        style_group "mm"
        xalign .0
        yalign .0

        has vbox
        label _("Menu Utama")
    
    frame:
        style_group "mm"
        xalign .50
        yalign .50

        has vbox
        textbutton _("     Mulai") action Start()
        textbutton _("Pengaturan") action ShowMenu("preferences")
        textbutton _("   Tentang") action ShowMenu("about")
        textbutton _("    Keluar") action Quit(confirm=False)
        
        
screen about():
    tag menu

    window:
        style "mm_root"

    frame:
        style_group "mm"
        xalign .0
        yalign .0

        has vbox
        label _("Tentang Aplikasi ")
        
    frame:
        style_group "mm"
        xalign .50
        yalign .50

        has vbox
        text _("eSP2 [config.version!t] C1357201064")
        text _(" Palangkaraya @2013")
        text _("{a=https://www.facebook.com/loliconazter}.Hubungi Pengembang.{/a}")
    
    frame:
        style_group "mm"
        xalign .50
        yalign .80

        has vbox
        textbutton _("   Kembali") action ShowMenu("main_menu")
        
    
        

init -2:

    style mm_button:
        size_group "mm"
        
    style mm_button_text:
        is default
        size 48

screen navigation():

    window:
        style "gm_root"
   
    frame:
        style_group "gm_nav"
        xalign .0
        yalign .0

        has vbox

init -2:

    style gm_nav_button:
        size_group "gm_nav"

screen preferences():
    tag menu
    use navigation
    grid 1 1:
        style_group "prefs"
        xfill True
        vbox:
            frame:
                label _("Pengaturan")
            frame:
                style_group "pref"
                has vbox
                label _("Tampilan(*versi desktop)")
                textbutton _("Layar Penuh") action Preference("display", "fullscreen")
                textbutton _("Tidak Layar Penuh") action Preference("display", "window")
            frame:
                style_group "pref"
                has vbox
                label _("Animasi Transisi")
                textbutton _("Aktif") action Preference("transitions", "all")
                textbutton _("Nonaktif") action Preference("transitions", "none")
                label _("Kecepatan teks")
                bar value Preference("text speed")
                label _("Musik")
                bar value Preference("music volume")
                label _("Efek Suara")
                bar value Preference("sound volume")
            frame:
                style_group "mm"
                xalign 0.55
                has vbox
                textbutton _("   Kembali") action Return()
                        
init -2:
    style pref_frame:
        xfill True
        xmargin 300
        top_margin 10
        bottom_margin 10
        left_margin 400
    
    style pref_label_text:
        is default
        size 40
    
    style pref_button_text:
        is default
        size 40

    style pref_vbox:
        xfill True

    style pref_button:
        size_group "pref"
        xalign 1.0

    style pref_slider:
        xmaximum 200
        xalign 1.0

    style soundtest_button:
        xalign 1.0

screen yesno_prompt(message, yes_action, no_action):
    modal False
    window:
        style "gm_root"
    frame:
        style_group "yesno"
        xfill True
        xmargin .05
        ypos .1
        yanchor 0
        ypadding .05
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label _(message):
            xalign 0.0
        hbox:
            xalign 0.5
            spacing 10

            textbutton _("Ya") action yes_action
            textbutton _("Tidak") action no_action
    key "game_menu" action no_action
    
init -2:
    style yesno_button:
        size_group "yesno"

    style yesno_label_text:
        text_align 0.5
        layout "subtitle"


screen quick_menu():
    hbox:
        style_group "mm"
        xalign 0.0
        yalign 0.0
        textbutton _("     Menu   ") action ShowMenu('help')
    hbox:
        style_group "mm"
        xalign 1.0
        yalign 0.0
        textbutton _("    Kembali  ") action Rollback()

init -2:
    style quick_button:
        is default
        background None
        xpadding 10
    style quick_button_text:
        is default
        size 48
        idle_color "#8888"
        hover_color "#ccc"
        selected_idle_color "#cc08"
        selected_hover_color "#cc0"
        insensitive_color "#4448"

