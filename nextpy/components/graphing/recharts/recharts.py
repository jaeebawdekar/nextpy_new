"""A component that wraps a recharts lib."""

from typing import List

from nextpy.components.component import Component, NoSSRComponent


class Recharts(Component):
    """A component that wraps a victory lib."""

    library = "recharts@2.8.0"

class RechartsCharts(NoSSRComponent):
    """A component that wraps a victory lib."""

    library = "recharts@2.8.0"
