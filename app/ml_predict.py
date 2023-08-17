def prediction_model(pclass, sex, age, sibsp, parch, fare, embarked, title):
    import pickle
    x = [[pclass, sex, age, sibsp, parch, fare, embarked, title]]
    decisiontree = pickle.load(open('titanic_model.sav', 'rb'))
    predictions = decisiontree.predict(x)
    return predictions