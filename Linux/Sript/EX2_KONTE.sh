#!/bin/bash

# Seuil d'espace disque en pourcentage
THRESHOLD=10

# Récupération de l'espace disque utilisé
USED=$(df / | awk '{ print $5 }' | tail -1 | cut -d'%' -f1)

# Vérification de l'espace disque utilisé par rapport au seuil
if [ "$USED" -gt "$THRESHOLD" ]; then
    # Ecriture dans un fichier de log
    echo "L'espace disque est presque plein." >> /var/log/disk_space.log
else
    echo "L'espace disque est suffisant."
fi
