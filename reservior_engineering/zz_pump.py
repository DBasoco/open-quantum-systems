from typing import Optional
import warnings
import numpy as np

from qiskit.circuit import QuantumCircuit, QuantumRegister, CircuitInstruction
from qiskit.circuit.library import BlueprintCircuit


class ZZPump(BlueprintCircuit):
    r"""ZZ Pump Circuit.

    More words.
    """

    def __init__(self, num_qubits: Optional[int] = None) -> None:
        """"Hello"""