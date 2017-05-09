
# Fitbit dumper

## Install

```sh
sudo pip2 install fitbit
sudo pip3 install fitbit
```

## Initialization

Get access tokens by using ``python-fitbit/gather_keys_oauth2.py``.
([guide in Japanese](http://qiita.com/fujit33/items/2af7c4afdb4e07601def))

```sh
cp config.template.json config.json

# Set tokens
vi config.json
```

## Sample

```sh
python3 ./dump.py -c ./config.json -o out.json.gz -d 2017-05-09 --gzip
```

## License
- [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)
