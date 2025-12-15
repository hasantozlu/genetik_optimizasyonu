
# 🧬 Genetik Algoritma ile Akıllı Depo Raf Optimizasyonu

Bu proje, genetik algoritma kullanarak depo raf yüksekliği (x1) ve derinliği (x2) parametrelerini optimize etmeye yönelik bir örnek uygulamadır. Amaç, verilen amaç fonksiyonunu maksimize ederek depo verimliliğini artırmaktır.

## Genetik Algoritma — Kısa Açıklama

Genetik algoritma (GA) popülasyon tabanlı, evrimsel bir optimizasyon yöntemidir. Bu proje için temel adımlar:

- **Popülasyon**: Her birey iki gen içerir (x1 = yükseklik, x2 = derinlik). Başlangıçta rastgele bireyler oluşturulur.
- **Uygunluk (Fitness)**: Her bireyin başarımı amaç fonksiyonuna göre hesaplanır; kısıt ihlalleri cezalandırılır (penalti).
- **Seçim**: Daha iyi uygunluk değerine sahip bireyler ebeveyn seçilme olasılığı daha yüksek olur (rulet veya rank seçimi kullanılabilir).
- **Çaprazlama (Crossover)**: Ebeveynlerden yeni çocuklar üretilir (tek nokta veya aritmetik/iki-nokta yaklaşımları).
- **Mutasyon**: Çocukların genlerine rastgele küçük değişiklikler uygulanır; bu, arama alanını keşfetmeyi sağlar.
- **Elitizm**: Her nesilde en iyi birey korunup yeni nesile aktarılır; böylece iyi çözümler kaybolmaz.
- **Döngü**: Bu adımlar belirlenen nesil sayısı kadar tekrar edilir; en iyi çözüm nesiller boyunca takip edilir.

Parametreler (popülasyon büyüklüğü, nesil sayısı, mutasyon oranı vb.) algoritmanın keşif/sömürü dengesini ve sonuç kalitesini etkiler.

## Problem Özeti

Amaç fonksiyonu:

```
y = 4*x1 + 3*x2 - 0.5*x1*x2
```

- x1: Raf yüksekliği (m), aralık: [2, 6]
- x2: Raf derinliği (m), aralık: [1, 4]

Kısıtlar:

- x1 + x2 <= 8
- x2 >= 1.5
- Hard-bounds: x1 ∈ [2,6], x2 ∈ [1,4]

Kısıt ihlallerine penalti uygulanır (koda göre ceza puanları mevcuttur).

## Depo Yapısı (Dosyalar)

- `fitness.py`           : Amaç fonksiyonu, kısıt kontrolü ve uygunluk hesaplama.
- `operators.py`         : Seçim (rulet, rank), çaprazlama ve mutasyon fonksiyonları.
- `evrim_motoru.py`      : Ana evrimsel algoritma (iterasyonlar, elitizm, grafik).
- `main.py`              : Komut satırından çalıştırılabilir giriş noktası (önceden `run.py`).
- `requirements.txt`     : Gerekli Python paketleri (`numpy`, `matplotlib`).

## Kurulum (lokal / GitHub üzerinden klonlandıktan sonra)

1) (Önerilen) Bir sanal ortam oluşturun ve aktif edin (PowerShell örneği):

```powershell
python -m venv .venv;
.\.venv\Scripts\Activate.ps1
```

2) Gerekli paketleri yükleyin:

```powershell
pip install -r requirements.txt
```

## Çalıştırma

Komut satırından parametrelerle çalıştırabilirsiniz. Örnek:

```powershell
python main.py --nesil_sayisi 50 --populasyon_buyuklugu 12 --caprazlama_turu tek --secim_turu rank --mutasyon_ihtimali 0.1 --mutasyon_buyuklugu 0.5
```

Varsayılan argümanlar:

- `--nesil_sayisi`: 50
- `--populasyon_buyuklugu`: 6
- `--caprazlama_turu`: `tek` veya `iki` (default `tek`)
- `--secim_turu`: `rulet` veya `rank` (default `rank`)
- `--mutasyon_ihtimali`: float (default 0.1)
- `--mutasyon_buyuklugu`: float (default 0.5)

Çalıştırma sonucunda konsolda her nesilde en iyi birey yazdırılır ve sonrasında uygunluk değerlerinin nesillere göre grafiği gösterilir.


