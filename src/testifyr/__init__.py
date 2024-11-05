# SPDX-FileCopyrightText: 2024-present micha2718l <micha2718l@gmail.com>
#
# SPDX-License-Identifier: MIT

import matplotlib

matplotlib.use("agg")

from .elements import *
from .stuff import *

__all__ = [s for s in dir() if not s.startswith("_")]
