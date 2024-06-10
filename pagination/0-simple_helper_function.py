#!/usr/bin/env python3
""" Simple helper function """


def index_range(page, page_size):
    """Simple helper function"""
    return (page_size*(page-1), page_size*page)
