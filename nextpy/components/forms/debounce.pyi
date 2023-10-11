"""Stub file for debounce.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Optional, Union, overload
from nextpy.components.component import Component
from nextpy.core.vars import Var, BaseVar, ComputedVar
from nextpy.event import EventHandler, EventChain, EventSpec

def props_not_none(c: Component) -> dict[str, Any]: ...
def _collect_first_child_and_props(
    c: Component,
) -> tuple[Component, dict[str, Any]]: ...

class DebounceInput(Component):
    @overload
    @classmethod
    def create(cls, *children, min_length: Optional[Union[Var[int], int]] = None, debounce_timeout: Optional[Union[Var[int], int]] = None, force_notify_by_enter: Optional[Union[Var[bool], bool]] = None, force_notify_on_blur: Optional[Union[Var[bool], bool]] = None, value: Optional[Union[Var[str], str]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "DebounceInput":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            min_length: Minimum input characters before triggering the on_change event
            debounce_timeout: Time to wait between end of input and triggering on_change
            force_notify_by_enter: If true, notify when Enter key is pressed
            force_notify_on_blur: If true, notify when form control loses focus
            value: If provided, create a fully-controlled input
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
