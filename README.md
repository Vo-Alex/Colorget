# ColorGet
Génère une image représentant les couleurs d'un film.

# Instalation
Les librairies suivantes doivent être installées :

On utilisara le paquet **python3-pip**

+ NumPy
``` bash
python3 -m pip install numpy
```

+ OpenCV
``` bash
python3 -m pip install opencv-python
```

# Utilisation

Pour lancer le script il fait mettre le script et le film dans le même répertoire racine.

Le script de lance avec la commande suivante:
```bash
python3 colorget.py NomDuFilme IntervaleDechantionage TailleEchantionX TailleEchantionY 
```

## Exemple:

Pour le film Your Name avec un échantillon toutes les 2 secondes et des échantillons de 1 par 300:

``` bash
python3 colorget.py your_name.mkv 2 1 300
```

Le résultat obtenu est le suivant:

![](./exemple/your_name.jpeg)