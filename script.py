from bs4 import BeautifulSoup
import requests
import csv

data = open('data.csv', 'w')

csv_writer = csv.writer(data)
csv_writer.writerow(['GeneID','Gene Symbol', 'Gene Name', 'Discontinued?'])
with open('gene_result.xml') as xml_file:
    soup = BeautifulSoup(xml_file, 'xml')

for gene in soup.find_all('Entrezgene'):
    # find appropriate attributes
    geneID = gene.find('Gene-source_src-int').text
    geneSymbol = gene.find('Gene-ref_locus').text
    geneDesc = gene.find('Gene-ref_desc').text

    # note genes that NCBI classifies as discontinued
    try:
        discont = 'DISCONTINUED'
    except Exception as e:
        discont = None
    csv_writer.writerow([geneID, geneSymbol, geneDesc, discont])

data.close()

