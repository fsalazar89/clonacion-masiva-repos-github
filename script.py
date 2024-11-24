import os
import requests

cuentaGitHub = 'xxxxxxxxxxxxxxx'
token = 'ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxx'
ruta_local = 'repositoriosGit'

url = f'https://api.github.com/orgs/{cuentaGitHub}/repos'

headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

repos_ok = []
repos_falla = []

for i in range(3):
    print(i + 1)
    params = {
        'per_page': 100,
        'page': i + 1
    }
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        repos = response.json()
        if len(repos) > 0:
            for repo in repos:
                repo_name = repo['name']
                clone_url = repo['clone_url']

                authenticated_clone_url = clone_url.replace('https://', f'https://{token}@')
                repo_path = os.path.join(ruta_local, repo_name)
                try:

                    os.system(f'git clone {authenticated_clone_url} {repo_path}')


                    os.chdir(repo_path)


                    os.system(f'git fetch --all')


                    branches_output = os.popen(f'git branch -r').read()
                    branches = [branch.strip() for branch in branches_output.splitlines()]

                    for branch in branches:
                        if branch != "origin/HEAD -> origin/main":
                            branch_name = branch.split('/')[-1]
                            os.system(f'git checkout -b {branch_name} {branch}')

                    os.chdir('../..')

                    repos_ok.append(repo_name)
                except Exception as e:
                    print(f'Error clonando el repositorio {repo_name}: {e}')
                    repos_falla.append(repo_name)
    else:
        print(f'Error al conectarse a GitHub: {response.status_code}')

archivo_ok = 'logs_descarga_repos.txt'

with open(archivo_ok, 'w') as file:
    for repo in repos_ok:
        file.write(repo + ' ------ OK\n')
    for repo in repos_falla:
        file.write(repo + ' ------ FALLO\n')

print("Termino...")
