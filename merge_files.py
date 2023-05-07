import os


def merge_files(path, file_names=None):
    """
    ローカルのパスを受け取り、指定されたファイルの内容を1つにまとめたファイルを作成する関数。
    """
    if file_names is None:
        # file_namesが指定されていない場合は、ディレクトリ内のすべてのファイルを検索する
        file_paths = []
        for root, dirs, files in os.walk(path):
            if '.git' in dirs:
                dirs.remove('.git')
            for file in files:
                file_path = os.path.join(root, file)
                if not file_path.startswith(os.path.join(path, '.git')):
                    file_paths.append(file_path)
    else:
        # file_namesが指定された場合は、指定されたファイルのみを検索する
        file_paths = [os.path.join(path, name) for name in file_names]

    with open('merged_file.txt', 'w', encoding='cp932', errors='replace') as outfile:
        for file_path in file_paths:
            with open(file_path, encoding='cp932', errors='replace') as infile:
                outfile.write(infile.read())

    return file_paths


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='ファイルをまとめる')
    parser.add_argument('path', help='ファイルを検索するディレクトリ')
    parser.add_argument('-f', '--file_names', nargs='*', help='まとめるファイルの名前')
    args = parser.parse_args()

    file_paths = merge_files(args.path, args.file_names)
    for path in file_paths:
        print(path)
    print('merged_file.txt')
