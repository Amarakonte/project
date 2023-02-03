#!/bin/bash

# Services à vérifier
services=(vsftpd.service bind9.service syslog-ng.service)

for service in "${services[@]}"
do
  # Vérification du statut du service
  status=$(systemctl is-active $service)

  # Si le service est en panne
  if [ "$status" != "active" ]; then
    # Ecriture dans un fichier de log
    echo "Le service $service est en panne." >> /var/log/services.log
  else
    echo "Le service $service fonctionne normalement."
  fi
done
