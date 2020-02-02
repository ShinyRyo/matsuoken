"""
best_scoreなモデルを選びたい。
引数をモデル、テストサイズ、パラメータとして回す。
評価方法も選びたい。accuracy, mse, 
デフォルトはこれから設定。随時更新できるような感じが良い。たぶん使用頻度で更新。
"""
def model_iter(X_train, X_test, y_train, y_test,best_score,best_method):
    model_list=[]
    a = 0 #best_scoreとbest_methodを判断するために過学習の小さいものから選ぶ
    for i in model_list:
        model = i
        model.fit(X_train, y_train)
        D = abs(model.score(X_train, y_train) - model.score(X_test, y_test))
        if best_score == 0: #1番はじめ
            best_score = model.score(X_test, y_test)
            best_method = model.__class__.__name__
            a = D
        elif model.score(X_test, y_test) > best_score:
            best_score = model.score(X_test, y_test)
            best_method = model.__class__.__name__
            a = D
        elif model.score(X_test, y_test) == best_score:
            if D < a:
              a = D
              best_score = model.score(X_test, y_test)
              best_method = model.__class__.__name__
    my_result = best_method
    return my_result