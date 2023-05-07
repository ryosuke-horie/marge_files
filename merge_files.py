import os


def merge_files(path, file_names=None):
    """
    ローカルのパスを受け取り、指定されたファイルの内容を1つにまとめたファイルを作成する関数。
    """
    file_paths = []
    if file_names is None:
        # ディレクトリ内のファイルがない場合は、終了
        if not os.listdir(path):
            return file_paths

        for root, dirs, files in os.walk(path):
            if '.git' in dirs:
                dirs.remove('.git')
            for file in files:
                file_path = os.path.join(root, file)
                if not file_path.startswith(os.path.join(path, '.git')):
                    file_paths.append(file_path)
    else:
        file_paths = [os.path.join(path, name) for name in file_names]

    if file_paths:
        with open('merged_file.txt', 'a', encoding='cp932', errors='replace') as outfile:
            for i, file_path in enumerate(file_paths):
                with open(file_path, encoding='cp932', errors='replace') as infile:
                    rel_path = os.path.relpath(file_path, path)
                    if i != 0:
                        outfile.write('\n\n')
                    outfile.write(f'[{rel_path}]:\n')
                    outfile.write(infile.read())

        for path in file_paths:
            print(f"{path}: [{os.path.join(os.getcwd(), 'merged_file.txt')}]")
    
    return file_paths


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='ファイルをまとめる')
    parser.add_argument('path', help='ファイルを検索するディレクトリ')
    parser.add_argument('-f', '--file_names', nargs='*', help='まとめるファイルの名前')
    args = parser.parse_args()

    file_paths = merge_files(args.path, args.file_names)
    for path in file_paths:
        print(f"{path}: [{os.path.join(os.getcwd(), 'merged_file.txt')}]")
