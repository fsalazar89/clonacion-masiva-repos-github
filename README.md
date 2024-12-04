# descarga-masiva-repos-github
Script de python para clonar masivamente todos los repositorios de una cuenta de github, el script crara una carpeta con el nombre repositoriosGit y un archivo de logs con el nombre logs_descarga_repos.txt

### Carpeta repositoriosGit
En esta carpeta quedaran alojados todos los repositorios de la cuenta configurada en el script, cada repositorio se clonara con sus respectivas ramas

### Archivo de logs
El archivo logs_descarga_repos.txt contendra un registro de cada repositorio de la cuanta de github, el repositorio que se clone con exito dejara un registro en el archvio indicando OK y el repositorio que falle en el proceso de clonacion dejara un registro indicando FALLO
#### Ejemplo:
- repositorio-de-prueba1 ------ OK
- repositorio-de-prueba2 ------- FALLO
