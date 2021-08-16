# NCBI Scraper for Gene Conversion
A scraper tool to help map other species' genes to human analogs based on NCBI data. This tool provides information such as gene symbol as well as the frequency of a certain gene. Examples of the results of the scraping tool can be viewed in data.csv and freq.csv.

## Usage
If the other species' genes are already in a text file, first convert them to an Excel file whereby all the LOC gene names are in one column. Create another column that is a duplicate of the column created before, except add 'OR' next to each LOC gene name--this is necessary for input into the NCBI gene search builder.

Visit https://www.ncbi.nlm.nih.gov/gene/advanced, click "Edit", and copy and paste the entirety of the second column in your created Excel file into the search builder. Omit the "OR" off the last LOC gene name. Click "Search", which should bring up a table of results. Click the dropdown "Send to" option, and click "Create File". The destination of the download should be in the same directory as script.py.

The BeautifulSoup4 and csv modules will need to be imported before use. Afterwards, run script.py in a command line and two .csv (data.csv and freq.csv) files should be created in the same directory, one of which contains primary data such as Gene Symbol as specified in data.csv. Open the .csv files as an Excel sheet to view the data.

Note: this script does not account for "replaced" genes so those will have to be manually converted.

## Reference for Merging Excel Sheets
If you would like to merge two Excel sheets converted from .csv files such as a sheet for "replaced" gene info and a sheet created from the data.csv file, visit: https://yourbusiness.azcentral.com/subset-data-excel-8074.html.
