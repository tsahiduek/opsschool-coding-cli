import click


@click.group()
@click.pass_context
def cloudctl(ctx):
    """ Cloud Manager cli """


@cloudctl.group()
@click.pass_context
def get(ctx):
    """ get object """
    print(ctx)


@get.group()
@click.pass_context
def instances(ctx):
    """ get instances """
    print(ctx)


def start():
    cloudctl(obj={})


if __name__ == "__main__":
    start()
