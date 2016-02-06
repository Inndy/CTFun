import os

"""
Provide pushd context

https://gist.github.com/Tatsh/7131812
"""

__all__ = [ 'pushd' ]

class PushdContext:
    cwd = None
    original_dir = None

    def __init__(self, dirname):
        self.cwd = os.path.realpath(dirname)

    def __enter__(self):
        self.original_dir = os.getcwd()
        os.chdir(self.cwd)
        return self

    def __exit__(self, type, value, tb):
        os.chdir(self.original_dir)

def pushd(dirname):
    """
    Provide `pushd` and `popd` mechanism

    :param dirname: where to pushd

    >>> pwd = lambda: print('cwd: %s' % os.getcwd())
    >>> pwd()
    >>> with pushd('./yet/another/directory') as context:
    >>>     pwd()
    >>> pwd()
    """
    return PushdContext(dirname)
