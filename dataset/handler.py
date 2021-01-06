# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import os
import time
import argparse

from dataset.helper import *
from dataset.configurations import LOGGER


def main():
    parser = argparse.ArgumentParser(description="Data handler entry point", add_help=True)
    parser.add_argument('-d', '--dataset', action="store", help="dataset path", required=True)
    parser.add_argument('-a', '--annotation', action="store", help="annotation level: {top, mid, fine}", required=True)

    args = parser.parse_args()

    if args.dataset is None or not os.path.isdir(args.dataset) or args.annotation is None:
        LOGGER.info("No valid dataset set or annotations found!")
        return

    elif args.annotation not in ["top", "mid", "fine"]:
        LOGGER.info("Please select one of these for annotations type: {top, mid, fine}.")
        return
    elif args.annotation == "mid" and (args.dataset.find("NetML") > 0 or args.dataset.find("CICIDS2017") > 0):
        LOGGER.info("NetML & CICIDS cannot be trained with mid-level annotations. Please use either TOP or FINE.")
        return
    else:
        training_set = args.dataset + "/2_training_set"
        training_annotation = args.dataset + "/2_training_annotations/2_training_anno_" + args.annotation + ".json.gz"
        test_set = args.dataset + "/1_test-std_set"
        challenge_set = args.dataset + "/0_test-challenge_set"

        dataset_name = args.dataset.split("/")[-1]
        LOGGER.info(f'Process dataset: {dataset_name}')
        LOGGER.info(f'Training set path: {training_set}')
        LOGGER.info(f'Test set path: {test_set}')
        LOGGER.info(f'Training annotation path: {training_annotation}')
        LOGGER.info(f'Challenge set path: {challenge_set}')

    LOGGER.info(f'Retrieving dataset: {dataset_name}')
    train_df, y_train, class_label_pair, X_train_ids = get_training_data(training_set, training_annotation)
    test_df, _ = get_train_data(test_set)

    save_dir_train = './NAS/' + dataset_name + '/train/' + f'{args.annotation}'
    save_dir_test = './NAS/' + dataset_name + '/test/'

    os.makedirs(save_dir_train, exist_ok=True)
    LOGGER.info(f'Created directory: {save_dir_train}')

    os.makedirs(save_dir_test, exist_ok=True)
    LOGGER.info(f'Created directory: {save_dir_test}')

    save_train(train_df, y_train, class_label_pair, X_train_ids, save_dir_train)
    save_test(test_df, save_dir_test)


if __name__ == "__main__":
    main()





