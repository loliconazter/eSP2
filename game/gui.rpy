screen save:
    frame:
        style_group "mm"
        xalign .0
        yalign .0
        has vbox
        label _("Pilihan")
        textbutton _("   Kembali") action Return()
        textbutton _("Pengaturan ") action ShowMenu("preferences")
        textbutton _("  M.Utama ") action ShowMenu("m1")
        
init -2:
    style mm_button:
        size_group "mm"
    style mm_button_text:
        is default
        size 48       
screen m1():
    frame:
        style_group "mm"
        xalign .0
        yalign .0
        has vbox
        label _("Apakah yakin ingin kembali")
        label _("ke menu utama,atau anda")
        label _("ingin keluar aplikasi?")
        textbutton _("        Ya") action MainMenu(confirm=False)
        textbutton _("     Tidak") action Return()
        textbutton _("    Keluar") action Quit(confirm=False)
screen load():
    tag menu
    use navigation
screen help:
    frame:
        style_group "mm"
        xalign .0
        yalign .0
        has vbox
        label _("Pilihan")
        textbutton _("   Kembali") action Return()
        textbutton _("Pengaturan ") action ShowMenu("preferences")
        textbutton _("  M.Utama ") action ShowMenu("m1")     
init -2:
    style mm_button:
        size_group "mm"      
    style mm_button_text:
        is default
        size 48