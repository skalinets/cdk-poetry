# Sample repo for CDK + Poetry

This repo is a proof of concept using poetry for CDK stacks.

# How to start

1. Install poetry 

``` bash
brew install poetry
```

2. In the repo start the poetry shell.

``` bash
poetry shell
```

3. Install dependencies

``` bash
poetry install
```

4. Run tests

``` bash
pytest  # for single run
# OR
ptw # for live reload
```

## How to deploy

``` bash
cdk deploy
```

To test the function, use 
``` bash 
aws lambda invoke --function-name test-docker-function out --log-type Tail \
   --query 'LogResult' --output text |  base64 -d
```
