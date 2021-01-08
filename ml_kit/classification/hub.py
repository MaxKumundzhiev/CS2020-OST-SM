# ------------------------------------------
# 
# Program created by Maksim Kumundzhiev
#
#
# email: kumundzhievmaxim@gmail.com
# github: https://github.com/KumundzhievMaxim
# -------------------------------------------

from ml_kit.configurations import LOGGER


class Hub:
    @staticmethod
    def train_test_split(x, y, fraction: int, seed: int):
        from sklearn.model_selection import train_test_split
        LOGGER.info('Split data')
        return train_test_split(x, y, test_size=fraction, random_state=seed)

    @staticmethod
    def LogisticRegression(x_train, y_train, x_test, y_test, seed):
        from sklearn.linear_model import LogisticRegression
        from sklearn.metrics import accuracy_score

        # validate input shapes
        assert len(x_train) == len(y_train), 'Unequal shapes of X_train and Y_train'
        assert len(x_test) == len(y_test), 'Unequal shapes of X_test and Y_test'

        LOGGER.info('Utilized Logistic Regression')
        clf = LogisticRegression(random_state=seed).fit(x_train, y_train)
        predictions = clf.predict(x_test)
        score = accuracy_score(y_test, predictions)
        LOGGER.info(f'Logistic Regression score: {score}')
        return score, predictions

    @staticmethod
    def DecisionTree(x_train, y_train, x_test, y_test, seed):
        from sklearn.tree import DecisionTreeClassifier
        from sklearn.metrics import accuracy_score

        LOGGER.info('Utilized Decision Tree Classifier')
        clf = DecisionTreeClassifier(random_state=seed).fit(x_train, y_train)
        predictions = clf.predict(x_test)
        score = accuracy_score(y_test, predictions)
        LOGGER.info(f'Decision Tree Classifier: {score}')
        return score, predictions

    @staticmethod
    def RandomForest(x_train, y_train, x_test, y_test, seed):
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import accuracy_score

        LOGGER.info(f'Utilized Random Forest')
        clf = RandomForestClassifier(random_state=seed).fit(x_train, y_train)
        predictions = clf.predict(x_test)
        score = accuracy_score(y_test, predictions)
        LOGGER.info(f'Random Forest: {score}')
        return score, predictions

