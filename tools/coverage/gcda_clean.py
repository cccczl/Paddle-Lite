#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
usage: gcda_clean.py pull_id
"""

import os
import sys

from github import Github

token = os.getenv('GITHUB_API_TOKEN')

def get_pull(pull_id):
    """

    :param pull_id:
    :return: pull
    """

    github = Github(token, timeout=60)
    repo = github.get_repo('PaddlePaddle/Paddle-Lite')
    return repo.get_pull(pull_id)


def get_files(pull_id):
    """

    :param args:
    """

    pull = get_pull(pull_id)

    for file in pull.get_files():
        yield file.filename


def clean(pull_id):
    """

    :param pull_id:
    :return:
    """

    changed = [f'/Paddle-Lite/build/{file}.gcda' for file in get_files(pull_id)]

    for parent, dirs, files in os.walk('/Paddle-Lite/build/'):
        for gcda in files:
            if gcda.endswith('.gcda'):
                trimmed = parent

                # convert paddle/fluid/imperative/CMakeFiles/layer.dir/layer.cc.gcda
                # to paddle/fluid/imperative/layer.cc.gcda

                if trimmed.endswith('.dir'):
                    trimmed = os.path.dirname(trimmed)

                if trimmed.endswith('CMakeFiles'):
                    trimmed = os.path.dirname(trimmed)

                # remove no changed gcda

                if os.path.join(trimmed, gcda) not in changed:
                    gcda = os.path.join(parent, gcda)
                    os.remove(gcda)


if __name__ == '__main__':
    pull_id = sys.argv[1]
    pull_id = int(pull_id)

    clean(pull_id)
