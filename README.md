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
