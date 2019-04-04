# Changelog
All notable changes to this project will be documented in this file.

## [UNRELEASED] -
### Added
- Add button to delete index from web page.
- Add ability to index movies from web page.
- Display warning message on web start page if no movie index is found.
- Add min_size_to_index configuration option to web settings page.
- Add ability to edit poster location from cli.
- Add function to download/cache all poster images to local directory.
### Changed
- All endpoints now have checks if user login is required.
- Deleting a user from web settings page now asks for confirmation.
- Log level configuration in the settings page now has a dropdown list instead of textfield.
- Web interface now retrieving cached posters if available.


### Fixed 
- Login page using external dependencies instead of local ones.

## [2.4.1] - 2018-10-28
### Fixed
- Removed debug printouts.

## [2.4.0] - 2018-10-28
### Added
- Backend user database implemented.
- New config option, 'require_login'.
- Functional web login page.
- Database migration.
- Get movie plot and display on web page.
- User creation and deletion from web settings page.
- Added web config options to settings page.

### Changed
- Removed external links to dependencies in the web interface.
- Updated look of settings page in the web interface.
- Settings page now has a dropdown list for external API selection.


## [2.3.0] - 2018-10-21
### Added
- Command to edit index file from command line.
- Command to open configuration file in system default editor.
- Command to force indexation, ignoring already indexed movies.
- Web interface port setting in configuration file.
- Export dropdown list in web interface.
- Configuration option for minimum size for file to be allowed indexing.
- Long description in setup.py, reads from README.md

### Changed
- Second stage moving .json file to sql database. Migration now done.
- Web navbar title changed.
- Web interface shows default poster if none is found.

### Fixed
- Configuration file not being created if directory existed.

## [2.2.1] - 2018-08-18
### Fixed
- Requirements missing for the web interface in setup.py

## [2.2.0] - 2018-08-18
### Added
- Web interface

### Changed
- First stage moving .json index file to sql database.

## [2.1.0] - 2018-08-14
First release of ``movielst``
### Added
- File info to index file. Extension, filename and location.
- Internal logging of errors, debug etc.
- Ability to export index file to excel or csv.
- Option to index via TMDb as well.
- Configuration file, located inside ~/.movielst

### Changed
- Replaced `docopt` with `argparse` for argument handling.
- Moved .json file from indexed directory to centralized configuration folder. ~/.movielst
