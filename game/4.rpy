label tempatE:
    menu:
        
        "Tempat Berurusan diSTMIK Palangkaraya":
            
            jump tempat4
            
        "Ruangan Club":
            
            jump tempat5
        
        "Atap":
            jump tempat6
            
        
        "Maaf,aku ingin mengetahui hal lain tentang STMIK Palangkaraya..":
            jump ya1

#tempat berususan diSTMIK Palangkaraya
label tempat4:
    scene BG1
    with dissolve
    S0 "Tempat Berurusan diSTMIK Palangkaraya dapat berubah sewaktu-waktu guna mempermudah dalam berurusan diSTMIK Palangkaraya sendiri"
    S0 "dengan membuat sistem pengurusan yang lebih effesien dan efektif dalam pengurusan"
    S0 "namun perubahan itu juga adalah hasil kesepakatan dari seluruh anggota STMIK Palangkaraya"
    S0 "Baiklah,selanjutnya..."
    scene BG3
    with dissolve
    jump tempat
    
#Ruangan Club
label tempat5:
    scene BG1
    with dissolve
    S0 "Ruangan club sebenarnya ialah dimana ruangan suatu club tertentu yang dibuat oleh para mahasiswa dan juga dosen"
    S0 "ada beberapa club yang sudah dibuat seperti bahasa,budaya,pemograman.."
    S0 "keagamaan,musik,olahraga,hingga perkumpulan mahasiswa.."
    S0 "Jika kamu adalah anggota dari STMIK Palangkaraya,kamu dapat mengusulkannya dengan club yang kamu inginkan."
    S3 "Maaf,Karena terlalu banyak jadi tidak dapat ditampilkan disini." 
    S0 "Baiklah,selanjutnya..."
    scene BG3
    with dissolve
    jump tempat

#atap
label tempat6:
    S3 "Maaf..."
    S3 "Atap dilarang untuk disinggahi,karena pihak kampus peduli terhadap keselamatan para orang-orang diwilayah STMIK Palangkaraya sendiri"
    S3 "Lagipula diatap panas,kamu mau jadi ikan kering?"
    S3 "Cobalah untuk mengunjungi tempat lainnya saja.."
    scene BG3
    with dissolve
    jump tempat