import os
from github import Github

# Authentication is defined via github.Auth
from github import Auth

# Get Token from Env
token = os.getenv('GITHUB_TOKEN', '...')
# using an access token
auth = Auth.Token(token)

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
# g = Github(auth=auth, base_url="https://{hostname}/api/v3")

for repo in g.get_organization('hdrinc-dev').get_repos():
    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))