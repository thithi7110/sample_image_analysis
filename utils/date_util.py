from datetime import datetime, timezone, timedelta


def get_jst_unix_timestamp():
    JST = timezone(timedelta(hours=+9), 'JST')

    # [サンプル]UNIX秒(UTC)を生成
    epoch = int(datetime.now(JST).strftime('%s%f')) // 1000000
    return epoch