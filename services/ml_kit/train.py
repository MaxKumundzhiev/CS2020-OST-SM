# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

import argparse
from pathlib import Path

import pickle
import pandas as pd

# @TODO delete encoding once spark ready
from sklearn.preprocessing import OrdinalEncoder

from services.ml_kit.models.hub import ModelsHub
from services.ml_kit.configurations import LOGGER, NAS, MODELS_CHECKPOINT


def save_model(classifier, dataset_name, type, model):
    destination = Path(MODELS_CHECKPOINT, dataset_name, type, model)
    destination.mkdir(parents=True, exist_ok=True)
    LOGGER.info(f'Created destination folder for dataset: {dataset_name}, type: {type}, mode: {model} at \n {destination}')
    filename = destination / 'model.pkl'

    pickle.dump(classifier, open(filename, 'wb'))
    LOGGER.info(f'Successfully saved model as ')


def run(dataset_name, type, model):
    # @TODO delete encoding once spark ready
    ordinal_encoder = OrdinalEncoder()

    dataset_path = Path(NAS, dataset_name, 'train.csv')
    data = pd.read_csv(dataset_path)
    LOGGER.info(f'Read dataset: {dataset_name} train.csv file')

    if type == 'binary_class':
        data.drop(columns='multi_class', axis=1, inplace=True)
        LOGGER.info(f'Train task: {type}. Dropped multi-class column from train set')

    else:
        data.drop(columns='binary_class', axis=1, inplace=True)
        LOGGER.info(f'Train task: {type}. Dropped binary-class column from train set')

    # @TODO delete encoding once spark ready
    data['y'] = ordinal_encoder.fit_transform(data[[f'{type}']])

    data.drop(columns=f'{type}', axis=1, inplace=True)

    # @TODO delete line once spark ready
    for column in data.columns:
        data[f'{column}'].fillna((data[f'{column}'].mean()), inplace=True)

    _x = data.drop(columns='y', axis=1)
    _y = data['y']
    LOGGER.debug(f'Initial dataset shape - x: {_x.shape}, y: {_y.shape}')

    X_train, X_test, y_train, y_test = ModelsHub.train_test_split(x=_x, y=_y, fraction=.2, seed=241)
    LOGGER.info(f'X_train shape: {X_train.shape}')
    LOGGER.info(f'y_train shape: {y_train.shape}')
    LOGGER.info(f'X_test shape: {X_test.shape}')
    LOGGER.info(f'y_test shape: {y_test.shape}')

    if model == 'logistic-regressor':
        _model = ModelsHub.logistic_regression(X_train, X_test, y_train, y_test, seed=241)
        save_model(classifier=_model, dataset_name=dataset_name, type=type, model=model)

    elif model == 'decision-tree':
        _model = ModelsHub.decision_tree(X_train, X_test, y_train, y_test, seed=241)
        save_model(classifier=_model, dataset_name=dataset_name, type=type, model=model)

    elif model == 'random-forest':
        _model = ModelsHub.random_forest(X_train, X_test, y_train, y_test, seed=241)
        save_model(classifier=_model, dataset_name=dataset_name, type=type, model=model)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Interface to train particular model on particular dataset",
                                     add_help=True)
    # @TODO once spark finished choices should be changed at: ['SELECTED_CICIDS', 'SELECTED_NET']
    parser.add_argument('-d', '--dataset', action="store", help="source dataset name",
                        choices=['TRANSFORMED_CICIDS', 'TRANSFORMED_NET'], required=True)

    parser.add_argument('-t', '--type', action="store", help="type of task",
                        choices=['binary_class', 'multi_class'], required=True)

    parser.add_argument('-m', '--model', action="store", help="type of dataset",
                        choices=['logistic-regressor', 'decision-tree', 'random-forest'], required=True)

    args = parser.parse_args()

    run(dataset_name=args.dataset,
        type=args.type,
        model=args.model
        )

