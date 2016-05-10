# coder
###### coding tool that is suitable especially for simpler coding tasks, such as coding tweet or single words. 

Because of the low cognitive load associated with coding boolean variables, coder supports only true or false statements. The user can choose which keys to use. Using 1 and 0 seems to be good as they are far part but at the same level in the keyboard, and also stats tools will widely eat up the resulting format as is. 

Yes, in most cases you will be able to directly load the codebook in to a stats tool of your choice. 

#### for MAC user

You need python 2 to run this. If you are on Mac OS X you most likely already have it. Just start Terminal and type: 

    $ python -v
    
If you get a response with something do with Python, that means you probably are running Python already. Just make sure that it's not a version starting with 3. If you don't get anything like that, then install Python 2.7:

https://www.python.org/downloads/

Once you've installed Python succesfully, run the command to check the version and you should be good to go.

#### for WINDOWS user

1. Download the 2.7.x version:
https://www.python.org/downloads/windows/

2. Find python.exe and add it to Windows PATH:
http://showmedo.com/videotutorials/video?name=960000&fromSeriesID=96

3. Copy the files:
https://github.com/mikkokotila/coder

4. Open windows shell by searching "cmd"

5. Change directory in shell to where you saved the files, using "cd C:\xxxx\yyy"


NOTE: if you did not succeed with #2 above, then just copy the raw files to python directory and run #4 there

#### for LINUX users

You have to know how this works. 

## START USING CODER

There are two files you need for running coder: 

- this readme
- coder.py (the program code)

And two example sample sets:

- sample.txt (2,000 tweets about privacy for testing purpose)
- sample2.txt (2,000 words that are at least 5 characters long and are commonly used in Twitter)


1) copy the script to a folder /coder or something else and run the commands

    $ chmod +x coder.py
    $ touch codebook.txt 

2) create a sample where each item to be coded is on its own individual line

3) run the program by: 

    $ ./coder.py

...and follow the on-screen sequence. 

After each coded snippet, results are stored in to the codebook.txt file. The output is stored in the codebook in Python list format: 

[['1', '1'], ['1', '1']]

From here it can be converted in to a regular list format with newlines (line breaks) easily using the below command. This will also correct common errors the coder may have performed.

    $ cat codebook.txt | sed -e "s/''/'0'/g" -e "s/, ,/, 0,/g" -e "s/10/0/g" -e "s/01/0/g" -e $'s/\], \[/\\\n/g' -e "s/'//g" -e 's/\[//g' -e 's/\]//g'
