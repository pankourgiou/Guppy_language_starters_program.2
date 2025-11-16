from guppylang import guppy
from guppylang.std.builtins import owned
from guppylang.std.quantum import cx, h, measure, qubit, x, z


@guppy
def teleport(src: qubit @owned, tgt: qubit) -> None:
    """Teleports the state in `src` to `tgt`."""
    # Create ancilla and entangle it with src and tgt
    tmp = qubit()
    h(tmp)
    cx(tmp, tgt)
    cx(src, tmp)

    # Apply classical corrections
    h(src)
    if measure(src):
        z(tgt)
    if measure(tmp):
        x(tgt)
