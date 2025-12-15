import numpy as np
import argparse
from evrim_motoru import evrimsel_algoritma


def create_initial_population(size, x1_bounds=(2,6), x2_bounds=(1,4)):
    pop = []
    for _ in range(size):
        x1 = np.random.uniform(*x1_bounds)
        x2 = np.random.uniform(*x2_bounds)
        pop.append([x1, x2])
    return np.array(pop)


def main():
    parser = argparse.ArgumentParser(description='Run genetic algorithm for warehouse racks')
    parser.add_argument('--nesil_sayisi', type=int, default=50)
    parser.add_argument('--populasyon_buyuklugu', type=int, default=6)
    parser.add_argument('--caprazlama_turu', choices=['tek','iki'], default='tek')
    parser.add_argument('--secim_turu', choices=['rulet','rank'], default='rank')
    parser.add_argument('--mutasyon_ihtimali', type=float, default=0.1)
    parser.add_argument('--mutasyon_buyuklugu', type=float, default=0.5)

    args = parser.parse_args()

    populasyon = create_initial_population(args.populasyon_buyuklugu)

    evrimsel_algoritma(
        populasyon=populasyon,
        nesil_sayisi=args.nesil_sayisi,
        caprazlama_turu=args.caprazlama_turu,
        secim_turu=args.secim_turu,
        mutasyon_ihtimali=args.mutasyon_ihtimali,
        mutasyon_buyuklugu=args.mutasyon_buyuklugu
    )

if __name__ == '__main__':
    main()
