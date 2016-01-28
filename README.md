# coder
###### coding tool that is suitable especially for simpler coding tasks, such as coding tweet or single words. 

Because of the low cognitive load associated with coding boolean variables, coder supports only true or false statements. The user can choose which keys to use. Using 1 and 0 seems to be good as they are far part but at the same level in the keyboard, and also stats tools will widely eat up the resulting format as is. 

Yes, in most cases you will be able to directly load the codebook in to a stats tool of your choice. 

There are two files you need for running coder: 

- this readme
- coder.py (the program code)

And two example sample sets:

- sample.txt (2,000 tweets about privacy for testing purpose)
- sample2.txt (2,000 words that are at least 5 characters long and are commonly used in Twitter)


1) copy the script to a folder /coder or something else and run the commands

   chmod +x coder.py
   touch codebook.txt 

2) create a sample where each item to be coded is on its own individual line

3) run the program by: 

   ./coder.py

...and follow the on-screen sequence. 

After each coded snippet, results are stored in to the codebook.txt file. The output is stored in the codebook in Python list format: 

[['1', '1'], ['1', '1']]

From here it can be converted in to a regular list format with newlines (line breaks) easily. 

   cat codebook.txt | tr ']' '\n' | tr '[' ' ' | sed 's/^,//g' | tr -s ' '
   
In return you will get output like this: 

 '0', '1', '0', '0'
 
 '0', '1', '1', '0'

 '1', '1', '0', '1'

 '0', '1', '1', '0'
