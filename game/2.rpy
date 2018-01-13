label ya1:
    show A1 at left
    with dissolve
    S0 "Apa yang kamu ketahui lebih lanjut tentang STMIK Palangkaraya?"
    hide A1
    with dissolve
    menu:
        
        "Sejarah Singkat STMIK Palangkaraya":
            
            jump ya
        
        "Cara mendaftar sekolah di STMIK Palangkaraya ":
            
            jump daftar
        
        "Tempat-tempat diwilayah STMIK Palangkaraya?":
            
            jump tempat

        "Tidak,Cukup aku ingin keluar dari aplikasi ini..":
            
            jump tidak
    
    return
    

label daftar:
    with dissolve
    S0 "Baiklah.."
    S0 "Untuk mendaftar sekolah di STMIK Palangkaraya kamu bisa langsung ke situs resminya di..."
    S0 "{a=https://www.stmikplk.ac.id}stmikplk.ac.id{/a}"
    S0 "atau langsung ke STMIK Palangkaraya yang beralamatkan di {a=https://www.google.co.id/maps/place/STMIK+Palangka+RAYA/@-2.2282046,113.8945317,17z/data=!3m1!4b1!4m5!3m4!1s0x2dfcb319a220a98b:0x62c81a2f0c69f7d5!8m2!3d-2.2282046!4d113.8967204}Jl.G.Obos{/a}"
    S0 "Baiklah,selanjutnya.."
    jump ya1
    return
    
