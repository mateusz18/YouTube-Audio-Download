from pytube import YouTube


def download(urls, path):
    while True:
        if urls.empty():
            continue
        url = urls.get()
        yt_video = YouTube(url)
        stream = yt_video.streams.get_by_itag(251)  # you can change the itag in order to change the files quality and/or format
        stream.download(output_path=path)
