#!/usr/bin/env python3
# coding: utf-8
from pathlib import Path
import subprocess
import fire


def upload_file(
    url,
    path,
    proxy="http://127.0.0.1:7890",
    cache="already_upload.txt",
):
    if not Path(path).is_file():
        print("本地文件不存在", path)
        return
    if Path(cache).is_file():
        with open(cache, "r", encoding="utf8") as f:
            data = f.readlines()
        if path + "\n" in data:
            print("已存在,跳过:", path)
            return
    command = f'telegram-upload -p {proxy} --to {url} "{path}"'
    subprocess.run(command)
    with open(cache, "a+", encoding="utf8") as f:
        f.write(f"{path}\n")


def upload_dir(url, dir, proxy="http://127.0.0.1:7890", cache="already_upload.txt"):
    if not Path(dir).is_dir():
        print("空目录:", dir)
        return
    for path in Path(dir).glob("*"):
        if path.is_file():
            upload_file(url, path.as_posix(), proxy, cache)


if __name__ == "__main__":
    fire.Fire({"uf": upload_file, "ud": upload_dir})
