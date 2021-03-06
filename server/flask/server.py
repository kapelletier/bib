#!/usr/bin/env python
# vim: syntax=python tabstop=4 expandtab

from flask import Flask, jsonify
from modules.get_dir_list import path_to_dict

app = Flask(__name__)

@app.route('/flask/treeRoot')
def send_root_dirs():
    nodes = path_to_dict('/mnt/data', 1)
    return jsonify(nodes = [nodes])
