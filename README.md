# AK-CVR
Code to parse AK Cast Vote Records.

New code:
Run AK CVR Ripper2 to convert AK json files(s) to 2 csvs - Marks and Computation. Edit lines 9-15 to reflect the race you want to compute.

Note: 6 C:\\\Path\\\to\\\file must be changed to your file location.

Old code:
Run AK CVR Marks Converter.py first to convert the AK json file(s) to a csv, then run AK CVR Tabulator.py to convert marks to ranks.

Script is very basic - for now, with no input functionality, and must be manually changed for each race.

In the tabulator, py. Edit candidates for relevant candidate numbers and ex-list to change order of eliminated candidates. 

In both, the C:\\\Path\\\to\\\file must be changed to your file location.
