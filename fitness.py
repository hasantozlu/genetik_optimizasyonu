import numpy as np

# Amaç fonksiyonu
# y = 4*x1 + 3*x2 - 0.5*x1*x2

def amac_fonksiyonu(birey):
    x1 = birey[0]
    x2 = birey[1]
    return 4 * x1 + 3 * x2 - 0.5 * x1 * x2


def kisit_kontrol(birey):
    ceza_puani = 0.0
    x1 = birey[0]
    x2 = birey[1]

    # Kısıt 1: x1 + x2 <= 8
    if (x1 + x2) > 8:
        ceza_puani += ((x1 + x2) - 8) * 10

    # Kısıt 2: x2 >= 1.5
    if x2 < 1.5:
        ceza_puani += (1.5 - x2) * 10

    # Hard bounds: x1 in [2,6], x2 in [1,4]
    if not (2 <= x1 <= 6) or not (1 <= x2 <= 4):
        ceza_puani += 100

    return ceza_puani


def uygunluk_hesapla(birey):
    skor = amac_fonksiyonu(birey)
    ceza = kisit_kontrol(birey)
    return skor - ceza
