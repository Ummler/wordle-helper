`wordleHelper.py` filtert fünf-Buchstaben-Wörter aus einer Textdatei entsprechend Wordle-Hinweisen.

```
python3 wordleHelper.py [-f DATEI]
                        -g L# [...]
                        -y L# [...]
                        -n L [...]
```

* `-f` Wortliste (Standard: `validWordleWords.txt`)
* `-g` grün: Buchstabe **L** genau an Position **#**
* `-y` gelb: Buchstabe **L** im Wort, aber **nicht** an Position **#**
* `-n` grau: Buchstabe **L** darf gar nicht vorkommen

Jedes zutreffende Wort wird zeilenweise auf STDOUT ausgegeben.

**Beispiel:** 
```
~/wordle-helper$ python3 wordleHelper.py -g o3 t5 -y s4 t2 -n l g h n
scoot
scout
skort
smoot
smout
smowt
spoot
sport
spout
swopt
```