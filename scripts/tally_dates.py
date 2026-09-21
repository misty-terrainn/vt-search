#!/usr/bin/env python

import os
import json
import argparse
from datetime import datetime

DEFAULT_ATTRIBUTE = "last_submission_date"
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dir", type=str, default=".", 
                    help="Directory to search for VT-Search JSON output files")
parser.add_argument("-a", "--attribute", type=str, default=DEFAULT_ATTRIBUTE, 
                    help="Date attribute to tally (defaults to {})".format(DEFAULT_ATTRIBUTE))
args = parser.parse_args()

jfiles = os.listdir(args.dir)
dates_list = []
for jf in jfiles:
    if jf.endswith(".json"):
        print(jf)
        with open(os.path.join(args.dir,jf), 'r') as f:
            j = json.load(f)
        values = [e.get("attributes",{}).get(args.attribute) for e in j]
        dates = list(set([datetime.fromtimestamp(int(t)).strftime("%Y-%m-%d") for t in values]))
        dates_list.extend(dates)

dates = sorted(list(set(dates_list)))
print("===============================================")
print("JSON results cover the following values for {}:".format(args.attribute))
for d in dates:
    print(d)
