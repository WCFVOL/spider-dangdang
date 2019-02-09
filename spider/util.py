def url_is_legal(url):
    if url == "javascript:void(0);":
        return False
    if url == "":
        return False
    return True
