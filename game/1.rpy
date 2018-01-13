label ya:
    show A1 at left
    with dissolve
    S0 "Baiklah.."
    S0 "Terima kasih telah ingin meluangkan waktu untuk aplikasi sangat sederhana ini..."
    hide A1 at left
    scene BG2
    with dissolve
    S0 "Dikutip dari sumber yang dapat dipertanggung jawabkan.."
    S0 "Sekolah Tinggi Manajemen Informatika dan Komputer (STMIK) Palangkaraya yang dulunya bernama AMIK Palangkaraya.."
    S2 "Ialah merupakan Perguruan Tinggi Informatika dan Komputer yang pertama di"
    S0 "Kalimantan Tengah khususnya di Kota Cantik Palangka Raya."
    S2 "Berdiri sesuai dengan ijin yang dikeluarkan oleh Dirjen Dikti Depdikbud Nomor 078/D/O/1995.."
    S2 "tanggal 28 September 1995 dan ijin perubahan status menjadi STMIK Palangkaraya dari.."
    S0 "Menteri Pendidikan Nasional Republik Indonesia Nomor 71/D/O/2007 tanggal 24 Mei 2007."
    S0 "Sehingga.."
    S0 "Tanggal Ijin Perubahan Status dari AMIK Palangkaraya menjadi STMIK Palangkaraya itulah.."
    S0 "dijadikan sebagai tanggal untuk memperingati Dies Natalis STMIK Palangkaraya." 
    S0 "STMIK Palangkaraya dikutip situs resmi memiliki visi dan misi sebagai berikut.."
    scene kutipan
    with dissolve
    S1 "Kamu bisa lihat langsung gambar belakang ku ini.."
    S0 "Selanjutnya.."
    scene leader
    with dissolve
    S2 "Pemimpin STMIK dari generasi ke generasi ialah sebagai berikut.."
    S2 "Pada awalnya sebelum menjadi STMIK Palangkaraya,ialah AMIK..."
    hide leader
    scene leader1
    S2 "Pada saat itu AMIK dipimpin oleh Drs.H.Muchtar,M.Si."
    hide leader1
    scene leader2
    S1 "Pada saat itu pemimpin disebut sebagai Direktur selanjutnya digantikan oleh Ir.Siti Maryamah,MM."
    hide leader2
    scene leader3
    S2 "lalu diganti oleh Drs.Sartana,M.Si."
    S0 "Pada saat telah berganti menjadi STMIK Palangkaraya istilah Direktur diganti menjadi ketua.."
    hide leader3
    scene leader4
    S2 "dan pada tahun 2017 tepatnya 14 April 2017 Drs.Sartana,M.Si digantikan dengan Suparno,M.Kom.."
    scene MAP
    with dissolve
    S2 "STMIK Palangkaraya beralamatkan dijalan G.Obos"
    S2 "Untuk lebih lanjutnya bisa dilihat pada gambar dibelakangku ini..."
    S0 "STMIK Palangkaraya.."
    hide MAP
    scene BG1
    show A3 at right
    with dissolve
    S2 "memiliki sendiri 3 jurusan akademik seperti.."
    S2 "Teknik Informasi atau TI.."
    S2 "Sistem Informasi atau SI.."
    S2 "dan terakhir Manajemen Informatika atau MI.."
    hide A3 at right
    show A1 at right
    with dissolve
    S0 "STMIK Palangkaraya sendiri dikenal dengan kampus biru,dikarenakan dominan dengan warna mulai dari bangunan hingga almeter seperti yang kugunakan sekarang..."
    hide A1 at right
    show A3 at right
    with dissolve
    S2 "dan itu juga mengapa aplikasi ini dominan berwarna biru.."
    show STMIK
    hide A3 at right
    with dissolve
    S0 "STMIK Palangkaraya memiliki semboyan.."
    S0 "'Kuliah beneran,benar-benar kuliah'"
    S0 "STMIK palangkaraya juga memiliki beberapa tempat seperti ruang belajar,lab,dan lain sebagainya.."
    S0 "sekian informasi singkat tentang STMIK Palangkaraya,untuk lanjut kamu bisa langsung mendatangi STMIK Palangakaraya sendiri"
    hide STMIK
    show BG1
    show A2 at left
    with dissolve    
    S3 "Baiklah sekarang aku ingin bertanya lagi padamu..."
    S3 "Apakah kamu ingin mengetahui lebih lanjut tentang STMIK Palangkaraya?"
    hide A2
    with dissolve
    menu:
        
        "Ya":
            
            jump ya1


        "Tidak":
            
            jump tidak
    return
    
label mungkin:
    show A2 at left
    with dissolve
    S3 "Mungkin?"
    S3 "Baiklah ku tanya sekali lagi.."
    S3 "Apa kamu benar-benar ingin mengetahui tentang STMIK Palangkaraya?"
    hide A2
    with dissolve
    menu:
        
        "Ya":
            
            jump ya


        "Tidak":
            
            jump tidak

    

label tidak:
    scene BG
    with dissolve
    S3   "Tidak?"
    S2   "Baiklah"
    S4   "mohon maaf bila ada yang tidak berkenan,dan terima kasih telah ingin menggunakan aplikasi sederhana ini.."
    S0   "Sampai Jumpa...!"
    with dissolve
    scene loading1 with fade
    $ renpy.pause(0.2, hard=True)
    return
