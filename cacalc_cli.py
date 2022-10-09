#!/usr/bin/env python3

import argparse
import requests
import json

# Deal with arguements
arg_parser = argparse.ArgumentParser(
    description='This script calculates cacao percentages using existing API.')
arg_parser.add_argument(
    "-b", "--cacao_butter", help="Amount of cacao butter",
    type=float, required=False, default=0)
arg_parser.add_argument(
    "-c", "--cacao", help="Amount of cacao (nibs)",
    type=float, required=False, default=0)
arg_parser.add_argument(
    "-s", "--sugar", help="Amount of sugar",
    type=float, required=False, default=0)
arg_parser.add_argument(
    "-m", "--milk_powder", help="Amount of milk powder",
    type=float, required=False, default=0)
arg_parser.add_argument(
    "-0", "--other", help="Amount of other ingredients",
    type=float, required=False, default=0)
args = arg_parser.parse_args()


URL = 'https://tjeeclmrh0.execute-api.us-west-2.amazonaws.com/'

body = vars(args)

response = requests.post(URL, json=body)

print(response.json())