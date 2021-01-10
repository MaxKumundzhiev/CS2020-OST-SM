# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

from services.ml_kit.configurations import LOGGER


class ModelsHub:
    @staticmethod
    def train_test_split(x, y, fraction: float, seed: int):
        from sklearn.model_selection import train_test_split
        LOGGER.info('Splitted dataset')
        return train_test_split(x, y, test_size=fraction, random_state=seed, shuffle=True)

    @staticmethod
    def logistic_regression(x_train, x_test, y_train, y_test, seed):
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score

        LOGGER.info('Utilized Logistic Regression')
        clf = LogisticRegression(random_state=seed, max_iter=200).fit(x_train, y_train)
        predictions = clf.predict(x_test)
        score = accuracy_score(y_test, predictions)
        LOGGER.info(f'Logistic Regression score: {score}')
        return clf

    @staticmethod
    def decision_tree(x_train, x_test, y_train, y_test, seed):
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score

        LOGGER.info('Utilized Decision Tree Classifier')
        clf = DecisionTreeClassifier(random_state=seed).fit(x_train, y_train)
        predictions = clf.predict(x_test)
        score = accuracy_score(y_test, predictions)
        LOGGER.info(f'Decision Tree Classifier: {score}')
        return clf

    @staticmethod
    def random_forest(x_train, x_test, y_train, y_test, seed):
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        LOGGER.info(f'Utilized Random Forest')
        clf = RandomForestClassifier(random_state=seed).fit(x_train, y_train)
        predictions = clf.predict(x_test)
        score = accuracy_score(y_test, predictions)
        LOGGER.info(f'Random Forest: {score}')
        return clf

