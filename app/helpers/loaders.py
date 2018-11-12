import re
from inspect import getmembers, isclass
from sys import modules  # noqa

__all__ = ['NiaPyListLoader']


class NiaPyListLoader:
    """Loader for fetching NiaPy's algorithms and benchmarks."""

    @staticmethod
    def get_niapy_algorithms():
        """Returns an array of NiaPy algorithms."""
        b_members = [b_member[0] for b_member in
                     getmembers(modules['NiaPy.algorithms.basic'], isclass)]
        m_members = [m_member[0] for m_member in
                     getmembers(modules['NiaPy.algorithms.modified'], isclass)]
        o_members = [o_member[0] for o_member in
                     getmembers(modules['NiaPy.algorithms.other'], isclass)]
        algorithms = []
        for member in b_members + m_members + o_members:
            algorithms.append(re.sub(r'\B([A-Z])', r' \1', member))
        return algorithms

    @staticmethod
    def get_niapy_benchmarks():
        """Returns an array of NiaPy benchmarks."""
        b_members = [b_member[0] for b_member in
                     getmembers(modules['NiaPy.benchmarks'], isclass)]
        benchmarks = []
        for member in b_members:
            benchmarks.append(re.sub(r'\B([A-Z])', r' \1', member))
        return benchmarks
