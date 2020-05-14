# Created by BaiJiFeiLong@gmail.com at 2020/5/14 ‏‎16:34

import logging

import colorlog


def get_logger(name: str):
    logger = logging.getLogger(name)
    if logger.handlers:
        return logger
    handler = logging.StreamHandler()
    handler.setFormatter(colorlog.ColoredFormatter(
        fmt="%(black)s%(asctime)s.%(msecs)03d %(log_color)s%(levelname)8s%(reset)s %(black)s[%(name)-10s]\t %(message)s",
        datefmt='%Y-%m-%d %H:%M:%S'
    ))
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    return logger
