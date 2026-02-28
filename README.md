# Compactness-via-k-3-Operator
Scripts and core results for "Arithmetic Compactness and Universal Generation" preprint's replication. 
## README.md

```markdown
# Computational Validation: Arithmetic Compactness via the k=3 Operator

Supplementary computational materials for the preprint:

> **Arithmetic Compactness and Universal Generation: The k=3 Operator,
> Finite Siegel Points, and Dense Mordell-Weil Orbits in Congruent
> Number Theory**
> Francisco Javier Lucero Bravo, February 2026.

All scripts are written in [SageMath](https://www.sagemath.org/) and
were executed on SageMath 9.x under Ubuntu 24. No external dependencies
beyond a standard SageMath installation are required, except where noted.

---

## Repository Structure

### Computational Scripts

| File | Purpose |
|------|---------|
| `validation_k3_complete.sage.py` | Master validation script. Covers all empirical results in the preprint: Table 3 (density ratios for N=210), Tables 7--8 (24 anchor pairs), Tables 9--11 (integer points on curves E_m and rank estimates), Table 5 (complete Mordell-Weil orbit data for 17 congruent numbers with Regime I/II/III classification), Table 6 (digit-count formula validation), and Siegel hierarchy verification. |
| `kstar_eficiente.sage.py` | Efficient Mordell-Weil orbit search for the 17 target congruent numbers. Computes k*, x(k*P), m/n ratio, digit count of height parameter n, and square-free verification. Includes RAM monitoring and partial logging. Suitable for N with dig(n) up to ~200. |
| `kstar_frontera.sage.py` | Specialized script for computationally intensive cases (N=29, 31, 38, 47, 53, 61). Allocates up to 4GB PARI stack. Uses adaptive square-free verification: direct factorization for dig(n) <= 60, partial factor decomposition for intermediate sizes, and birational certificate for dig(n) > 300. |
| `validacion_37.sage.py` | Dedicated validation script for N=37. Jumps directly to k=14 and k=16, confirms k*=16, recovers exact coordinates of k*P, computes dig(n)=1508, and validates the digit-count formula with error 0.01%. Completes in under 30 seconds. |

### Result Logs

| File | Contents |
|------|---------|
| `validation_k3_results.txt` | Full output of `validation_k3_complete.sage.py`. Contains all six validation blocks: Bloque 1 (Table 3, N=210 ratios), Bloque 2 (24 anchor pairs with Delta=(4j-m)^2 verification), Bloque 3 (integer points on 19 curves E_m), Bloque 4 (Mordell-Weil orbit for N in {5,...,23}), Bloque 5 (Siegel hierarchy check), Bloque 6 (digit formula). |
| `kstar_resultados.txt` | Output of `kstar_eficiente.sage.py` for all 17 targets. Contains k*, x(k*P), m/n, dig(n), sf verification, and timing for each N. |
| `kstar_frontera_resultados.txt` | Output of `kstar_frontera.sage.py` for N in {29, 31, 38, 47, 53, 61}. Includes sf verification method (direct, partial factors, or birational) and RAM usage per case. |
| `validacion_37_resultados.txt` | Full output of `validacion_37.sage.py`. Confirms k*=16, dig(n)=1508, pred_dig=1508.2, error=0.01%, u/v=1.8414 in (1,2), gcd(n,m)=1. |

---

## Key Results Reproduced

### Table 3 — Density ratios for N=210
Ratios R = x/N for the first 20 multiples of the Mordell-Weil
generator of E_210. Computed via Lemma 23: R = x/N directly.
4 out of 20 multiples fall strictly in (1,2); one boundary case
at n=16 with R=1.0000. Coverage: 20%.

### Tables 7--8 — Anchor pairs
24 anchor pairs with n <= 100 verified exactly. All satisfy:
- C3(n,m) = 4j^2 - 2jm (autoreferential condition)
- Delta = (4j-m)^2 (integrality of j)
- u/v = (2n-m)/n in (1,2) (operator domain)
- gcd(n,m) = 1

19 distinct values of m produce anchor pairs.

### Table 5 — Mordell-Weil orbit data
k* and dig(n) reproduced exactly for all 17 congruent numbers.
Regime classification (I/II/III) based on sign of x(P):
- Regime I:   x(P) < 0  (search over even k only)
- Regime II:  x(P) in (N, 2N)  (k*=1)
- Regime III: x(P) > 0, outside (N, 2N)  (search all k)

### Table 6 — Digit-count formula
Formula: dig(n) ~ h(P) * (k*)^2 / log(10)

| N  | k*  | dig(n) observed | error  |
|----|-----|-----------------|--------|
| 6  | 2   | 2               | 22.81% |
| 22 | 8   | 118             | 0.18%  |
| 29 | 72  | 19911           | 0.03%  |
| 37 | 16  | 1508            | 0.01%  |
| 61 | 4   | 116             | 0.58%  |

Errors below 1% for all k* >= 8. Larger errors at small k*
are consistent with the asymptotic character of the formula.

---

## Usage Notes

**Running any script:**
```bash
sage validation_k3_complete.sage.py
sage kstar_eficiente.sage.py
sage kstar_frontera.sage.py
sage validacion_37.sage.py
```

**PARI stack for large cases:**
Scripts `kstar_frontera.sage.py` and `validacion_37.sage.py`
automatically attempt to allocate 4GB PARI stack (2GB fallback).
For N=29 with dig(n)=19911, this is required to avoid overflow
in the square-free verification step.

**Estimated run times:**
| Script | Time |
|--------|------|
| `validation_k3_complete.sage.py` | ~12 min (N=22 dominates at ~10 min) |
| `kstar_eficiente.sage.py` | ~15 min (N=22 at k*=8 dominates) |
| `kstar_frontera.sage.py` | ~10 s |
| `validacion_37.sage.py` | ~10 s |

---

## Author

Francisco Javier Lucero Bravo
February 2026
```
