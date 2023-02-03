#!/bin/bash
cd /root
# Demande à l'utilisateur d'entrer son nom
read -p "Quel est votre nom? " nom

# Vérifie si l'utilisateur existe réellement
if getent passwd "$nom" >/dev/null 2>&1; then
  # Affiche "Bonjour, [nom de l'utilisateur]!"
  echo "Bonjour, $nom!"
else
  # Affiche un message d'erreur
  echo "Désolé, l'utilisateur $nom n'existe pas."
  exit 1
fi

echo "voici les repertoire : "
ls -a

read -p "Entrez le nom de votre répertoire: " rep

# vérifie si un répertoire existe
if [ -d "$rep" ]; then
  # vérifie les droit de l'utilisateur
  permissions=$(ls -ld "$rep" | awk '{print $1}')
  if [ "${permissions:1:1}" = "r" ] && [ "${permissions:3:1}" = "x" ]; then
    # change le répertoire courant
    cd "$rep"
  else
    echo "Vous n'avez pas les autorisations appropriées pour accéder à ce répertoire."
    exit 1
  fi
else
  # Affiche un message d'erreur
  echo "Désolé, le répertoire $rep n'existe pas."
  exit 1
fi
# Affiche tous les fichiers du répertoire courant, y compris les fichiers cachés
echo "Voici la liste des fichiers dans le répertoire $rep:"
ls -a
read -p "choisi un fichier : " fiche

# Vérifie si un fichier spécifié en argument existe
if [ -e "$fiche" ]; then 
  # Affiche le contenu du fichier
  cat "$fiche"
else
  # Affiche un message d'erreur
  echo "Erreur: le fichier $fiche n'existe pas."
fi
