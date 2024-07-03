import glob
import pandas as pd
from pandas.errors import EmptyDataError
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import stor
import  openpyxl
import os
import defopt


"""This function will take a filepath as input for vcf file directory, prepare the the input filepath for further processing and print the filepath.
 Args:
        filepath_in (str): a file path to search for VCF files.

    Returns:
        filepath_in (str): a file path to search for VCF files.

    """
#Input a filepath to search for VCF files
def input_filepath():
    filepath_in = input("Enter the filepath to search for VCF files: ")
    #Expand the user pathe if a tilde is present
    filepath_in = os.path.expanduser(filepath_in)
    #Remove Whitespace
    filepath_in = filepath_in.strip()
    #remove terminal single or double quotes
    filepath_in = filepath_in.strip("'")
    filepath_in = filepath_in.strip('"')

    return filepath_in

# Call the function
filepath_in = input_filepath()
print(filepath_in, "****Input filepath****")



#Input a filepath that will be used to write the output files
"""This function will take a filepath as input for writing to output file, prepare the the output filepath for further processing and print the filepath.
 Args:
        filepath_out (str): a filepath to write the output files.

    Returns:
        filepath_out (str): a file path to write the output files.

    """

def output_filepath():
   filepath_out = input("Enter the filepath to write the output files: ")
   #Expand the user path if a tilde is present
   filepath_out = os.path.expanduser(filepath_out)
   #Remove Whitespace
   filepath_out = filepath_out.strip()
   #remove terminal single or double quotes
   filepath_out = filepath_out.strip("'")
   filepath_out = filepath_out.strip('"')
   return filepath_out

# Call the function
filepath_out = output_filepath()
print(filepath_out, "****Output filepath****")


#Input the number of rows/vcf file to be written to the output file
"""This function will ask for the number of rows to be written to the output file for each vcf file.
    Args:
        input number of rows (int): the number of rows to be written to the output file for each vcf file.

    Returns:
        rows (int): the number of rows to be written to the output file for each vcf file.

    """

def input_rows():
    rows = int(input("Enter the number of rows to be written to the output file for each vcf: "))
    return rows
#Call the function
rows = input_rows()
print(rows, "****Number of rows****")

#Make a list of all the vcf files in the input directory
"""This function will search the input directory for vcf files and make a list of all the vcf files.
    Args:
        filepath_in (str): a file path to search for VCF files.

    Returns:
        vcf_files (list): a list of all the vcf files in the input directory.

    """

def list_vcf_files(filepath_in):
    vcf_files = []
    for file in os.listdir(filepath_in):
        if file.endswith(".vcf"):
            vcf_files.append(file)
    return vcf_files

#Call the function
vcf_files = list_vcf_files(filepath_in)
# Print the VCF files vertically
for vcf_file in vcf_files:
    print(vcf_file)

#Open each vcf file and locate the header row starting with #CHROM and print the row
"""This function will find the header row for each vcf file and print the header row and the following n rows of the vcf file.
    Args:
        vcf_file (str): a vcf file in the input directory.
        rows (int): the number of rows to be written to the output file for each vcf file.

    Returns:
        line (str): the header row for each vcf file.
        file.readline() (str): the following n rows of the vcf file
    """

def header_row(filepath_in, vcf_files):
    for vcf_file in vcf_files:
        with open(filepath_in + "/" + vcf_file, "r") as file:
            for line in file:
                if line.startswith("#CHROM"):
                    print(line)
                    #Print the following n rows of the vcf file
                    for i in range(rows):
                        print(file.readline())

                    break

#Call the function
header_row(filepath_in, vcf_files)

#write a function that will make a dataframe fome the the vcf files using the CHROM, POS, and vcf_file name
"""This function will make a dataframe from the vcf files using the CHROM, POS, and vcf_file name.
    Args:
        vcf_files (str): a vcf file in the input directory.
        rows (int): the number of rows to be written to the output file for each vcf file.
        vcf_file (str): a vcf file in the input directory.

    Returns:
        df (dataframe): a dataframe from the vcf files using the CHROM, POS, and vcf_file name.
    """
def make_dataframe(filepath_in, vcf_files, rows):
    data = []
    for vcf_file in vcf_files:
        with open(filepath_in + "/" + vcf_file, "r") as file:
            for line in file:
                if line.startswith("#CHROM"):
                    for i in range(rows):
                        row = file.readline().split("\t")
                        chrom = row[0]
                        pos = row[0]
                        data.append([chrom, pos, vcf_file])
                    break
    df = pd.DataFrame(data, columns=["#CHROM", "POS", "VCF_Filename"])
    return df

df = make_dataframe(filepath_in, vcf_files, rows)
print(df)

#write the dataframe to a csv file
"""This function will write the dataframe to a csv file.
    Args:
    df (dataframe): a dataframe from the vcf files using the CHROM, POS, and vcf_file name.
    filepath_out (str): a filepath to write the output files.


    Returns:
        df (dataframe): a dataframe from the vcf files using the CHROM, POS, and vcf_file name.
    """

def write_to_csv(df, filepath_out):
    df.to_csv(filepath_out + "/output.csv", index=False)
#Call the function
write_to_csv(df, filepath_out)
