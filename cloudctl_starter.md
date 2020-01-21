```python
import click


@click.group()
@click.pass_context
def cloudctl(ctx):
    """ Cloud Manager cli """


def start():
    cloudctl(obj={})


if __name__ == "__main__":
    start()

```
