# Experimental Mathematics

**Exploring patterns in numbers, networks, and nonlinear systems with Python.**

How do prime factors constrain a sum of two squares? What does a random graph look like through its eigenvalues? How can a simple recurrence produce dramatically different behavior as one parameter changes?

This collection investigates those questions through numerical experiments and visualization. Nine projects span number theory, random graph spectra, dynamical systems, and statistical inference, combining mathematical reasoning with direct computation.

## Explore the projects

| Project | Question explored | Methods |
| --- | --- | --- |
| [Collatz sequences](collatz/collatz.py) | How do ordinary iteration and grouping divisions by two compare? | Recursive iteration, descent times, least-squares fits, empirical tails |
| [Digits of pi](pi_digits/digits_of_pi.py) | How do digit frequencies and repeated-digit patterns compare with random digits? | Histograms, relative entropy, random guessing, position classes |
| [Random graph spectra](random_graphs/) | How do adjacency eigenvalues change with graph size and edge density? | ErdÃ…â€˜sÃ¢â‚¬â€œRÃƒÂ©nyi models, matrix centering, numerical eigenvalues |
| [Pythagorean triples](pythagorean_triples/pythagorean_triples.py) | Which legs and hypotenuses occur in a bounded search? | Enumeration, primitive triples, greatest common divisors |
| [Sums of two squares](two_squares/) | How does prime factorization relate to representability and multiplicity? | Modular arithmetic, factorization, lattice-point enumeration |
| [Logistic map](logistic_map/bifurcations.py) | How does an orbit change with its parameter and initial condition? | Discrete dynamics, interactive sliders |
| [Plant dynamics](plant_dynamics/plant_bifurcations.py) | How do equilibria change as a model parameter varies? | Numerical root searches, local stability, bifurcation plots |
| [Chemical dynamics](chemical_dynamics/bifurcations_bead.py) | What does a two-variable vector field reveal about the dynamics? | Direction fields, nullcline visualization |
| [Statistical power](statistical_power/powercurve.py) | How does a two-sided normal test respond to different true means? | Normal probabilities, acceptance regions, power curves |

For a quick visual introduction, start with the **logistic map**. For the connection between computation and mathematical reasoning, read **sums of two squares**, which includes a modular-arithmetic proof alongside the calculations. The **random graph** scripts illustrate a different perspective: studying a combinatorial object through its matrix representation.

## Getting started

Use Python 3 and install the dependencies in a virtual environment:

```sh
python -m venv .venv
```

Activate with `.venv\Scripts\Activate.ps1` in Windows PowerShell, or `source .venv/bin/activate` on macOS/Linux, then run:

```sh
python -m pip install -r requirements.txt
python logistic_map/bifurcations.py
```

Move either slider to update the logistic orbit. Interactive plots require a desktop Matplotlib backend. Each project is a standalone script with parameters near the relevant calculations.

## Examples

```sh
# Integer representations and prime factorizations
python two_squares/sum_of_squares.py

# Enumerate primitive and scaled right triangles
python pythagorean_triples/pythagorean_triples.py

# Eigenvalue histograms for fixed-edge random graphs
python random_graphs/erdos-renyi2.py

# Power of a two-sided normal-mean test
python statistical_power/powercurve.py
```

`random_graphs/erdos-renyi.py` saves histogram images in `plots/` under the working directory. Other plotting scripts display figures; close each window to advance through successive plots. Randomized experiments are unseeded, so repeated runs vary.

For the pi experiment, run from the directory containing its input:

```sh
cd pi_digits
python digits_of_pi.py
```

`pi.txt` contains about 14 MB of digits, including the leading integer digit `3`. The experiment examines prefixes of up to one million digits, including repeated-digit windows and position classes. Its indices include that leading digit, and the repeated scans take longer than the smaller examples.

## Mathematical interpretation

The projects use finite computations to explore patterns. A histogram, fitted curve, or bounded search is evidence on the sampled domain, not a proof of a general conjecture. The sums-of-two-squares project also includes a direct modular-arithmetic proof.

Some implementation details are important when interpreting the output:

- **Collatz:** counters include the terminal call, and grouping divisions by two changes the step convention. The comparison measures iteration counts, not runtime speedup.
- **Digit and graph statistics:** histogram shapes do not establish normality of pi or a limiting spectral law. Distribution comments in the graph script are exploratory. The pi random-frequency snapshot precedes the final increment.
- **Integer searches:** triangle enumeration uses floating-point square roots and legs below 1,000. The multiplicity script `sum_of_squares3.py` has a mismatch-flag naming error, so its final Boolean alone is not a verification.
- **Continuous dynamics:** the plant derivative and chemical nullcline expressions need correction before drawing stability or trapping-region conclusions from those figures.
- **Statistical power:** the curve varies the true mean; the vertical cutoffs instead describe the sample mean under the null hypothesis.

The scripts are small enough to read alongside their output: follow the definitions, inspect the chosen range, and compare the computation with the mathematical claim being explored.
