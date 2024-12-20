# Présentation du problème

Fraîchement recruté au PEReN, votre première mission consiste à déceler d'éventuels biais dans l'algorithme de fixation des prix d'une plateforme fictive de VTC dénommée "Hubert".

La plateforme vous a communiqué un fichier CSV qui contient l'historique des courses réalisées sur le mois de janvier 2023 dans Paris. Chaque ligne contient 3 variables : `timestamp` qui correspond à l'heure de commande du VTC, `raw_start_location` qui correspond à l'adresse de prise en charge et `raw_end_location` qui correspond à l'adresse de destination.

Vous commencerez dans un premier temps par explorer le jeu de données et produire les visualisations qui vous paraissent pertinentes.

Vous tenterez ensuite de modéliser les tarifs de course en utilisant le ou les modèles de votre choix. Vous évaluerez la qualité de votre (ou vos) modèle(s) et produirez une analyse critique des résultats.

S'il vous reste du temps, vous pourrez tenter de répondre à la question suivante : est-il possible d'identifier d'éventuels biais dans le jeu de données ou de déterminer les variables qui ne sont pas utilisées par Hubert dans son calcul de prix de course parmi les variables à votre disposition ? 

# Données supplémentaires

A toutes fins utiles, les jeux de données suivants vous sont fournis : 
- Des données Météo-France qui comprennent l'historique des températures et des niveaux de pluie sur le mois de janvier 2023 heure par heure. La colonne `rain_level` indique un niveau de pluie entre 0 et 3 (0 = pas de pluie, 1 = pluie légère, 2 = pluie modérée, 3 = pluie forte)
- La Base Adresse Nationale de Paris (accessible à cette adresse : https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-75.csv.gz) qui comporte des informations utiles sur les adresses parisiennes.

**Attention** : Les adresses présentes dans le jeu de données Hubert sont de la forme `[numero][rep], [nom voie], [nom commune]` (`[rep]` correspond aux suffixes bis, ter,...).


# Format de réponse attendu

Le projet doit être retourné sous format `.zip` et doit comporter un Jupyter notebook ainsi qu'un fichier qui liste les dépendances nécessaires à la bonne exécution du notebook. 
