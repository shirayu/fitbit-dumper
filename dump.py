#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dump fitbit data
"""

import argparse
import codecs
import gzip
import json
import sys
import time

import fitbit


def get_data(cfgname, date, sleep):
    """
    Get data and print
    """

    def update_token(token):
        """
        Write token
        """
        token["client_id"] = cfg["client_id"]
        token["client_secret"] = cfg["client_secret"]
        with open(cfgname, "w") as fhdl:
            json.dump(token, fhdl, ensure_ascii=False, sort_keys=True, indent=4)

    cfg = None
    with open(cfgname) as fhdl:
        cfg = json.loads(fhdl.read())

    client = fitbit.Fitbit(
        cfg["client_id"],
        cfg["client_secret"],
        access_token=cfg["access_token"],
        refresh_token=cfg["refresh_token"],
        expires_at=cfg["expires_at"],
        refresh_cb=update_token,
    )
    data = {}

    # https://python-fitbit.readthedocs.io/en/latest/
    # pylint: disable=maybe-no-member
    data["sleep"] = client.sleep(date=date)
    #     data['bp'] = client.bp(date=date)  # blood pressure
    # pylint: enable=maybe-no-member

    # https://dev.fitbit.com/docs/activity/#get-activity-intraday-time-series
    keys = ["heart", "calories", "steps", "distance", "floors", "elevation"]
    for key in keys:
        time.sleep(sleep)
        data[key] = client.intraday_time_series(
            "activities/" + key, base_date=date, detail_level="15min"
        )  # '1sec', '1min', or '15min'
    return data


def main():
    """
    main
    """

    oparser = argparse.ArgumentParser()
    oparser.add_argument("-d", "--date", dest="date", default=None, required=True)
    oparser.add_argument("-c", "--config", dest="config", default=None, required=True)
    oparser.add_argument("-o", "--output", dest="output", default="-")
    oparser.add_argument("-z", "--gzip", dest="gzip", default=False, action="store_true")
    oparser.add_argument("-s", "--sleep", dest="sleep", default=1.0, type=float)
    opts = oparser.parse_args()

    outf = None
    if opts.output == "-":
        outf = sys.stdout
    elif opts.gzip:
        outf1 = gzip.open(opts.output, mode="wb")
        outf = codecs.getwriter("utf_8")(outf1)
    else:
        outf = codecs.open(opts.output, "w", "utf8")

    data = get_data(opts.config, opts.date, opts.sleep)
    json.dump(data, outf, ensure_ascii=False)
    outf.write("\n")
    outf.close()


if __name__ == "__main__":
    main()
