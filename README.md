# Uniao Rio Projections API
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg?style=for-the-badge)](http://commitizen.github.io/cz-cli/)

## Description

This is an API for storing COVID-19 projections in the state of Rio de Janeiro, Brazil, made by the União Rio Team

Based on https://github.com/cosmic-byte/flask-restplus-boilerplate.

## Installation

- Clone/Download this repo
- Make sure you have the latest version of `Python 3` and `PostgreSQL` installed.
- (Optional) Create a virtual environment on the root of the project
- Install the requirements with `pip install -r requirements .txt`
- Create a new database on `PostgreSQL`
- Copy the contents of `.env.example` onto a new `.env` file, replacing the contents between `{}` with the needed information
- Run the following commands to initialize the DB:
  - `python manage.py db init`
  - `python manage.py db migrate`
  - `python manage.py db upgrade`
- Run `python manage.py db run`

That's it!


## Contributing

Contributors are welcome! As this is a commitizen friendly repo, please follow this instructions when committing:

- Make sure you have `yarn` installed
- Run `yarn`
- Run `yarn global add commitizen`
- For every commit, run `git cz` instead of `git commit`

## License

This project is under the GNU General Public License v3.0

