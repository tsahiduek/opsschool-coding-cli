```python
import click
import logging

logging.basicConfig(format=(
    '%(asctime)s %(name)-12s %(funcName)-8s %(message)s'))
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@click.group()
@click.pass_context
def cloudctl(ctx):
    """ Cloud Manager cli """


def start():
    cloudctl(obj={})


if __name__ == "__main__":
    start()

```
