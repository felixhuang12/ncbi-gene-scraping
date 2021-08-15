from bs4 import BeautifulSoup
import csv

# create primary csv file
data = open('data.csv', 'w', newline='')

# create writer and headers for data types
csv_writer = csv.writer(data)
csv_writer.writerow(['GeneID','Gene Symbol', 'Gene Full Name', 'Discontinued?'])

# open xml file downloaded from NCBI database
with open('gene_result.xml') as xml_file:
    soup = BeautifulSoup(xml_file, 'xml')

# map frequencies to genes
def freqDict(dict):
    with open('freq.csv', 'w', newline='') as f: 
        writer = csv.writer(f)
        writer.writerow(['Gene Symbol', 'Number of Occurrences'])
        for geneSymbol, freq in dict.items():
            writer.writerow([geneSymbol, freq])

# scrape data from xml file
def scrape():
    frequencies = {}
    for gene in soup.find_all('Entrezgene'):
        # desired attributes
        geneID = gene.find('Gene-source_src-int').text
        geneSymbol = gene.find('Gene-ref_locus').text
        geneDesc = gene.find('Gene-ref_desc').text

        # special note for the genes that NCBI classifies as discontinued
        try:
            discont = gene.find('Entrezgene_summary').text
            if (discont):
                discont = 'DISCONTINUED'
        except Exception as e:
            discont = ''

        # counting and updating frequencies of genes
        if(discont):
            pass
        elif (geneSymbol in frequencies):
            frequencies[geneSymbol] += 1
        else:
            frequencies.update({geneSymbol:1})
        
        csv_writer.writerow([geneID, geneSymbol, geneDesc, discont])
    freqDict(frequencies)

scrape()
data.close()