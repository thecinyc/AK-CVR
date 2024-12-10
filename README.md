# AK-CVR
Code to parse AK Cast Vote Records.

### Cloning the Repo

Clone the repository by running:

```shell
# TODO: update the URL once a repo in GitHub is available
git clone https://github.com/BrightSpots/repo-to-clone.git
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

This runs the main.py script, which convert AK json files(s) to 2 csvs - Marks and Computation. Edit lines 9-15 to reflect the race you want to compute.

Note: 6 C:\\\Path\\\to\\\Files must be changed to your file location.

Script is very basic - for now, with no input functionality, and must be manually changed for each race.

In the tabulator, main.py, Edit candidates for relevant candidate numbers and ex-list to change order of eliminated candidates.
