# AI Algos — Semester 5 

A curated collection of implementations, notebooks, assignments and experiments for AI algorithms covered in Semester 5. This repository collects algorithmic implementations, visualizations and practice problems to help learn and teach core AI techniques (search, optimization, probabilistic models, ML algorithms and more).

Goals
- Provide clear, well-documented implementations of algorithms taught in the course.
- Offer reproducible examples and datasets (or links) for exercises and assignments.
- Be a learning resource and a starter codebase for student projects.

Table of contents
- Overview
- Repository structure
- Languages & tools
- Installation
- Quick start
- How to run notebooks and scripts
- Datasets
- Tests
- Contribution guide
- License & contact

Overview
This repository is organized to separate conceptual notebooks and polished algorithm implementations. Notebooks are used for interactive exploration and visual explanation; scripts and modules contain reusable implementations suitable for assignments and integration into larger projects.

Repository structure (suggested)
- README.md — this file
- requirements.txt — Python dependencies
- environment.yml — optional Conda environment
- notebooks/ — Jupyter notebooks used for teaching, demos and experiments
- algorithms/ — library-style implementations (Python packages/modules)
  - search/
  - optimization/
  - probabilistic_models/
  - ml/  (classical ML algorithms)
  - deep_learning/ (if applicable)
- assignments/ — assignment statements, starter code and solutions (if included)
- data/ — small datasets, or scripts that download datasets
- examples/ — runnable example scripts demonstrating usage
- tests/ — unit tests and test data
- docs/ — additional notes, lecture slides, or generated docs

Languages & tools
- Primary: Python (>=3.8 recommended)
- Jupyter / JupyterLab for notebooks
- Typical libraries: numpy, scipy, scikit-learn, matplotlib, seaborn, pandas, networkx, tqdm, jupyter, torch / tensorflow (only if deep learning content)
- Linting/formatting: black, flake8 (optional)

Installation

Option A — using pip (recommended)
1. Clone the repo
   git clone https://github.com/maithilimukherjee/ai-algos-sem5.git
   cd ai-algos-sem5
2. Create and activate a virtual environment
   python -m venv .venv
   source .venv/bin/activate    # macOS / Linux
   .\.venv\Scripts\activate     # Windows (PowerShell)
3. Install dependencies
   pip install -r requirements.txt

Option B — using conda (if environment.yml provided)
1. conda env create -f environment.yml
2. conda activate ai-algos-sem5

Quick start examples

Run a notebook
1. Start Jupyter Lab
   jupyter lab
2. Open a notebook from the notebooks/ directory and run cells interactively.

Run an example script
- Examples are placed under examples/ — run them directly:
  python examples/run_example_search.py

Use library modules
- Import algorithm implementations from the algorithms package:
  from algorithms.search.a_star import a_star
  path = a_star(start, goal, graph, heuristic)

How to run notebooks and scripts reproducibly
- Keep a requirements.txt with pinned versions.
- Use environment.yml for conda users to reproduce the environment.
- Notebooks can be executed headlessly for reproducible runs:
  pip install nbconvert
  jupyter nbconvert --to notebook --execute notebooks/your_notebook.ipynb --output executed_notebook.ipynb

Datasets
- Small, course-specific datasets should be committed under data/ (if license allows).
- For larger public datasets, include a download script in data/scripts/ or document external links and preprocessing steps in notebooks/ or docs/.

Tests
- Tests are under tests/ and use pytest.
- Run tests with:
  pip install -r requirements-dev.txt  # if separate dev requirements exist
  pytest -q

Contributing
Contributions are welcome — student improvements, bug fixes, additional notebooks, better visualizations and new algorithms.
Suggested workflow:
1. Fork the repo and create a feature branch:
   git checkout -b feat/your-feature
2. Make changes, add tests and documentation.
3. Run formatting and linting:
   black .
   flake8
4. Create a PR with a clear description of what changed and why.

Coding guidelines
- Prefer clear, well-documented code and type hints where helpful.
- Keep algorithms modular and testable.
- Notebooks should include goal, explanation, and results sections; keep them runnable from a fresh environment when possible.

License
This project is intended to be open and reusable. If no license file exists yet, add one. A common choice is the MIT License. Example header:
MIT License (c) 2025 Maithili Mukherjee

(Replace year/name as appropriate; add LICENSE file to the repo.)

Acknowledgements & references
- Cite textbooks, lecture notes and external resources used while implementing algorithms.
- If any code is adapted from other repositories, document the source and ensure license compatibility.

Maintainer / Contact
- GitHub: @maithilimukherjee
- For questions, open an issue in the repo and tag the maintainers.

