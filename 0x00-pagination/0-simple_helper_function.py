#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a function named index_range that takes two integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """
    Returns start and end index for pagination

    Args:
        page (int): page number
        page_size (int): page size

    Returns:
        Tuple: start and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
