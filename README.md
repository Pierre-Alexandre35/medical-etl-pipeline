# pipeline


## Quels sont les éléments à considérer pour faire évoluer votre code afin qu’il puisse gérer de grosses volumétries de données (fichiers de plusieurs To ou millions de fichiers par exemple) ? Pourriez-vous décrire les modifications qu’il faudrait apporter, s’il y en a, pour prendre en considération de telles volumétries ?


Il existe de nombreux outils Cloud qui permettent de faire runner une pipeline ETL avec de grosses volumétries de données. Je pense qu'une solution optimale pour migrer facilement la pipeline actuelle est GCP Dataflow + BigQuery. Chaque Dataflow job peut utiliser au maximum 1000 Compute Engine instances et 1 projet GCP peut avoir jusqu'a 25 concurrent Dataflows jobs. Voici les modifications qu'il faudrai ajouter au code:
- 
- 
-



# ToDo
- remplir le readme
- testing 
- dossier DEVOPS (Dockerfile)
- Import order
- Extract, Validate (voir si le fichier respecte les normes -> sinon Expect), Process (traitement des valeurs manqueantes et transformations), Post-Process 
- Creer docker


SCALABILITE:
- Distribution OU ingerer le fichier en BQ  
