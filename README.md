# movielst [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

movielst is a fork of moviemon, a Python application that displays information about all your movies in the command line.
This fork is intended to update the project to latest python version, fix existing issues from the orignal project and add new features.

![](https://i.imgur.com/Lb8qCXa.gif)

## Installation

### Install from source

* Install with pip `pip install git+git://github.com/Mozzo1000/movielst.git`


### Dependencies

* [guessit](https://github.com/guessit-io/guessit)
* [terminaltables](https://github.com/Robpol86/terminaltables)
* [tqdm](https://github.com/tqdm/tqdm)
* [colorama](https://github.com/tartley/colorama)


### Usage:
```sh
  movielst PATH
  movielst [-i | -t | -g | -a | -c | -d | -y | -r | -I | -T ]
  movielst -h | --help
  movielst --version
```

### Options:
```sh
  -h, --help            Show this screen.
  -v, --version             Show version.
  PATH                  Path to movies dir. to index/reindex all movies.
  -i, --imdb            Sort acc. to IMDB rating.(dec)
  -t, --tomato          Sort acc. to Tomato Rotten rating.(dec)
  -g, --genre           Show movie name with its genre.
  -a, --awards          Show movie name with awards received.
  -c, --cast            Show movie name with its cast.
  -d, --director        Show movie name with its director(s).
  -y, --year            Show movie name with its release date.
  -r, --runtime         Show movie name with its runtime.
  -I, --imdb-rev        Sort acc. to IMDB rating.(inc)
  -T, --tomato-rev      Sort acc. to Tomato Rotten rating.(inc)
```

### Credits
[iCHAIT](https://github.com/iCHAIT) - Original developer

### Contribute

Found a bug or want to suggest a new feature? Report it by opening an issue. Feel free to send a pull request for any improvements or feature requests ;)


### License
`movielst` is released under the [MIT License](http://www.opensource.org/licenses/MIT).