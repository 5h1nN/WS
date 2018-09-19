
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
1. Country 
2. Name of the player
3. 50 card code 
4. Favourite card's code 

# Instructions:
1. Create a new file decklist 
2. Copy the content of decklist-template and fill the respective information
3. Run the generateDeckList.py file to generate the decklist to be printed 