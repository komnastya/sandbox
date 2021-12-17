import pathlib

from count import count_lines
from represent import represent

represent(count_lines(pathlib.Path(__file__).parent.parent))
