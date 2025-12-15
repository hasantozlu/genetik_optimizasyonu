import numpy as np
import matplotlib.pyplot as plt
from fitness import uygunluk_hesapla
from operators import rulet_secimi, rank_temelli_secim, tek_noktali_caprazlama, iki_noktali_caprazlama, mutasyon_uygula


def evrimsel_algoritma(populasyon, nesil_sayisi, caprazlama_turu,
                       secim_turu, mutasyon_ihtimali, mutasyon_buyuklugu):

    en_iyiler = []
    best_solution = None
    best_fitness = -1e9

    for nesil in range(nesil_sayisi):
        uygunluklar = np.array([uygunluk_hesapla(b) for b in populasyon])

        mevcut_en_iyi_index = np.argmax(uygunluklar)
        elit_birey = populasyon[mevcut_en_iyi_index].copy()
        elit_uygunluk = uygunluklar[mevcut_en_iyi_index]
        en_iyiler.append(elit_uygunluk)

        if elit_uygunluk > best_fitness:
            best_fitness = elit_uygunluk
            best_solution = elit_birey

        print(f"Nesil {nesil}: En İyi Skor = {elit_uygunluk:.4f} | Genler: {np.round(elit_birey,2)}")

        # Eşleme havuzu
        havuz = []
        for _ in range(len(populasyon) // 2):
            if secim_turu == "rulet":
                ebeveynler = rulet_secimi(populasyon, uygunluklar)
            elif secim_turu == "rank":
                ebeveynler = rank_temelli_secim(populasyon, uygunluklar)
            else:
                ebeveynler = rulet_secimi(populasyon, uygunluklar)
            havuz.append(ebeveynler)

        yeni_bireyler = [elit_birey]
        while len(yeni_bireyler) < len(populasyon):
            index = np.random.randint(0, len(havuz))
            p1, p2 = havuz[index]
            if caprazlama_turu == "tek":
                c1, c2 = tek_noktali_caprazlama(p1, p2)
            else:
                c1, c2 = iki_noktali_caprazlama(p1, p2)

            c1 = mutasyon_uygula(c1, mutasyon_ihtimali, mutasyon_buyuklugu)
            c2 = mutasyon_uygula(c2, mutasyon_ihtimali, mutasyon_buyuklugu)

            yeni_bireyler.append(c1)
            if len(yeni_bireyler) < len(populasyon):
                yeni_bireyler.append(c2)

        populasyon = np.array(yeni_bireyler)

    print("\n🏁 ALGORİTMA TAMAMLANDI")
    if best_solution is not None:
        print(f"🏆 En İyi Çözüm: Raf Yüksekliği (x1) = {best_solution[0]:.3f} m")
        print(f"🏆 En İyi Çözüm: Raf Derinliği (x2)  = {best_solution[1]:.3f} m")
    print(f"⭐ Maksimum Verim Puanı: {best_fitness:.4f}")

    plt.figure(figsize=(10,6))
    plt.plot(en_iyiler, linewidth=2, color='green')
    plt.title(f"Genetik Algoritma Optimizasyonu (Senaryo 0)\nEn İyi Skor: {best_fitness:.4f}")
    plt.xlabel("Nesil Sayısı")
    plt.ylabel("Amaç Fonksiyonu Değeri (Fitness)")
    plt.show()
