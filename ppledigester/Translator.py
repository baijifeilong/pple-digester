# Created by BaiJiFeiLong@gmail.com at 2020/5/14 15:01

import re
from collections import defaultdict
from pathlib import Path

from ppledigester import log_utils


class Translator(object):
    def __init__(self):
        self.logger = log_utils.get_logger("Translator")
        self.translation_dict = defaultdict(dict)
        self.pattern = re.compile(r"(?P<key>\w+)\.(?P<locale>\w+)=(?P<value>.+)")
        self.locale = "en_US"
        lines = Path("i18n.txt").read_text(encoding="utf8").splitlines()
        for index, line in enumerate(lines):
            match = self.pattern.match(line)
            assert match, f"Translation line format is wrong: {line}"
            key = match.group("key")
            locale = match.group("locale")
            value = match.group("value")
            self.logger.debug(f"[{index + 1:3}] {key}:{locale} => {value}")
            self.translation_dict[key][locale] = value

    def translate(self, key: str):
        assert key in self.translation_dict
        return self.translation_dict[key].get(self.locale, "en_US")
