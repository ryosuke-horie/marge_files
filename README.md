## merge_files関数

ローカルのパスを受け取り、指定されたファイルの内容を1つにまとめたファイルを作成する関数。

```python
def merge_files(path, file_names=None):
    ...
```

### 引数

- `path`：ファイルを検索するディレクトリのパス
- `file_names`（オプション）：まとめるファイルの名前を指定するリスト

### 戻り値

- `file_paths`：指定されたパスから取得されたファイルのパスのリスト

### 例

```python
merge_files('/path/to/files')
merge_files('/path/to/files', ['file1.txt', 'file2.txt'])
```

### 注意

- `merged_file.txt`がすでに存在する場合は、ファイルの最後に追記されます。
- `merged_file.txt`のエンコーディングは、現在設定されているcp932に固定されています。このエンコーディングが正しくない場合、ファイルの出力が壊れる可能性があります。