import gzip
import sys
import argparse
import os


def linear_search(key, L):
    hit = -1
    for i  in range(len(L)):
        curr =  L[i]
        if key == curr:
            return i
    return -1


def readGeneCounts(ifile, g_name, ofile):
    	version = None
    	header = None
    	dim = None
    	output = open(ofile, 'w')
    	gene_name_col = 1

    	gene_counts = None

    	for line in gzip.open(ifile, 'rt'):
    		if version is None:
    			version = line
    			continue
    		if dim is None:
    			dim = [int(x) for x in line.rstrip().split('\t')]
    			continue
    	    if header is None:
    	    	header = line.rstrip().split('\t')
    	    	id_d = linear_search("Description", header)
    	    	if(id_d is not -1):
    	    		gene_counts = line.rstrip().split('\t')
    	    		if(gene_counts[id_d] is g_name):
    	    			for i in range(id_d + 1, len(data_header)-1):
                            output.write(header[i]+'\t'+gene_counts[i]+'\n')
    	    	continue




def main():
    parser = argparse.ArgumentParser(
                description="plot data from stdin")

    parser.add_argument('--in_file_name',
                        type=str,
                        help='name of input(gene count) file',
                        required=True)

    parser.add_argument('--gene_name',
                        type=string,
                        help='take "histrogram" or "boxplot" or "combo"',
                        required=True)

    parser.add_argument('--out_file_name',
                        type=string,
                        help='name of output file',
                        required=True)

    args = parser.parse_args()

    readGeneCounts(args.in_file_name, args.out_file_name, args.gene_name)

if __name__ == '__main__':
    main()
