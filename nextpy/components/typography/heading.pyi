"""Stub file for heading.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `scripts/pyi_generator.py`!
# ------------------------------------------------------

from typing import Literal, Optional, Union, overload
from nextpy.components.libs.chakra import ChakraComponent
from nextpy.components.component import Component
from nextpy.core.vars import Var, BaseVar, ComputedVar
from nextpy.core.event import EventHandler, EventChain, EventSpec

class Heading(ChakraComponent):
    @overload
    @classmethod
    def create(cls, *children, as_: Optional[Union[Var[str], str]] = None, size: Optional[Union[Var[Literal["lg", "md", "sm", "xs", "xl", "2xl", "3xl", "4xl"]], Literal["lg", "md", "sm", "xs", "xl", "2xl", "3xl", "4xl"]]] = None, on_blur: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_context_menu: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_double_click: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_focus: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_down: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_enter: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_leave: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_move: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_out: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_over: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_mouse_up: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_scroll: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, on_unmount: Optional[Union[EventHandler, EventSpec, List, function, BaseVar]] = None, **props) -> "Heading":  # type: ignore
        """Create the component.

        Args:
            *children: The children of the component.
            as_: Override the tag. The default tag is `<h2>`.
            size: "4xl" | "3xl" | "2xl" | "xl" | "lg" | "md" | "sm" | "xs"
            **props: The props of the component.

        Returns:
            The component.

        Raises:
            TypeError: If an invalid child is passed.
        """
        ...
