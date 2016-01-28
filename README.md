# coder
###### coding tool that is suitable especially for simpler coding tasks, such as coding tweet or single words. 

1) copy the script to a folder /coder or something else and run the commands

   chmod +x coder.py
   touch codebook.txt 

2) create a sample where each item to be coded 

3) run the program by: 

   ./coder.py

...and follow the on-screen sequence. 

After each coded snippet, results are stored in to the codebook.txt file. The output is stored in the codebook in Python list format: 

[['1', '1'], ['1', '1']]

From here it can be converted in to a regular list format with newlines (line breaks) easily. 

   cat codebook.txt | tr ']' '\n' | tr '[' ' ' | sed 's/^,//g' | tr -s ' '
