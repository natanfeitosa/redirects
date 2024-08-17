import os
import re
import typing
from pathlib import Path


def _split_key_value(string):
    position = string.find("=")

    if position != -1:
        parte1 = string[:position]
        parte2 = string[position + 1:]
        return [parte1, parte2]

    return [string]


def _remove_quotes(string):
    match = re.match(r"^(['\"])(.*)\1$", string)
    if match:
        return match.group(2)

    return string


def load_env_files(paths: typing.Iterable[Path] = Path('.').glob('./**/.env')):
    for path in paths:
        if not path.exists():
            raise FileNotFoundError('.env is required')

        if not path.is_file():
            raise TypeError('.env is dir?')

        for line in path.read_text().split('\n'):
            if len(line) < 3 or line.startswith('#'):
                continue

            key, value = _split_key_value(line)
            if value:
                os.environ.update({key: _remove_quotes(value)})
