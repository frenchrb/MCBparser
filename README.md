#MCB Parser

This script produces lists of LCCNs for updated and deleted authority records reported in the monthly [Music Cataloging Bulletin](https://www.musiclibraryassoc.org/?page=musiccatbulletin). These lists can then be used to retrieve the full updated records via OCLC Connexion batch searching or to remove deleted records from your local catalog.

##Requirements
- [Python](https://www.python.org/downloads/) must be installed. This script has been tested with Python 3.5.1 on Windows 8.1.
- A subscription to the [Music Cataloging Bulletin](https://www.musiclibraryassoc.org/?page=musiccatbulletin) is also required. This script has been tested on the January, February, and March 2016 issues. While most of the reported changes are described in a regular format, when parsing earlier or later issues there is always a chance that special cases may occur that the script is not designed to parse.

##Usage
Download MCBparser.py.

To run the script from the command line, first move to the directory where MCBparser.py is located. Type the following and hit Enter:

`python MCBparser.py`

You will then be prompted to enter the year and month to select the issue of the MCB for which you want to retrieve lists of updates.

###Output
Three output files will be created in the same directory where MCBparser.py is located. YYYY and MM are the year and month of the MCB issue.

- `MCB_changes_YYYYMM.txt` contains a list of LCCNs for personal name, corporate name, and preferred title authority records with changed AAPs
- `MCB_deletes_YYYYMM.txt` contains a list of LCCNs for personal name, corporate name, and preferred title authority records that have been deleted
- `MCB_subject_YYYYMM.txt` contains a list of all new and changed LC subject headings; includes genre/form and medium of performance terms

##Author
Rebecca French

##License
This script is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.