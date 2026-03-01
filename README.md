
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
| `validation_k3_complete.sage.py` | Master validation script. Covers all empirical results in the preprint: Table 3 (density ratios for N=210), Tables 7–8 (24 anchor pairs), Tables 9–11 (integer points on curves E_m and rank estimates), Table 5 (complete Mordell-Weil orbit data for 17 congruent numbers with Regime I/II/III classification), Table 6 (digit-count formula validation), and Siegel hierarchy verification. |
| `kstar_eficiente.sage.py` | Efficient Mordell-Weil orbit search for the 17 target congruent numbers. Computes k*, x(k*P), m/n ratio, digit count of height parameter n, and square-free verification. Includes RAM monitoring and partial logging. Suitable for N with dig(n) up to ~200. |
| `kstar_frontera.sage.py` | Specialized script for computationally intensive cases (N=29, 31, 38, 47, 53, 61). Allocates up to 4GB PARI stack. Uses adaptive square-free verification: direct factorization for dig(n) ≤ 60, partial factor decomposition for intermediate sizes, and birational certificate for dig(n) > 300. |
| `validacion_37.sage.py` | Dedicated validation script for N=37. Jumps directly to k=14 and k=16, confirms k*=16, recovers exact coordinates of k*P, computes dig(n)=1508, and validates the digit-count formula with error 0.01%. Completes in under 30 seconds. |
| `rank_Em_simon.sage` | Simon-only exact rank computation for the 19 original paper values of m. Uses PARI's `ellfromeqn` to convert E_m to Weierstrass form and Simon's 2-descent (`lim1=3, lim3=6`) for unconditional rank determination. Resolves all 19 cases in fast mode (< 3s per curve). Corrects all heuristic estimates in Section 14. |
| `rank_Em_extended.sage` | Extended search covering m ≤ 1,000 and n ≤ 10,000. Two-phase pipeline: (1) pure-Python anchor pair scan over 10M parameter pairs; (2) Simon rank computation for all active m values. Discovers 141 anchor pairs across 114 values of m, with exact ranks for 65 curves including a rank-7 curve at m=169. Runtime approximately 15–18 minutes. |

---

### Result Logs

| File | Contents |
|------|---------|
| `validation_k3_results.txt` | Full output of `validation_k3_complete.sage.py`. Contains all six validation blocks: Bloque 1 (Table 3, N=210 ratios), Bloque 2 (24 anchor pairs with Δ=(4j−m)² verification), Bloque 3 (integer points on 19 curves E_m), Bloque 4 (Mordell-Weil orbit for N ∈ {5,…,23}), Bloque 5 (Siegel hierarchy check), Bloque 6 (digit formula). |
| `kstar_resultados.txt` | Output of `kstar_eficiente.sage.py` for all 17 targets. Contains k*, x(k*P), m/n, dig(n), sf verification, and timing for each N. |
| `kstar_frontera_resultados.txt` | Output of `kstar_frontera.sage.py` for N ∈ {29, 31, 38, 47, 53, 61}. Includes sf verification method (direct, partial factors, or birational) and RAM usage per case. |
| `validacion_37_resultados.txt` | Full output of `validacion_37.sage.py`. Confirms k*=16, dig(n)=1508, pred_dig=1508.2, error=0.01%, u/v=1.8414 ∈ (1,2), gcd(n,m)=1. |
| `rank_Em_simon_results.txt` | Full output of `rank_Em_simon.sage`. Exact ranks, Weierstrass models, conductors, generators and Néron-Tate heights for all 19 paper values of m. Validates and corrects the heuristic estimates of Section 14. |
| `rank_Em_extended_results.txt` | Full output of `rank_Em_extended.sage`. Complete anchor pair table (141 pairs, 114 active m values), rank distribution, high-rank curves, and open cases for m ≥ 400. Includes rank-7 discovery at m=169 and five rank-6 curves. |

---

## Key Results Reproduced

### Table 3 — Density ratios for N=210
Ratios R = x/N for the first 20 multiples of the Mordell-Weil
generator of E_210. Computed via Lemma 23: R = x/N directly.
4 out of 20 multiples fall strictly in (1,2); one boundary case
at n=16 with R=1.0000. Coverage: 20%.

### Tables 7–8 — Anchor pairs (original dataset)
24 anchor pairs with n ≤ 100 verified exactly. All satisfy:
- C³(n,m) = 4j² − 2jm (autoreferential condition)
- Δ = (4j−m)² (integrality of j)
- u/v = (2n−m)/n ∈ (1,2) (operator domain)
- gcd(n,m) = 1

19 distinct values of m produce anchor pairs.

### Section 14 — Exact Mordell-Weil ranks (corrected)
Exact ranks via Simon's 2-descent for all 19 paper values of m.
Every heuristic estimate in Section 14 was an underestimate.
Selected corrections:

| m  | Heuristic | Exact rank | Correction |
|----|-----------|------------|------------|
| 4  | 2         | 3          | +1         |
| 8  | 2         | 3          | +1         |
| 19 | 2         | **5**      | +3         |
| 32 | 2         | 4          | +2         |
| 58 | ≥3        | **6**      | confirmed+ |
| 90 | ≥3        | **5**      | confirmed+ |

All ranks unconditional (Simon fast mode, < 3s per curve).

### Extended search — m ≤ 1,000, n ≤ 10,000
Anchor pair scan and exact rank computation beyond the paper's original dataset.

**Anchor pairs:** 141 total across 114 active values of m
(vs. 24 pairs / 19 values in the paper; factor of ~6× in both dimensions).

**Rank distribution** (65 curves with exact rank):

| Rank | Curves | % of resolved |
|------|--------|---------------|
| 3    | 6      | 9.2%          |
| 4    | 35     | 53.8%         |
| 5    | 18     | 27.7%         |
| 6    | 5      | 7.7%          |
| **7**| **1**  | **1.5%**      |

Mean rank: **4.385** (vs. 0.5 predicted by Goldfeld's conjecture for generic families).

**High-rank curves (rank ≥ 6):**

| m   | Exact rank | Anchor pairs | Status   |
|-----|------------|--------------|----------|
| 58  | 6          | 2            | In paper |
| 146 | 6          | 1            | New      |
| 171 | 6          | 1            | New      |
| 283 | 6          | 1            | New      |
| 318 | 6          | 1            | New      |
| **169** | **7** | **2**        | **New — highest rank found** |

The rank-7 curve E₁₆₉ is the first rank-7 curve identified in this framework.
The monotone growth of maximum rank (3 → 5 → 6 → 7 as m increases) supports
the conjecture that the Mordell-Weil ranks of {E_m} are unbounded.

**Surface structure:**
The family {E_m} is the fiber family of the irreducible elliptic surface
S: Y² = Z² + 4N(N−Z)(2N−Z)(3N−Z) ⊂ A³_Q. Each E_m is a distinct fiber
with its own Mordell-Weil group. The family is not a twist family: no two
curves E_m, E_m' are quadratic twists of each other, verified by distinct
prime factors in each conductor. All Weierstrass models satisfy a²(E_m) = 24m².

### Table 5 — Mordell-Weil orbit data
k* and dig(n) reproduced exactly for all 17 congruent numbers.
Regime classification (I/II/III) based on sign of x(P):
- Regime I:   x(P) < 0  (search over even k only)
- Regime II:  x(P) ∈ (N, 2N)  (k*=1)
- Regime III: x(P) > 0, outside (N, 2N)  (search all k)

### Table 6 — Digit-count formula (rigorously bounded)
Formula: dig(n) ≈ ĥ(P) · (k*)² / log(10)

Rigorous bound (proved in Section 15):

    | dig(n) − ĥ(P)·(k*)²/log(10) | ≤ log(2N)/log(10)

| N  | k*  | dig(n) observed | error  | bound log(2N)/log10 |
|----|-----|-----------------|--------|----------------------|
| 6  | 2   | 2               | 22.81% | 1.079                |
| 22 | 8   | 118             | 0.18%  | 1.643                |
| 29 | 72  | 19911           | 0.03%  | 1.763                |
| 37 | 16  | 1508            | 0.01%  | 1.869                |
| 61 | 4   | 116             | 0.58%  | 2.086                |

All 15 cases in the paper satisfy the bound. Errors below 1% for k* ≥ 8.

---

## Usage Notes

**Running any script:**
```bash
sage validation_k3_complete.sage.py
sage kstar_eficiente.sage.py
sage kstar_frontera.sage.py
sage validacion_37.sage.py
sage rank_Em_simon.sage
sage rank_Em_extended.sage
```

**Runtime estimates:**

| Script | Estimated runtime |
|--------|-------------------|
| `validation_k3_complete.sage.py` | ~10 min |
| `kstar_eficiente.sage.py` | ~15 min |
| `kstar_frontera.sage.py` | ~2 hours (N=29 dominates) |
| `validacion_37.sage.py` | < 30 sec |
| `rank_Em_simon.sage` | ~1 min |
| `rank_Em_extended.sage` | ~15–18 min |

**Memory requirements:**
- Standard scripts: < 512 MB RAM
- `kstar_frontera.sage.py`: up to 4 GB (PARI stack for N=29, N=37)
- `rank_Em_extended.sage`: < 1 GB RAM

**SageMath version:** All scripts tested on SageMath 9.x, Ubuntu 24.
The `simon_two_descent` API uses `lim1`, `lim3`, `limtriv`, `maxprob`,
`limbigprime` parameters (not `bound`). This is the correct API for
SageMath ≥ 9.0; see [issue #35621](https://github.com/sagemath/sage/issues/35621)
for the deprecation notice affecting `simon_two_descent` in older versions.

---

## Reproducibility Statement

All rank computations are **unconditional** (Simon's 2-descent over Q,
via PARI's `ellfromeqn` + `simon_two_descent`). No results depend on the
Birch and Swinnerton-Dyer conjecture, unverified heuristics, or
probabilistic primality tests. Square-free verification of C³(n,m) for
large n uses the birational certificate of Theorem 25: existence of
x(k*P) ∈ (N, 2N) with P ∈ E_N(Q) certifies sf(C³(n,m)) = N directly.
