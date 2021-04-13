# Python 檔案讀寫練習

## 前置作業
```
git clone https://github.com/tings0802/python-file-io.git
```

## 開啟與關閉檔案

### 開啟檔案

```python
file = open(filename, mode)
```

- `r`：讀取檔案，不能寫
- `w`：從頭開始寫入檔案，不能讀，若檔案不存在則創建檔案
- `a`：從尾開始寫入檔案，不能讀，若檔案不存在則創建檔案
- `r+`：讀取檔案，也可從頭寫入
- `w+`：從頭寫入，可讀，若檔案不存在則創建檔案
- `a+`：從尾寫入，可讀，若檔案不存在則創建檔案


### 關閉檔案

使用完檔案物件之後一定要記得關閉檔案

```python
file.close()
```

### 例外處理

若讀寫檔案時發生錯誤，程式會中斷，檔案未正常可能引起非預期的結果，因此檔案讀寫常搭配 `try`-`except` 做例外處理

```python
try:
    file = open(filename, mode)
    # do something on the file
except IOError:
    # do error handling
finally:
    file.close()
```

Python 提供另一種例外處理的寫法，當 `with` 區塊內的程式執行完畢或是執行到一半例外發生時，會自動幫我們關閉檔案，只需要一行程式碼，因此推薦使用這種寫法來進行檔案讀寫

```python
with open(filename, mode) as file:
    # do something on the file
```

## 讀取檔案

從檔案讀入內容，回傳字串

```python
string = file.read(size)
```
`size`: 讀取字元數，若未指定或給負數則讀取整個檔案


讀取整行，回傳字串 (包含換行符 `'\n'`)

```python
string = file.readline()
```

讀取所有行，回傳 list，元素是每一行內容的字串 (包含換行符 `'\n'`)

```python
list_of_string = file.readlines()
```

## 寫入檔案

把字串寫入檔案，回傳寫入的字串長度

```python
length = file.write(string)
```

向文件寫入字串列表，如果需要換行則需要自己加換行符 `'\n'`

```python
file.writelines(list_of_string)
```

## 實戰演練

### 介紹

[PDB file (Protein Data Bank)](https://en.wikipedia.org/wiki/Protein_Data_Bank_(file_format)) 是一種用來描述與記錄分子三維結構的純文字檔案格式，可以從 [RCSB 蛋白質資料庫](https://www.rcsb.org/) 下載

[Topology file](https://manual.gromacs.org/documentation/current/reference-manual/topologies/topology-file-formats.html) 則是定義胺基酸分子的組成、原子位置、鍵結方式及其他物理性質的純文字檔案格式

這個範例的目標是要寫一支 Python 程式，從 PDB 檔裡面讀取蛋白質分子的三維結構，然後從 Topology 檔讀取胺基酸的資訊，用來計算該分子的質心、分子量及慣性張量 (tensor)

你的工作是實作兩個函式 `readPDB()` 和 `readTOP()`，分別將 PDB file 和 Topology file 的內容讀入，並依照指定的格式回傳

### 取得資料

首先進到 `cmass` 資料夾，會看到以下檔案：`getdata.sh` 式用來下載資料的腳本，`cmass.py` 是主要執行的程式，`modules` 內是用來計算和輸出結果的模組，`solution.py` 是實作檔案讀寫的檔案，請將你的程式碼寫在這裡

```diff
  cmass
  ├── cmass.py
  ├── getdata.sh
  ├── modules
  │   ├── calculate.py
  │   ├── inspect.py
  │   ├── read.py
  │   └── test.py
  └── solution.py   # 寫這個檔案
```

然後執行 `getdata.sh` 下載所需的 PDB 檔和 Topology 檔

```shell
./getdata.sh
```

如果成功下載，會看到資料夾內多了這些檔案和資料夾

```diff
  cmass/
  ├── cmass.py
+ ├── data.tar.gz
  ├── getdata.sh
  ├── modules
  │   ├── calculate.py
  │   ├── inspect.py
  │   ├── read.py
  │   └── test.py
+ ├── pdb
+ │   └── receptor5_Pemirolast.pdb
  ├── solution.py
+ └── topology
+     ├── top_all22_prot.rtf
+     ├── top_all35_ethers.rtf
+     ├── top_all36_carb.rtf
+     ├── top_all36_cgenff.rtf
+     ├── top_all36_lipid.rtf
+     ├── top_all36_na.rtf
+     └── top_all36_prot.rtf
```

如果沒辦法順利下載，請從 [這裡](https://drive.google.com/u/1/uc?id=1b39Lp4PA0DT5wbvicuN1S7Pp7kU9P66y&export=download) 下載 `data.tar.gz` 到 `cmass` 資料夾內，然後輸入以下指令解壓縮：

```shell
tar zxvf data.tar.gz
```

接著就可以開始打開文字編輯器開始實作了

```shell
subl solution.py
# or
vim solution.py
```

### 撰寫程式

在 `solution.py` 裡面有三個函式，你只需要實作 `readPDB()` 和 `readTOP()` 即可，三個函式的都只有一個參數，且皆為讀檔路徑，下面說明實作細節

#### `readPDB()` 實作細節

函式原型如下，接受一個字串作為參數，回傳一個二維串列

```python
def readPDB(pfile):
    ''' read a pdb file and return coordinates of atoms (2D list) '''
    atomicCoor = []     # [[name, x, y, z]]

    # your code should be here
    
    return atomicCoor
```

觀察下載下來的 `pdb/receptor5_Pemirolast.pdb`，參考 [PDB file format](https://www.cgl.ucsf.edu/chimera/docs/UsersGuide/tutorials/pdbintro.html)，將所有的 `ATOM` 讀入，依照以下格式，將每個原子的名稱和座標儲存在一個二維串列中作為函式的回傳值

```python
[
    [element_symbol, x_coordinate, y_coordinate, z coordinate],
    [element_symbol, x_coordinate, y_coordinate, z coordinate],
    [element_symbol, x_coordinate, y_coordinate, z coordinate],
#     ...
    [element_symbol, x_coordinate, y_coordinate, z coordinate],
]
```

#### `readTOP()` 實作細節

函式原型如下，接受一個字串作為參數，回傳一個字典

```python
def readTOP(tfile):
    ''' read a topology file and return atomic masses (dict) '''
    atomicMass = {}     # {name: mass}
 
    # your code should be here
        
    return atomicMass
```
topology 檔裡面我們只需要各個原子的 `MASS`，觀察 `topology` 資料夾中的任一個檔案，將原子的名稱和原子量讀入，依照以下格式儲存在一個字典中並回傳

```python
{
    atom_name: atomic_mass,
    atom_name: atomic_mass,
    atom_name: atomic_mass,
#     ...
    atom_name: atomic_mass,
}
```

### 執行程式

寫好 `solution.py` 後，執行 `cmass.py` 來確認程式是否正常執行

```shell
./cmass.py
```

若想確認答案是否正確，再次執行 `cmass.py` 並加上 `--check` 選項

```shell
./cmass.py --check
```

查看程式的使用說明，請加上 `--help` 選項

```shell
./cmass.py --help
```

如果結果正確，會輸出以下結果

```
[My answer]
center of mass: [0.0643, -0.0255, -0.1699]
molecular mass: 16473.4484
moment of inertia:
    0.2061    2.6148   -0.2856
    2.6148   33.5764    0.0222
   -0.2856    0.0222   33.7776

[Your answer]
center of mass: [0.0643, -0.0255, -0.1699]
molecular mass: 16473.4484
moment of inertia:
    0.2061    2.6148   -0.2856
    2.6148   33.5764    0.0222
   -0.2856    0.0222   33.7776

Congratulations! Your answer is correct!
```
