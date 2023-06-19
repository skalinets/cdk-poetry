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

# Current issues and concerns

Currently code works, however there are some items looking suboptimal. 

- *Nested package directories*. If we want to create a package, we need to 
create a nested directory with the same name, eg. `package1/package1`. 

- *Explicit install of dependencies*. See [Dockerfile](./cdk_poetry/lambdas/hello_world/Dockerfile#14) – if lines 14-15 are removed, the `common` package will be installed, 
however its dependencies, ie pendulum won't. 

- *Suboptimal Dockerfile*. It is not obvious how to add multistage builds here
because there is more than one `pyproject.toml`. Also `.dockerignore` might be
helpful.
