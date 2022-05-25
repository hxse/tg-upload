#!/usr/bin/env python3
# coding: utf-8
from pathlib import Path
import time
import subprocess
import fire

blacklist = [".srt"]


def upload_file(
    url,
    path,
    proxy="http://127.0.0.1:7890",
    cache="already_upload.txt",
    blacklist=blacklist,
):
    if not Path(path).is_file():
        print("本地文件不存在", path)
        return True
    if Path(path).suffix in blacklist:
        print("黑名单,跳过", path)
        return True
    if Path(cache).is_file():
        with open(cache, "r", encoding="utf8") as f:
            data = f.readlines()
        if path + "\n" in data:
            print("已存在,跳过:", path)
            return True
    command = f'telegram-upload -p {proxy} --to {url} "{path}"'
    subprocess.run(command)
    with open(cache, "a+", encoding="utf8") as f:
        f.write(f"{path}\n")
    return


def upload_dir(
    url,
    dir,
    proxy="http://127.0.0.1:7890",
    cache="already_upload.txt",
    blacklist=blacklist,
    sleep=2,
):
    if not Path(dir).is_dir():
        print("空目录:", dir)
        return
    for path in Path(dir).glob("*"):
        if path.is_file():
            isSkip = upload_file(url, path.as_posix(), proxy, cache, blacklist)
            if not isSkip:
                print("sleep", sleep)
                time.sleep(sleep)


if __name__ == "__main__":
    fire.Fire({"uf": upload_file, "ud": upload_dir})
