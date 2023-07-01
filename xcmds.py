
# encoding: utf-8

import base64
import hashlib
import urllib
import json

def md5(str):
    m = hashlib.md5()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

def sha1(str):
    m = hashlib.sha1()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

def sha256(str):
    m = hashlib.sha256()
    m.update(str.encode('utf-8'))
    return m.hexdigest()

def url_encode(str):
    return urllib.quote(str.encode('utf-8'))

def url_decode(str):
    return urllib.unquote(str.encode('utf-8')).decode('utf-8')

def json_beautify(str):
    return json.dumps(json.loads(str), indent=4, ensure_ascii=False)

def base64_encode(str):
    return base64.b64encode(str.encode('utf-8'))

def base64_decode(str):
    return base64.b64decode(str.encode('utf-8')).decode('utf-8')

XCMDS = {
    "XMD5": md5,
    "XSHA1": sha1,
    "XSHA256": sha256,
    "XURLENCODE": url_encode,
    "XURLDECODE": url_decode,
    "XJSONBF": json_beautify,
    "XBASE64ENCODE": base64_encode,
    "XBASE64DECODE": base64_decode,
}