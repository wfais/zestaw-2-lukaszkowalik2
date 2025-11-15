import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, sympify, lambdify

def parse_input(wejscie):
    parts = wejscie.split(",")
    func_str = parts[0].strip()
    range_parts = parts[1].strip().split()
    x_min = float(range_parts[0])
    x_max = float(range_parts[1])
    return func_str, x_min, x_max

# Funkcja rysująca wykres na podstawie eval()
def rysuj_wielomian(wejscie):
    # Generowanie wartości x i y przy użyciu eval()
    # Rysowanie wykresu ale bez show()

    func_str, x_min, x_max = parse_input(wejscie)
    
    x = np.linspace(x_min, x_max, 200)
    y = eval(func_str) * np.ones(x.shape)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Funkcja: {func_str}")
    plt.grid(True)

    return y[0], y[-1]

# Funkcja rysująca wykres na podstawie SymPy i lambdify()
def rysuj_wielomian_sympy(wejscie):
    # Definicja symbolu i konwersja do funkcji numerycznej za pomocą SymPy
    # Generowanie wartości x i y przy użyciu funkcji numerycznej
    # Rysowanie wykresu ale bez show()

    func_str, x_min, x_max = parse_input(wejscie)
    x = symbols('x')
    
    expr = sympify(func_str)
    
    f_numeric = lambdify(x, expr, 'numpy')
    
    x_val = np.linspace(x_min, x_max, 200)
    
    y_val_sympy = f_numeric(x_val)
    
    plt.figure()
    plt.plot(x_val, y_val_sympy)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(f"Funkcja (SymPy): {func_str}")
    plt.grid(True)

    return y_val_sympy[0], y_val_sympy[-1]

if __name__ == '__main__':
    # Przykładowe wywołanie pierwszej funkcji
    wejscie1 = "5, -5 5"
    
    # Pierwszy wykres z eval
    wynik_eval = rysuj_wielomian(wejscie1)
    print("Wynik (eval):", wynik_eval)

    
    # Wyświetlanie obu wykresów
    plt.show()
