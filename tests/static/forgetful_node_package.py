"""
An incorrect node package for the purpose of testing node package registration.
"""

from pyiron_workflow import Workflow


@Workflow.wrap_as.single_value_node("sum")
def add(x: int, y: int) -> int:
    return x + y


# nodes = [add]  # Oops, we "forgot" to populate a `nodes` list