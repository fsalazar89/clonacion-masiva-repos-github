# Clonación masiva de repositorios GitHub
Script de Python para clonar masivamente todos los repositorios de una cuenta de GitHub. El script creará una carpeta con el nombre repositoriosGit y un archivo de logs con el nombre logs_descarga_repos.txt.

# Configuración
Solo se deben ajustar los valores de las siguientes variables con el nombre de la cuenta de GitHub y el token generado en GitHub con permisos para clonar los proyectos.

```
cuentaGitHub = 'xxxxxxxxxxxxxxx'
token = 'ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

## Carpeta repositoriosGit
En esta carpeta quedarán alojados todos los repositorios de la cuenta configurada en el script. Cada repositorio se clonará con sus respectivas ramas.

## Archivo de logs
El archivo logs_descarga_repos.txt contendrá un registro de cada repositorio de la cuenta de GitHub. El repositorio que se clone con éxito dejará un registro en el archivo indicando OK y el repositorio que falle en el proceso de clonación dejará un registro indicando FALLO.
### Ejemplo:
repositorio-de-prueba1 ------ OK
repositorio-de-prueba2 ------- FALLO
