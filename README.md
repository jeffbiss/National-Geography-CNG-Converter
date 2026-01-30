# National-Geographic-CNG-Converter
This repository contains the Jupyter Notebook Python code that converts the NatGeo CD-ROM collection from CNG format to PDF files of JPEG format pages.

This isn't beautiful, but it works. There are two code cells, the first was the initial try and works but if it is stopped, it must be manually stopped or reach the end of the CD-ROM, it starts the entire conversion process from the first file. The second code cell checks for existing directories and files and so will pick up where it left off.

To use this, install Visual Studio Code and open CNGtoJPEGConversion.ipynb. 
