# twitter-banner-switcher
[![PyPI Version](https://img.shields.io/pypi/v/twitter-banner-switcher.svg)][tbs pypi]
[![Python Versions](https://img.shields.io/pypi/pyversions/twitter-banner-switcher.svg)][tbs pypi]
[![License](https://img.shields.io/github/license/Pythonity/twitter-banner-switcher.svg)][license]

Python (3) script that sets your Twitter profile banner to a random
image from a specified folder or a list of paths.

## Installation
With `PyPI` (recommended):
```shell
$ pip3 install twitter-banner-switcher
```

With `git clone`:
```shell
$ git clone https://github.com/Pythonity/twitter-banner-switcher
$ pip3 install -r twitter-banner-switcher/requirements.txt
$ cd twitter-banner-switcher/bin
```

## Usage
```
$ twitter-banner-switcher -h
Usage: twitter-banner-switcher [OPTIONS]

  Set Twitter profile banner to a random image from a specified folder or a
  list of paths

Options:
  -c, --config-file FILENAME  Path to YAML config file (default: ~/.twitter-
                              banner-switcher.yml).
  -h, --help                  Show this message and exit.

```

## Examples
Not much to show here - you can provide path to config file:
```shell
$ twitter-banner-switcher -c twitter-banner-switcher.yaml
```
or save it at `~/.twitter-banner-switcher.yaml` and just run the damn
thing:
```shell
$ twitter-banner-switcher
```

### Example config file
```yaml
$ cat twitter-banner-switcher.yaml
consumer_key: "Twitter consumer key"
consumer_secret: "Twitter consumer secret"
access_token: "Twitter access token"
access_token_secret: "Twitter access token secret"

banner_images:
    - "/home/bender/Photos/Awesome Twitter Banners/"
    - "/home/bender/Downloaded/planet_express.png"
```

Note: `banner_images` can be a path or a list of paths (to directories
containing images or directly to image files). Recognized formats are `gif`,
`jpg`, `jpeg` and `png`.

## Contributions
Package source code is available at [GitHub][tbs github].

Feel free to use, ask, fork, star, report bugs, fix them, suggest 
enhancements and point out any mistakes.

## Authors
Developed and maintained by [Pythonity][pythonity].

Written by [Paweł Adamczak][pawelad].

[tbs github]: https://github.com/Pythonity/twitter-banner-switcher
[tbs pypi]: https://pypi.python.org/pypi/twitter-banner-switcher
[license]: https://github.com/Pythonity/twitter-banner-switcher/blob/master/LICENSE
[pythonity]: http://pythonity.com/
[pawelad]: https://github.com/pawelad
