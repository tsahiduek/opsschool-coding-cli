# Making your own CLI

This repo will demonstrate how to use coding fundamentals to create our own tool.
We'll call this tool `cloudctl`, which will be a simplified and unified CLI to the Cloud Providers used in your organization.

## Prerequisites

As covered, we'll use the following tools:

- [Click - Python library for CLI](https://click.palletsprojects.com/en/7.x/ "Click Homepage")
- [Virtualenv - tool for isolated python environment](https://virtualenv.pypa.io "Virtualenv RTD")

## Instructions

### Creating virtualenv for your project

Let's start by creating our workspace:

```bash
[ ! -d ~/.virtualenvs ] && mkdir ~/.virtualenvs
mkdir cloudctl
cd cloudctl
virtualenv  ~/.virtualenvs/cloudctl
source ~/.virtualenvs/cloudctl/bin/activate
```

`source ~/.virtualenvs/cloudctl/bin/activate` will open a new shell with `cloudctl` virtualenv. To exit this shell, type `deactivate`.

### Writing your CLI "hierarchy"

Our cli will be called `cloudctl`.
For start we'll support `get` and `stop` command for `instances` resource.
In addition, the CLI should support additional params of `tags` and `cloud` (which represent cloud provider).

The output should look like:

```
(cloudctl)$ cloudctl
Usage: cloudctl [OPTIONS] COMMAND [ARGS]...

  Cloud Manager cli

Options:
  -t, --tags <TEXT TEXT>...    Query resources by tags
  -c, --cloud [aws|gcp|azure]  Cloud provider to query  [default: aws]

  --help                       Show this message and exit.

Commands:
  get   get action
  stop  stop action

---------------------------------

(cloudctl)$ cloudctl get
Usage: cloudctl get [OPTIONS] COMMAND [ARGS]...

  get action

Options:
  --help  Show this message and exit.

Commands:
  instances
```

Follow click [documentation](https://click.palletsprojects.com/en/7.x/) to create your first cli hierarchy.

If you're struggling with how to start, follow this [starter](cloudctl_starter.md)

### Test your CLI

In your virtualenv shell type:

`python cloudctl --help`

Your output should look like this:

```
(cloudctl)$ cloudctl --help
Usage: cloudctl [OPTIONS] COMMAND [ARGS]...

  Cloud Manager cli

Options:
  -t, --tags <TEXT TEXT>...    Query resources by tags
  -c, --cloud [aws|gcp|azure]  Cloud provider to query  [default: aws]
  --help                       Show this message and exit.

Commands:
  get   get action
  stop  stop action
```

### Set your CLI to run from the command line

### Writing your CLI logic
