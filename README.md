
A simple python script that automates the process of filling in the decklist form.

```sh
Usage: python generateDeckList.py 
```

# Description
It takes in the card code specified in the **decklist ** file and fetch the corresponding japanese name of the card from the official ws tcg site before filling it into the form.  

#### Note that:
1. You still have to create and fill in the list of card code 
2. If there is any changes to the template in the future, please update/replace the template.pdf. There might be a need to update the numbers in the script if there is any changes to the template. 
3. The structure of the decklist file is as follows:
a. Country 
b. Name of the player
c. 50 card code 
d. Favourite card's code 

# Instructions:
```sh
Create a new file decklist 
Copy the content of decklist-template and fill the respective information
Run the generateDeckList.py file to generate the decklist to be printed 
```