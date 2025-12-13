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

