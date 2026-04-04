"""
Verificación de universalidad del arco (N, 2N) en la medida de Haar de E_N.

Calcula para cada N congruente (Tabla 5 del preprint):

    Ratio(N) = ∫_N^{2N} dT/y  /  ∫_N^∞ dT/y

donde y = sqrt(T(T-N)(T+N))  sobre la curva  E_N: W² = T³ - N²T.

Si Ratio(N) es constante en N, la universalidad queda verificada:
el arco del operador k=3 captura siempre la misma fracción del
período real de E_N, independientemente de N.

NOTA TEÓRICA:
    El cambio T = NR elimina N analíticamente:
    ∫_N^{2N} dT/y = N^{-1/2} ∫_1^2 dR/√(R(R-1)(R+1))
    ∫_N^∞   dT/y = N^{-1/2} ∫_1^∞ dR/√(R(R-1)(R+1))
    => Ratio = constante universal, independiente de N.
    El código VERIFICA esto numéricamente.
"""

import numpy as np
from scipy.integrate import quad

# ----------------------------------------------------------------
# Números congruentes de la Tabla 5 del preprint
# (excluye N=20 que no es libre de cuadrados)
# ----------------------------------------------------------------
N_list = [5, 6, 7, 13, 14, 15, 22, 23, 29, 31, 37, 38, 47, 53, 61]

# ----------------------------------------------------------------
# Funciones del integrando con manejo explícito de singularidad
# ----------------------------------------------------------------

def integrando_sustituido(t, Nv):
    """
    Sustitución T = Nv + t^2 para eliminar la singularidad integrable en T = Nv.
    Derivación:
        dT = 2t dt
        sqrt(T(T-Nv)(T+Nv)) = sqrt((Nv+t^2) * t^2 * (2Nv+t^2))
                              = t * sqrt((Nv+t^2)(2Nv+t^2))
        => dT/y = 2t dt / (t * sqrt((Nv+t^2)(2Nv+t^2)))
                = 2 dt / sqrt((Nv+t^2)(2Nv+t^2))
    Límites para T in (Nv, 2Nv): t in (0, sqrt(Nv))
    """
    return 2.0 / np.sqrt((Nv + t * t) * (2.0 * Nv + t * t))


def integrando_original(T, Nv):
    """
    Integrando dT/sqrt(T(T-N)(T+N)) sin singularidad (T > 2N).
    """
    return 1.0 / np.sqrt(T * (T - Nv) * (T + Nv))


# ----------------------------------------------------------------
# Cálculo principal
# ----------------------------------------------------------------

print("=" * 72)
print("  UNIVERSALIDAD DEL ARCO (N, 2N) EN LA MEDIDA DE HAAR DE E_N")
print("  Ratio = ∫_N^{2N} dT/y  /  ∫_N^∞ dT/y,   y = sqrt(T(T-N)(T+N))")
print("=" * 72)
print(f"  {'N':>4}  {'∫(N,2N)':>13}  {'∫(N,∞)':>13}  {'Ratio':>14}  {'Error quad':>10}")
print("  " + "-" * 60)

ratios = []

for N in N_list:
    Nf = float(N)          # conversión explícita a float Python puro

    # --- Numerador: T in (N, 2N) con sustitución ---
    I_num, err_num = quad(
        integrando_sustituido,
        0.0, np.sqrt(Nf),
        args=(Nf,),
        limit=200
    )

    # --- Denominador parte 1: T in (N, 2N) = mismo que numerador ---
    I_d1 = I_num

    # --- Denominador parte 2: T in (2N, ∞), sin singularidad ---
    # scipy.quad acepta np.inf directamente como límite superior
    I_d2, err_d2 = quad(
        integrando_original,
        2.0 * Nf, np.inf,
        args=(Nf,),
        limit=200
    )

    I_den = I_d1 + I_d2
    ratio = I_num / I_den
    error_total = float(err_num + err_d2)

    ratios.append(ratio)
    print(f"  {N:>4d}  {I_num:>13.8f}  {I_den:>13.8f}  {ratio:>14.10f}  {error_total:>10.2e}")

print("  " + "-" * 60)
media   = float(np.mean(ratios))
sigma   = float(np.std(ratios))
print(f"  {'Media':>4}  {'':>13}  {'':>13}  {media:>14.10f}")
print(f"  {'σ':>4}  {'':>13}  {'':>13}  {sigma:>14.10f}")
print()

# ----------------------------------------------------------------
# Valor teórico: ratio en coordenada R = T/N (independiente de N)
# ----------------------------------------------------------------
print("  VALOR TEÓRICO (coordenada universal R = T/N):")
print("  Ratio = ∫_1^2 dR/√(R(R-1)(R+1))  /  ∫_1^∞ dR/√(R(R-1)(R+1))")
print()

def f_R_sub(t):
    """
    R = 1 + t^2, misma sustitución aplicada en R=1.
    dR/sqrt(R(R-1)(R+1)) = 2 dt / sqrt((1+t^2)(2+t^2))
    Límites R in (1,2) => t in (0,1)
    """
    return 2.0 / np.sqrt((1.0 + t * t) * (2.0 + t * t))

def f_R_cola(R):
    return 1.0 / np.sqrt(R * (R - 1.0) * (R + 1.0))

I_R_num, _ = quad(f_R_sub,   0.0, 1.0,     limit=200)   # R in (1, 2)
I_R_d2,  _ = quad(f_R_cola,  2.0, np.inf,  limit=200)   # R in (2, ∞)
I_R_den    = I_R_num + I_R_d2

ratio_teo = I_R_num / I_R_den

print(f"  ∫_1^2  dR/√(R(R-1)(R+1)) = {I_R_num:.10f}  ← Z del preprint")
print(f"  ∫_2^∞  dR/√(R(R-1)(R+1)) = {I_R_d2:.10f}")
print(f"  ∫_1^∞  dR/√(R(R-1)(R+1)) = {I_R_den:.10f}  ← período normalizado")
print()
print(f"  Ratio teórico universal    = {ratio_teo:.10f}")
print()
print(f"  Diferencia media-teórico   = {abs(media - ratio_teo):.2e}")
print()

# ----------------------------------------------------------------
# Interpretación
# ----------------------------------------------------------------
print("  INTERPRETACIÓN:")
print(f"  El arco (N,2N) captura el {ratio_teo*100:.6f}% del período real de E_N.")
print(f"  Esta fracción es UNIVERSAL: idéntica para todo N congruente.")
print()
print("  Prueba analítica (cambio T = NR):")
print("  ∫_N^{2N} dT/y = N^{-1/2} · ∫_1^2 dR/√(R(R-1)(R+1))")
print("  ∫_N^∞   dT/y = N^{-1/2} · ∫_1^∞ dR/√(R(R-1)(R+1))")
print("  => N^{-1/2} se cancela => Ratio independiente de N.  □")
print()
print("  El operador k=3 selecciona el único subarco compacto de")
print("  la componente no acotada de E_N(R) con medida de Haar")
print("  que representa exactamente esta fracción universal del período.")
print("=" * 72)
