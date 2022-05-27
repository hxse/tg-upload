#!/usr/bin/env python3
# coding: utf-8
from pathlib import Path
import time
import subprocess
import fire
import json

blacklist = [".srt"]
retryMax = 10
sleep = 8


def convert_json(data):
    # outData = data.encode().decode(
    #     # "unicode-escape"
    # )  # or string-escape https://stackoverflow.com/questions/2969044/python-string-escape-vs-unicode-escape
    outJson = json.loads(data)
    return outJson


def run_ffmpeg(url, path, proxy):
    command = f'telegram-upload -p {proxy} --to {url} "{path}"'
    commandArr = ["telegram-upload", "-p", proxy, "--to", url, f'"{path}"']

    pop = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    while pop.poll() == None:
        line = pop.stdout.readline()
        # print(line)
        message = b"Uploading"
        if line[:9].strip() == message:
            return [True, message]

        message = b"UnicodeEncodeError: 'gbk' codec can't encode character '\\xa0' in position 37: illegal multibyte sequence"
        if line.strip() == message:
            return [False, message]

        message = b"Task was destroyed but it is pending!"
        if line.strip() == message:
            return [False, message]

    print("输出结果")
    for line in pop.stdout:
        print(line)
    import pdb

    pdb.set_trace()


def loop_run_ffmepg(url, path, proxy, retry=0, sleep=sleep):
    assert retry <= retryMax, f"超过最大次数{retryMax}"
    [state, message] = run_ffmpeg(url, path, proxy)

    if not state:
        retry += 1
        print("上传错误", path, message)
        print("重试次数:", retry, "最大次数:", retryMax)
        print("sleep", sleep)
        time.sleep(sleep)
        return loop_run_ffmepg(url, path, proxy, retry, sleep=sleep)
    print("上传成功", retry, path)


def upload_file(
    url,
    path,
    proxy="http://127.0.0.1:7890",
    cache="already_upload.txt",
    blacklist=blacklist,
    sleep=sleep,
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

    loop_run_ffmepg(url, path, proxy, sleep=sleep)

    with open(cache, "a+", encoding="utf8") as f:
        f.write(f"{path}\n")
    return


def upload_dir(
    url,
    dir,
    proxy="http://127.0.0.1:7890",
    cache="already_upload.txt",
    blacklist=blacklist,
    sleep=sleep,
):
    if not Path(dir).is_dir():
        print("空目录:", dir)
        return
    for path in Path(dir).glob("*"):
        if path.is_file():
            isSkip = upload_file(
                url, path.as_posix(), proxy, cache, blacklist, sleep=sleep
            )
            if not isSkip:
                print("sleep", sleep)
                time.sleep(sleep)


if __name__ == "__main__":
    fire.Fire({"uf": upload_file, "ud": upload_dir})
