#!/usr/bin/env python3
from setuptools import setup

setup(
    name="binance-futures",
    version="1.1.0",
    packages=['binance_f', 'binance_f.impl', 'binance_f.impl.utils', 'binance_f.exception', 'binance_f.model', 'binance_f.base', 'binance_f.constant'],
    install_requires=['requests', 'websocket-client', 'urllib3']
)

