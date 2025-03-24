# import sys
import json
import click

def formatter(string, sort_keys=True, indent=4):
    # Load incoming string to JSON
    load_json = json.loads(string)
    # Dump as string
    return json.dump(load_json, sort_keys=sort_keys, indent=indent)


@click.command()
@click.argument('path') # From the terminal provide path info instead positional arg from the terminal(#21), also no need sys arg(#1)
def main(path):
    with open(path, 'r') as _f:
        print(
            formatter(_f.read(), sort_keys=True)
        )

if __name__ == '__main__':
    # formatter(sys.arv[-1])
    main()
