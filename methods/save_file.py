import os


def save_file(df, path):

    if os.path.isfile(path):
        open(path, 'w').close()

    with open(path, 'a') as f:
        df = df.round()
        f.write(df.to_string(header=True, index=False))


