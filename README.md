
# Fitbit dumper

[![CircleCI](https://circleci.com/gh/shirayu/fitbit-dumper.svg?style=svg)](https://circleci.com/gh/shirayu/fitbit-dumper)
[![Apache License](http://img.shields.io/badge/license-APACHE2-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0)

## Install

```sh
sudo pip3 install fitbit
```

## Initialization

Get access tokens by using ``python-fitbit/gather_keys_oauth2.py``.
([guide in Japanese](http://qiita.com/fujit33/items/2af7c4afdb4e07601def))

```sh
cp config.template.json config.json
chmod 600 config.json

# Set tokens
vi config.json
```

The configuration file will be overwrite, when the access token is expired.
So, the program should be write permission to the file.

## Sample

```sh
python3 ./dump.py -c ./config.json -o out.json.gz -d 2017-05-09 --gzip
```

## License
- [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
