# ReadMe

## wordleHelper.py

`wordleHelper.py` filtert fünf-Buchstaben-Wörter aus einer Textdatei entsprechend Wordle-Hinweisen.

```bash
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
```bash
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

## sortLetters.py

Das Skript `sortLetters.py` kann verwendet werden, um aus einer Zeichenkette oder einer gepipeten Wortliste die **häufigsten Buchstaben** zu zählen. Dabei können Buchstaben von der Zählung ausgeschlossen werden.

### Nutzung

```bash
python3 sortLetters.py "abc abc def" -n c
````

Gibt z. B. aus:

```
2x a
2x b
2x d
1x e
1x f
```

### In Kombination mit `wordleHelper.py`

```bash
python3 wordleHelper.py -g o3 t4 -n w e r d i | python3 sortLetters.py -n o t
```


