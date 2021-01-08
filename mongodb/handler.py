# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import argparse
from mongodb.utils import Factory


def main(action: str, dataset: str):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MongoDB interface to upload source dataset(S)")
    parser.add_argument('--action', '-a', required=True, help='type of action to apply', choices=['upload'])
    parser.add_argument('--dataset', '-d', required=True, help='datasets', choices=['cicidc', 'netml', 'nonvpn', 'all'])

    args = parser.parse_args()

    main(action=args.action, dataset=args.dataset)

