# Install pre-commit and git lint tool 
pip install pre-commit  
pip install gitlint

# Copy files into repository
Those files must be paste in the repository 
.pre-commit-config.yaml
.gitlint
gitlint_rules/gitlint_emoji.py

# Install the pre-commit hook into repository
pre-commit install  
pre-commit run --all-files

# Commit the modified files and .pre-commit-config.yaml with the following commit message : 
👷 (project) add pre-commit hooks

I want the project to adhere to best practices using classic pre-commit hooks.

# Commit the gitlint files with the following message : 
🔧 (project) add gitlint configuration file

I want to enforce every commit the FUN way (see: https://handbook.openfun.fr/git) with an emoji, the scope, the subject and a body.

# FINISH it should work perfectly 
