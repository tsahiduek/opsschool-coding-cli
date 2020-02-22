# Making your own CLI

This repo will demonstrate how to use coding fundamentals to create our own tool.
We'll call this tool `cloudctl`, which will be a simplified and unified CLI to the Cloud Providers used in your organization.

## Prerequisites

As covered, we'll use the following tools:

- [Click - Python package for CLI](https://click.palletsprojects.com/en/7.x/ "Click Homepage")
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

### Writing your CLI logic

Our CLI should interact with AWS API to retrieve the data it needs. In python, we have [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html). Boto3 is a package/SDK that already implemented and exposes many different AWS API endpoints ready for use. Instead of calling AWS API directly (and implementing all the logic that is needed around it, such as: retry, error handling, support different API endpoint, etc...), Boto3 expose to the developer set of predefined classes and functions that can be consumed very easily.

Use Boto3 to implement the logic for the `get instances` command. This is a direct link to the [`describe_instances`](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances) command which you'll need to use for this. The output should look something like this (I've used another package to make the output more "tabulate" - I'll let you to google for it :-):

```
(cloudctl) tsahiduek:cloudctl Tashi.Duek$ cloudctl get instances
Id                   Name    State    name
-------------------  ------  -------  -----------------------------------------
i-08548cc86a6159509          running  nodes.kops.spot8s.com
i-0a62ea0a882407d58          running  master-us-west-2b.masters.kops.spot8s.com
i-0886cb9d63dccf69d          running  bastions.kops.spot8s.com
i-06cc0db7be322489a          running  master-us-west-2a.masters.kops.spot8s.com
i-076329695031a064d          running  master-us-west-2c.masters.kops.spot8s.com
```

Another note about Boto3 and its advantage:
Take a look at the AWS guide of interacting with the AWS API _without_ Boto3 package:
https://docs.aws.amazon.com/general/latest/gr/sigv4-signed-request-examples.html#sig-v4-examples-get-auth-header
