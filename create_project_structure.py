import os

PROJECT_ROOT = "."

folders = [
    # Data layers
    "data/raw",
    "data/processed",
    "data/features",

    # Notebooks (experimentation only)
    "notebooks/eda",
    "notebooks/modeling",

    # Source code (production)
    "src/data_engineering",
    "src/feature_engineering",
    "src/models",
    "src/nlp",
    "src/llm",
    "src/agents",
    "src/api",
    "src/mlops",

    # Cloud & CI/CD
    "cloud/aws",
    ".github/workflows",

    # Tests
    "tests"
]

files = [
    "README.md",
    ".gitignore",

    # Init files
    "src/__init__.py",
    "src/feature_engineering/__init__.py",
    "src/models/__init__.py",
    "src/nlp/__init__.py",
    "src/llm/__init__.py",
    "src/agents/__init__.py",
    "src/api/__init__.py",
    "src/mlops/__init__.py",
]

for folder in folders:
    os.makedirs(os.path.join(PROJECT_ROOT, folder), exist_ok=True)

for file in files:
    path = os.path.join(PROJECT_ROOT, file)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        open(path, "w").close()

print("✅ Industry-level project structure created successfully")
