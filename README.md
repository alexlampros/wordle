# wordle
Wordle Solver

First we type in a random word. Ratio is a good one to start with

![](https://github.com/alexlampros/wordle/blob/main/images/img1.png)

From this result, we know that "r" and "i" must be in the word. We also know that "a", "t" and "o" cannot be in the word. Finally, we know that "r" cannot be in position 0, and "i" cannot be in position 3. 

To translate this information into the find_word() function. The find_word function takes 3 parameters find_word(string,must="",never="")
The second and third parameter are easiest, so let's start with them first. 

find_word("",must="ri",never="ato")

Now we build our string. 

There are 5 character positions in the string, each corresponding to the letter we are trying to figure out. 
If all we know is that a random letter must be in a position, the we fill the character position with "\w""
If we know that a certain character goes in that position, then we fill in that character
If we know that a character cannot go in this position (say "r" for example), then we fill the character position with [\^r']

Thus to build our string for this first iteration we write: 
find_word("[^r]\w\w[^i]\w","ri","ato")
[[100, 'price'], [583, 'girls'], [736, 'drive'], [1424, 'bring'], [2009, 'crime'], [2107, 'prime'], [2223, 'virus'], [2435, 'brief'], [2723, 'drink'], [3013, 'irish'], [3023, 'firms'], [3727, 'birds'], [4061, 'inner'], [4299, 'prize'], [4450, 'fiber'], [4699, 'pride'], [5361, 'liver'], [5548, 'weird'], [6057, 'grill'], [6889, 'bride']]

The function will return the top 20 words that match our filter setting, sorted by most commonly used words. 

lets try guessing "price" next

![](https://github.com/alexlampros/wordle/blob/main/images/img2.png)









