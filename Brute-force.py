def best_model(train, test, model_list):
  #初期値の設定
  best_score = 0
  best_size = 0
  best_factor = ""
  best_method = ""
  a_list=[]
  #抽出するデータ項目の全組み合わせ
  for i in range(1, len(test.columns)+1):
    a = list(itertools.combinations(test.columns, i))
    #print(i, a)
    a_list.append(a)
  for i in a_list[::-1]: #iはn個抽出した時の項目の組み合わせを格納
    for j in i: #jはiの組み合わせを1組ずつ抽出
      #print('current check: ', j)
      #実際の抽出
      X = train[list(j)]
      y = train['quality']

      test_size = [0.5, 0.3, 0.25, 0.2, 0.1]
      #n個の組み合わせ毎に一番良い値とその時のテストサイズを抽出するための箱
      better_score = 0 #n個の組み合わせの計算毎にリセットされる
      better_size = 0
      better_factor = ""
      better_method = ""
      for size in test_size:
        X_train, X_test, y_train, y_test = train_test_split(
              X, y, test_size=size, random_state=0)

        for i in model_list:
            model = i
            model.fit(X_train, y_train)
            #n個の組み合わせ毎に一番良い値とその時のテストサイズを実際に抽出
            if better_score == 0: #1番はじめ
                better_score = model.score(X_test, y_test)
                better_size = size
                better_factor = j              
                better_method = model.__class__.__name__
            elif model.score(X_test, y_test) > better_score:
                better_score = model.score(X_test, y_test)
                better_size = size
                better_factor = j    
                better_method = model.__class__.__name__
      print('better_method: {}'.format(better_method), 'better_size: ', better_size, 'better_score(acc): ', better_score, 'better_factor: {}{}'.format(len(better_factor), better_factor))
      #n個の組み合わせの全ての計算が終わったあとに、bestなものを選ぶ
      if best_score == 0:
          best_score = better_score
          best_size = better_size
          best_factor = better_factor
          best_method = better_method
      if better_score > best_score:
          best_score = better_score
          best_size = better_size
          best_factor = better_factor
          best_method = better_method    #n個の組み合わせ毎の計算が終わったら、最善の結果を出力する
  print('best_method: {}'.format(best_method),'best_size: ', best_size, 'best_score(acc): ', best_score, 'best_factor: {}'.format(best_factor))
  return best_method, best_size, best_score, best_factor
