label start:
    play music "1.ogg"
    scene BG1
    with dissolve
    centered "Hello World..."
    scene BG1
    centered "kamu bisa keluar dari aplikasi ini jika tidak ingin memulai dengan menekan pilihan menu dipojok kiri atas atau sentuh layar untuk memulai..."
    centered "Hai..."
    centered "Selamat datang..."
    show A0
    with dissolve
    hide A0
    show A1
    with dissolve
    S0 "Perkenalkan namaku Alice, aku adalah makhluk virtual yang dibuat untuk menemani kalian..."
    S0 "Aku disini bertugas untuk menjadi pemandu kalian..."
    S0 "Aplikasi ini dibuat dengan maksud untuk memperkenal STMIK Palangkaraya."
    S0 "Baiklah.."
    hide A1
    scene BG2
    with dissolve
    S0 "Selamat datang di STMIK Palangkaraya!"
    S0 "Ini adalah tampak depan kampus STMIK Palangkaraya.."
    S2 "Sebelum aku memberitahumu tentang STMIK Palangkaraya ini, aku ingin bertanya.."
    S3 "Apa kamu benar-benar ingin mengetahui tentang STMIK Palangkaraya?"
    scene BG1
    with dissolve
    menu:
        
        "Ya":
            
            jump ya
            

        "Mungkin":
            
            jump mungkin
            

        "Tidak":
            
            jump tidak

return