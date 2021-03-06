import requests

def get(uri_):
    if "&" in uri_:
        try:
            uri_ = uri_[:uri_.find('&')]
        except Exception as e:
            return e
    try:
        r = requests.get(uri_)
        if f"https://www.youtube.com/watch?v=" in uri_:
            uri_ = uri_.replace(f"https://www.youtube.com/watch?v=", '')
        elif f"http://www.youtube.com/watch?v=" in uri_:
            uri_ = uri_.replace(f"http://www.youtube.com/watch?v=", '')
        elif f"http://youtube.com/watch?v=" in uri_:
            uri_ = uri_.replace(f"http://youtube.com/watch?v=", '')
        elif f"https://youtube.com/watch?v=" in uri_:
            uri_ = uri_.replace(f"https://youtube.com/watch?v=", '')
        elif f"https://youtu.be/" in uri_:
            uri_ = uri_.replace("https://youtu.be/", '')
            if f"?" in uri_:
                uri_ = uri_[:uri_.find("?")]
        elif f"http://youtu.be/" in uri_:
            uri_ = uri_.replace("http://youtu.be/", '')
            if f"?" in uri_:
                uri_ = uri_[:uri_.find("?")]
        elif f"https://www.youtu.be/" in uri_:
            uri_ = uri_.replace("https://www.youtu.be/", '')
            if f'?' in uri_:
                uri_ = uri_[:uri_.find('?')]
        elif f"http://www.youtu.be/" in uri_:
            uri_ = uri_.replace("http://www.youtu.be/", '')
            if f'?' in uri_:
                uri_ = uri_[:uri_.find('?')]
    except Exception as e:
        return e
    try:
        uri_ = "https://i.ytimg.com/vi/{}/hqdefault.jpg".format(uri_)
        return uri_
    except Exception as e:
        return e
