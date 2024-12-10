# AK-CVR
Code to parse AK Cast Vote Records.

### Cloning the Repo

Clone the repository by running:

```shell
git clone https://github.com/nurse-the-code/cinyc-ak-cvr-tabulator-2024.git
```

### Installing Dependencies

Install the dependencies by running:

```shell
poetry install
```

## Usage

```shell
poetry run python main.py
```

This runs the `main.py` script, which convert AK json files(s) to 2 csvs - Marks and Computation. Edit lines 16-27 to reflect the race you want to compute.

Note: `path_to_alaska_dominion_cvrs` and `path_to_output_cinyc_files` must be changed to your file location.

Script is very basic - for now, with no input functionality, and must be manually changed for each race.

In the tabulator, main.py, Edit candidates for relevant candidate numbers and ex-list to change order of eliminated candidates.
