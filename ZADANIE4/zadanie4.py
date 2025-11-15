import os
import time
import threading
import sys

# Stałe konfiguracyjne
LICZBA_KROKOW = 80_000_000
LICZBA_WATKOW = sorted({1, 2, 4, os.cpu_count() or 4})


def policz_fragment_pi(pocz: int, kon: int, krok: float, wyniki: list[float], indeks: int) -> None:
    # Funkcja oblicza częściową sumę przybliżenia liczby pi metodą prostokątów.
    # Argumenty:
    #     pocz, kon - zakres iteracji (indeksy kroków całkowania),
    #     krok      - szerokość pojedynczego prostokąta (1.0 / LICZBA_KROKOW),
    #     wyniki    - lista, do której należy wpisać wynik dla danego wątku na pozycji indeks,
    #     indeks    - numer pozycji w liście 'wyniki' do zapisania rezultatu.

    # Każdy wątek powinien:
    #   - obliczyć lokalną sumę dla przydzielonego przedziału,
    #   - wpisać wynik do wyniki[indeks].

    suma = 0.0
    for i in range(pocz, kon):
        x_i = (i + 0.5) * krok
        suma += 4.0 / (1.0 + x_i * x_i)
    wyniki[indeks] = suma


def main():
    print(f"Python: {sys.version.split()[0]}  (tryb bez GIL? {getattr(sys, '_is_gil_enabled', lambda: None)() is False})")
    print(f"Liczba rdzeni logicznych CPU: {os.cpu_count()}")
    print(f"LICZBA_KROKOW: {LICZBA_KROKOW:,}\n")

    # Wstępne uruchomienie w celu stabilizacji środowiska wykonawczego
    krok = 1.0 / LICZBA_KROKOW
    wyniki = [0.0]
    w = threading.Thread(target=policz_fragment_pi, args=(0, LICZBA_KROKOW, krok, wyniki, 0))
    w.start()
    w.join()

    # ---------------------------------------------------------------
    # Tu zaimplementować:
    #   - utworzenie wielu wątków (zgodnie z LICZBY_WATKOW),
    #   - podział pracy na zakresy [pocz, kon) dla każdego wątku,
    #   - uruchomienie i dołączenie wątków (start/join),
    #   - obliczenie przybliżenia π jako sumy wyników z poszczególnych wątków,
    #   - pomiar czasu i wypisanie przyspieszenia.
    # ---------------------------------------------------------------

    czasy = {}

    for num_watkow in LICZBA_WATKOW:
        wyniki = [0.0] * num_watkow

        podstawa = LICZBA_KROKOW // num_watkow
        reszta = LICZBA_KROKOW % num_watkow

        zakresy = []
        poczatek = 0
        for k in range(num_watkow):
            koniec = poczatek + podstawa + (1 if k < reszta else 0)
            zakresy.append((poczatek, koniec))
            poczatek = koniec

        czas_start = time.perf_counter()

        watki = []
        for k, (pocz, kon) in enumerate(zakresy):
            w = threading.Thread(target=policz_fragment_pi, args=(pocz, kon, krok, wyniki, k))
            watki.append(w)

        for w in watki:
            w.start()

        for w in watki:
            w.join()

        czas_koniec = time.perf_counter()
        czas_wykonania = czas_koniec - czas_start
        czasy[num_watkow] = czas_wykonania

        suma_wynikow = sum(wyniki)
        pi_przybl = krok * suma_wynikow

        przyspieszenie = czasy[1] / czas_wykonania if num_watkow > 1 else 1.0

        print(f"Wątków: {num_watkow:2d} | Czas: {czas_wykonania:.4f}s | π ≈ {pi_przybl:.9f} | Przyspieszenie: {przyspieszenie:.2f}x")


if __name__ == "__main__":
    main()
