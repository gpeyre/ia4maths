SHELL := /bin/zsh

export KMP_DUPLICATE_LIB_OK := TRUE
export MPLCONFIGDIR := $(CURDIR)/.matplotlib

.PHONY: notebooks paper check all clean

all: check notebooks paper

check:
	PYTHONDONTWRITEBYTECODE=1 python3 python/check_math.py

notebooks:
	python3 python/build_notebooks.py
	python3 -m jupyter nbconvert --to notebook --execute --inplace python/flow_matching_dirac_mixture.ipynb --ExecutePreprocessor.timeout=900
	python3 -m jupyter nbconvert --to notebook --execute --inplace python/gaussian_covariance_ellipses.ipynb --ExecutePreprocessor.timeout=900

paper:
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cd paper && bibtex main
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex
	cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex

clean:
	rm -f paper/*.aux paper/*.bbl paper/*.blg paper/*.log paper/*.out paper/*.toc
	rm -rf .matplotlib tmp/pdfs
