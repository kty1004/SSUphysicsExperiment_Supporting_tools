# SSUphysics experiment supporting tools
숭실대학교 물리학과 물리계측실험 수업에서 유용하게 사용할 수 있는 python 페키지입니다.

> 향후 다른 실험 수업에서도 사용할 수 있도록 확장할 예정입니다.

## How to install
```zsh
pip install SSUphysicsTools
```

## Example
다음의 repository를 참고하여 사용할 수 있습니다.
[SSUphysicsTools-example](https://github.com/kty1004/SSUphysicsTools_examples)

## How to use
### Setting up
실험 데이터는 data 폴더에 저장되어 있어야 합니다. 이 때 data 폴더는 다음과 같은 구조를 가지고 있어야 합니다.
```
data
├── experiment 1
│   ├── 1.csv
│   ├── 2.csv
├── experiment 2
│   ├── 1.csv
│   ├── 2.csv
└── ...
```
만약 data 폴더가 준비되지 않았더면, 자동으로 data 폴더를 생성하고 `DataDirectoryEmptyError`를 발생시켜 data 폴더에 실험 데이터를 넣도록 알려줍니다.

### getting data
`data` 폴더에 저장된 실험 데이터를 가져오는 방법은 다음과 같습니다.
```python
from SSUphysicsTools import getting_data as gd
from padas import pd
data_paths=gd.get_all_csv_paths_in_data(custom_dir_name=True, flatten=False)()
data_set:list[pd.Dataframe]=[gd.read_csv_Tektronix(path) for path in data_paths]
```
위 코드는 다음과 같은 순서로 작동합니다.
0. SSUphysicsTools 패키지 중 getting_data module을 import 합니다.
1. `get_all_csv_paths_in_data`를 이용하여 실험 데이터의 경로를 가져올 수 있습니다.
2. `read_csv_Tektronix`를 이용하여 실험 데이터를 가져올 수 있습니다. 이 때 list comprehension을 이용하여 가독성 높임과 동시에 여러 실험 데이터를 가져올 수 있습니다.
>[!warning] `data_set`은 `numpy.ndarray`로 두지 마십시오. `numpy.ndarray`는 `pandas.DataFrame`의 내용을 전부 풀어서 저장하기 때문에 데이터를 다루기 어려워집니다.
```
|column1|column2|column3|
|-------|-------|-------|
|data1  |data2  |data3  |
|data4  |data5  |data6  |
...

-> numpy.ndarray를 사용하면 다음과 같이 저장됩니다.
array([data1, data2, data3, data4, data5, data6, ...])
```

### processing data
- Regression
    - cosine_regression
- Delate_offset
### analyzing data
- Phase_shift
    - find_min_x_vector
    - find_ym_y0
    - __call__ : get_phase_shift
- get_error_rate
### plot
- DataPlots
    - data_plots
    - Lissajous_plots
- plot_table