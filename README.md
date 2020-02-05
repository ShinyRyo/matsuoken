# matsuoken
GCI2019-winterデータサイエンス基礎講座を通じて作った自作モジュール
# homework5
## ベストなモデルを選ぶ
Brute-force.py<br>
### ver.1
trainとtest（それぞれデータフレーム）を入れればベストモデルを返す
<br>=>モデルも指定したい
#### ver.1.1
trainとtest(dataframe), model_list(list)を入れればベストモデルを返す<br>
exam: model_list = [RandomForestRegressor(random_state=42),LinearRegression()]
<br>=>テストサイズも指定したい
#### ver.1.2
train,test(dataframe),model_list(list),test_size(list)を引数として、ベストモデルを返す<br>
exam: test_size = [0.5, 0.3, 0.25, 0.2, 0.1]
<br>=> ハイパーパラメータを組み込みたい
