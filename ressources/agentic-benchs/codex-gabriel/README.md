# Stochastic Interpolants: Dirac Mixtures and Gaussian Geometry

This repository contains a small, reproducible numerical and LaTeX study of
flow matching with stochastic interpolants

\[
X_t=a(t)X_0+b(t)X_1.
\]

It has two parts:

- `python/flow_matching_dirac_mixture.ipynb` derives and simulates the
  conditional expectation velocity when `X0 ~ N(0, I)` and `X1` is a uniform
  mixture of three Dirac masses.
- `python/gaussian_covariance_ellipses.ipynb` derives the Gaussian covariance
  path and exports ellipse figures for the article.
- `paper/main.tex` is a self-contained LaTeX article integrating the generated
  figures and proving the Gaussian endpoint-map theorem.

## Repository Layout

```text
.
├── Makefile
├── README.md
├── requirements.txt
├── todo.md
├── python/
│   ├── build_notebooks.py
│   ├── flow_matching_dirac_mixture.ipynb
│   ├── gaussian_covariance_ellipses.ipynb
│   └── stochastic_interpolants.py
└── paper/
    ├── figures/
    ├── main.tex
    └── references.bib
```

## Reproducing Everything

The local environment used to create the artifacts has Python, PyTorch,
Jupyter, Matplotlib, BibTeX, LaTeX, and Poppler available.

```bash
python3 -m pip install -r requirements.txt
make all
```

The `Makefile` sets two environment variables that are useful on macOS scientific
Python stacks:

- `KMP_DUPLICATE_LIB_OK=TRUE` avoids an OpenMP runtime import clash.
- `MPLCONFIGDIR=$(pwd)/.matplotlib` keeps Matplotlib cache files inside the
  repository instead of the user home directory.

You can also run the steps manually:

```bash
python3 python/check_math.py
python3 python/build_notebooks.py
python3 -m jupyter nbconvert --to notebook --execute --inplace python/flow_matching_dirac_mixture.ipynb
python3 -m jupyter nbconvert --to notebook --execute --inplace python/gaussian_covariance_ellipses.ipynb
cd paper
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Outputs

Executing the notebooks writes publication-ready PDF figures to
`paper/figures/`:

- `dirac_density_velocity.pdf`
- `dirac_schedule_comparison.pdf`
- `dirac_ot_trajectories.pdf`
- `dirac_path_length_comparison.pdf`
- `gaussian_covariance_ellipses.pdf`
- `gaussian_endpoint_maps.pdf`

Compiling the paper writes `paper/main.pdf`.

## Mathematical Summary

For the three-Dirac experiment, the density is the exact Gaussian mixture

\[
p_t(x)=\sum_k \pi_k\varphi_{a(t)^2I}(x-b(t)y_k),
\]

and the velocity is

\[
u_t(x)=\frac{\dot a(t)}{a(t)}x+
\left(\dot b(t)-\frac{\dot a(t)b(t)}{a(t)}\right)
\sum_k \gamma_k(x,t)y_k.
\]

For independent Gaussian endpoints, the paper proves

\[
\Sigma_t=a(t)^2\Sigma_0+b(t)^2\Sigma_1,
\qquad
T_t=\Sigma_0^{1/2}
\left(a(t)^2I+b(t)^2\Sigma_0^{-1/2}\Sigma_1\Sigma_0^{-1/2}\right)^{1/2}
\Sigma_0^{-1/2}.
\]

The endpoint map agrees with the Gaussian optimal-transport map if and only if
`Sigma0` and `Sigma1` commute.
