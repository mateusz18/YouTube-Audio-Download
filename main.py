from multiprocessing import Process, Queue

import downloader
import youtube_search
import os

t = Queue()
u = Queue()
if __name__ == '__main__':

    path = input('Specify the target file path: ')

    # songs are being downloaded in the background so you can keep on adding more to the list
    get_urls = Process(target=youtube_search.get_url, args=(t, u))
    get_files = Process(target=downloader.download, args=(u, path))
    get_urls.start()
    get_files.start()

    while True:
        title = input('Enter the name of the song (type: "!x" to leave): ')
        if title == '!x':
            get_urls.terminate()
            get_files.terminate()
            exit()
        t.put(title)
        os.system('clear')
