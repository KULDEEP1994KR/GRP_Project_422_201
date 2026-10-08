import subprocess
import sys
from pathlib import Path


# Find the project folder where orchestration.py is located
PROJECT_DIR = Path(__file__).resolve().parent

# Location of notebooks
CODE_DIR = PROJECT_DIR / "Code"


# Run notebooks in this order
notebooks = [
    "listing_project.ipynb",
    "Christ_data.ipynb",
    "tenancy.ipynb",
    "new_christ_bond.ipynb",
    "compare_prop.ipynb"
]


def run_notebook(notebook):

    notebook_path = CODE_DIR / notebook

    print("\n" + "=" * 60)
    print(f"Running: {notebook}")
    print("=" * 60)

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--inplace",
            str(notebook_path)
        ],
        cwd=PROJECT_DIR,
        capture_output=True,
        text=True
    )

    if result.returncode != 0:

        print(f"\nERROR: {notebook} failed!\n")
        print(result.stderr)

        sys.exit(1)

    print(f"Completed successfully: {notebook}")


def main():

    print("\nStarting data orchestration...")
    print(f"Project folder: {PROJECT_DIR}")

    for notebook in notebooks:
        run_notebook(notebook)

    print("\n" + "=" * 60)
    print("ALL NOTEBOOKS COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    main()