# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------


import argparse

from dataset.utils import *
from dataset.configurations import LOGGER, TRAIN_CICI, TRAIN_VPN, TRAIN_NET


def main():
    parser = argparse.ArgumentParser(description="Data Handler", add_help=True)
    parser.add_argument('-d', '--dataset', action="store", help="dataset path")
    parser.add_argument('-a', '--annotation', action="store", help="annotation level: {top, mid, fine}")

    args = parser.parse_args()

    if args.dataset is None or not os.path.isdir(args.dataset) or args.annotation is None:
        print("No valid dataset set or annotations found!")
        return

    elif args.annotation not in ["top", "mid", "fine"]:
        print("Please select one of these for annotations type: {top, mid, fine}.")
        return
    elif args.annotation == "mid" and (args.dataset.find("NetML") > 0 or args.dataset.find("CICIDS2017") > 0):
        print(
            "NetML and CICIDS2017 datasets cannot be trained with mid-level annotations. Please use either TOP or FINE.")
        return
    else:
        training_set = args.dataset + "/2_training_set"
        training_annotation = args.dataset + "/2_training_annotations/2_training_anno_" + args.annotation + ".json.gz"
        test_set = args.dataset + "/1_test-std_set"
        challenge_set = args.dataset + "/0_test-challenge_set"
        LOGGER.info(f'Process dataset: {args.dataset.split("/")[-1]}')
        LOGGER.info(f'Training set path: {training_set}')
        LOGGER.info(f'Test set path: {test_set}')
        LOGGER.info(f'Training annotation path: {training_annotation}')
        LOGGER.info(f'Challenge set path: {challenge_set}')


if __name__ == "__main__":
    main()

