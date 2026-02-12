
        '''Example AI/NLP entry point.'''

        from sklearn import datasets
        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import classification_report
        from sklearn.model_selection import train_test_split


        def run_demo() -> None:
            '''Train a tiny classifier and print a report.'''
            data = datasets.load_iris()
            X_train, X_test, y_train, y_test = train_test_split(
                data.data, data.target, test_size=0.2, random_state=42
            )
            model = RandomForestClassifier(n_estimators=20, random_state=42)
            model.fit(X_train, y_train)
            predictions = model.predict(X_test)
            report = classification_report(y_test, predictions, zero_division=0)
            print("Iris classification report:
", report)


        if __name__ == "__main__":
            run_demo()
