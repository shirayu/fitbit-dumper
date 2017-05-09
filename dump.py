#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Dump fitbit data
"""

import argparse
import json
import sys
import codecs
import gzip
import fitbit


def get_data(cfg, date):
    '''
    Get data and print
    '''

    client = fitbit.Fitbit(cfg["CLIENT_ID"],
                           cfg["CLIENT_SECRET"],
                           access_token=cfg["ACCESS_TOKEN"],
                           refresh_token=cfg["REFRESH_TOKEN"])
    data = {}

    # https://python-fitbit.readthedocs.io/en/latest/
    # pylint: disable=maybe-no-member
    data['sleep'] = client.sleep(date=date)
#     data['bp'] = client.bp(date=date)  # blood pressure
    # pylint: enable=maybe-no-member

    # https://dev.fitbit.com/docs/activity/#get-activity-intraday-time-series
    keys = ["heart", "calories", "steps", "distance", "floors", "elevation"]
    for key in keys:
        data[key] = client.intraday_time_series(
            'activities/' + key,
            base_date=date,
            detail_level='15min')  # '1sec', '1min', or '15min'
    return data


def main():
    '''
    main
    '''

    oparser = argparse.ArgumentParser()
    oparser.add_argument("-d", "--date", dest="date", default=None, required=True)
    oparser.add_argument("-c", "--config", dest="config", default=None, required=True)
    oparser.add_argument("-o", "--output", dest="output", default="-")
    oparser.add_argument("-z", "--gzip", dest="gzip", default=False, action="store_true")
    opts = oparser.parse_args()

    cfg = None
    with open(opts.config) as fhdl:
        cfg = json.loads(fhdl.read())

    outf = None
    if opts.output == "-":
        outf = sys.stdout
    elif opts.gzip:
        outf1 = gzip.open(opts.output, mode='wb')
        outf = codecs.getwriter('utf_8')(outf1)
    else:
        outf = codecs.open(opts.output, "w", "utf8")

    data = get_data(cfg, opts.date)
    json.dump(data, outf, ensure_ascii=False)
    outf.write("\n")
    outf.close()

if __name__ == '__main__':
    main()
