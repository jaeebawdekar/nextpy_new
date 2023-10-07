"""A date input component."""

from dotreact.components.forms.input import Input
from dotreact.vars import Var


class DatePicker(Input):
    """A date input component."""

    # The type of input.
    type_: Var[str] = "date"  # type: ignore