import click
import torch
from pathlib import Path

from DynaGen import load_DynaGen_from_checkpoint
from DynaGen.version import __version__
from DynaGen.utils import safeget

def exists(val):
    return val is not None

def simple_slugify(text, max_length = 255):
    return text.replace("-", "_").replace(",", "").replace(" ", "_").replace("|", "--").strip('-_')[:max_length]

def main():
    pass


