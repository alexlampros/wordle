# Wordle Solver


## Description

Helps you cheat at wordle by filtering dictionary words, and then sorting the remaining candidates by word popularity. 

Use the ```find_word(string, must="", never="")``` function in the wordle.py file <br><br>

build your string using these keys. 1 key for each character position in the word :<br><br>
  "\w" means allow any letter to go in this character position <br>
  "[^aey]" means that the letters aey will be excluded from this character position, but may appear elsewhere in the word <br>
  "a" means that an "a" goes in this chracter position. <br><br>
  
  must="ayi" means that these characters must appear in the word somewhere<br><br>
  never="zqp" means that these characters never appear in the word.<br><br>




## Example 1: 

First guess "Retail"

![](https://github.com/alexlampros/wordle/blob/main/images/img1.png)

```
find_word("\w\w\w[^a][^i][^l]","ail","ret")

[[261, 'family'], [2182, 'claims'], [3669, 'alumni'], [4283, 'mainly'], [6372, 'villas'], [6474, 'dialog'], [7276, 'valium'], [7571, 'plains'], [9367, 'julian'], [10800, 'manila'], [11330, 'laying'], [11959, 'alison'], [13495, 'diablo'], [15937, 'albion'], [16127, 'malibu'], [16688, 'dialup'], [17712, 'climax'], [19198, 'silica'], [19940, 'libyan'], [20437, 'louisa']]
```


![](https://github.com/alexlampros/wordle/blob/main/images/img2.png)


## Example 2

First guess: Retail

![](https://github.com/alexlampros/wordle/blob/main/images/img2-1.png)

```
find_word("[^r][^e][^t]\w\w\w", "ret", "ail")

[[522, 'street'], [549, 'stores'], [705, 'others'], [1596, 'pretty'], [1648, 'theory'], [1878, 'forest'], [1951, 'poster'], [1991, 'effort'], [2128, 'sorted'], [2154, 'expert'], [2349, 'turned'], [2712, 'hunter'], [2815, 'turkey'], [2988, 'stress'], [2992, 'trends'], [3048, 'poetry'], [3062, 'forget'], [3100, 'export'], [3769, 'puerto'], [3917, 'stored']]
```

![](https://github.com/alexlampros/wordle/blob/main/images/img2-2.png)

```
find_word("[^r]or[^e]\w[^t]", "ret", "ailfs")

[[7899, 'porter'], [11134, 'torque'], [15254, 'cortex'], [16378, 'vortex'], [20010, 'ported'], [26625, 'cortez'], [34141, 'torrey'], [35004, 'mortem'], [40798, 'morten'], [142757, 'tortue'], [153488, 'korten'], [176897, 'tormen'], [186222, 'torney'], [213060, 'horten'], [222867, 'dorter']]
```

![](https://github.com/alexlampros/wordle/blob/main/images/img2-3.png)











