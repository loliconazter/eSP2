label tempat:
    show A1 at left
    with dissolve
    S0 "Tempat mana yang kamu ketahui lebih lanjut di STMIK Palangkaraya?"
    hide A1
    with dissolve
    menu:
        
        "Ruang kelas":
            
            jump tempat1
            
        "Perpustakaan":
            
            jump tempat2
        
        "Ruang Laboratorium":
            jump tempat3
            
        "Tempat Lainnya...":
            jump tempatE
        
            
#kelas
label tempat1:
    scene BG4
    with dissolve
    S0 "Selamat datang di ruang kelas STMIK Palangkaraya.."
    S0 "Disini adalah tempat dimana dilakukan proses belajar mengajar namun secara teori.."
    S0 "Baiklah,selanjutnya..."
    scene BG3
    with dissolve
    jump tempat
    
#perpustakaan    
label tempat2:
    scene BG5
    with dissolve
    S0 "Selamat datang di ruang perpustakaan STMIK Palangkaraya.."
    S3 "Disini adalah tempat kamu membaca buku atau pun sesuatu yang bisa kamu baca.."
    scene BG6
    with dissolve
    S0 "hingga e-book yang disediakan oleh para petugas purpustakaan.."
    S0 "diperpustakaan juga terdapat fasilitas wifi untuk menunjang proses belajar"
    S0 "Baiklah,selanjutnya..."
    scene BG3
    with dissolve
    jump tempat

#laboratorium    
label tempat3:
    scene BG8
    with dissolve
    S0 "Selamat datang di laboratorium komputer STMIK Palangkaraya.."
    S0 "Disini adalah tempat dimana dilakukan proses belajar mengajar secarae teori maupun praktek"
    S0 "disini terdapat fasilitas berupa komputer untuk praktek pemograman dan lain-lain"
    S0 "Baiklah,selanjutnya..."
    scene BG3
    with dissolve
    jump tempat

return