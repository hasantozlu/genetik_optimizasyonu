import numpy as np
import random


def rulet_secimi(populasyon, uygunluklar, adet=2):
    secilenler = []
    min_val = np.min(uygunluklar)
    pozitif_uygunluklar = uygunluklar.copy()
    if min_val < 0:
        pozitif_uygunluklar = uygunluklar - min_val + 1e-3

    toplam_puan = np.sum(pozitif_uygunluklar)
    for _ in range(adet):
        sans_oku = np.random.uniform(0, toplam_puan)
        kumulatif_toplam = 0.0
        for i in range(len(populasyon)):
            kumulatif_toplam += pozitif_uygunluklar[i]
            if kumulatif_toplam >= sans_oku:
                secilenler.append(populasyon[i])
                break
    return np.array(secilenler)


def rank_temelli_secim(populasyon, uygunluklar, adet=2):
    N = len(populasyon)
    secilenler = []
    sirali_indeksler = np.argsort(uygunluklar)
    toplam_rank_puani = N * (N + 1) / 2
    for _ in range(adet):
        sans_oku = np.random.uniform(0, toplam_rank_puani)
        kumulatif_toplam = 0.0
        for rank, orj_idx in enumerate(sirali_indeksler):
            rank_degeri = rank + 1
            kumulatif_toplam += rank_degeri
            if kumulatif_toplam >= sans_oku:
                secilenler.append(populasyon[orj_idx])
                break
    return np.array(secilenler)


def tek_noktali_caprazlama(p1, p2):
    c1 = np.array([p1[0], p2[1]])
    c2 = np.array([p2[0], p1[1]])
    return c1, c2


def iki_noktali_caprazlama(p1, p2):
    alpha = random.random()
    c1 = alpha * p1 + (1 - alpha) * p2
    c2 = alpha * p2 + (1 - alpha) * p1
    return c1, c2


def mutasyon_uygula(birey, ihtimal, buyukluk):
    yeni = birey.copy()
    if np.random.rand() < ihtimal:
        degisim = buyukluk * np.random.randn()
        yeni[0] += degisim
    if np.random.rand() < ihtimal:
        degisim = buyukluk * np.random.randn()
        yeni[1] += degisim

    # Sınırlar
    if yeni[0] < 2:
        yeni[0] = 2
    elif yeni[0] > 6:
        yeni[0] = 6
    if yeni[1] < 1:
        yeni[1] = 1
    elif yeni[1] > 4:
        yeni[1] = 4
    return yeni
