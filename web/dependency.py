from movielst import config
import requests
import os

dep_folder = config.CACHE_DIR / 'deps'
dependencies = ['https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
                'https://code.jquery.com/jquery-3.3.1.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js',
                'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js',
                'https://cdnjs.cloudflare.com/ajax/libs/blazy/1.8.2/blazy.min.js']


def check_for_dep():
    try:
        dep_folder.mkdir(parents=True)
    except FileExistsError:
        pass

    for url in dependencies:
        local_path = dep_folder / url.rsplit('/', 1)[-1]
        if not local_path.exists():
            download_dep(url)


def download_dep(url):
    local_filename = url.split('/')[-1]
    r = requests.get(url, stream=True)
    with (dep_folder / local_filename).open('wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local_filename
