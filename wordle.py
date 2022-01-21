import re
import csv
import os



c = open(os.getcwd()+'/unigram_freq.csv')
r = csv.reader(c)
r = list(r)
r = [ i[0] for i in r[1:] ]

def lookup(word):
        return r.index(word)
        

#string = ""
#string = "r\w[^t]\w[^o]"


def find_word(string, must="", never=""):
        f = open(os.getcwd()+'/wordle_dict.txt')
        f = list(f)
        f = [ f[i][:-1].lower() for i in range(len(f)) ]
        
        hold = []
        is_must = True
        is_never = True
        for i in f:
                p = re.match('^'+string+'$', i)
                if bool(p):
                        for j in must:
                                if not j in p.group():
                                        is_must = False
                        if is_must == True:
                                for k in never:
                                        if k in p.group():
                                                is_never = False
                                        
                                if is_never == True:
                                        hold.append(i)
                        is_must = True
                        is_never = True
                        
                                
        
        return rank_by_pop(hold)[:20]



def rank_by_pop(lis):
        h = []
        for word in lis:
                try:
                        h.append([lookup(word), word])
                except:
                        pass

        return sorted(h, key=lambda x: x[0])





