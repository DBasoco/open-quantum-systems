from typing import Optional

from qiskit.circuit.gate import Gate
from qiskit.circuit.quantumregister import QuantumRegister


class XXPump(Gate):
    """The xx_pump gate."""

    def __init__(self, label: Optional[str] = None):
        """Create new xx_pump gate."""
        super().__init__("xx_pump", 2, [], label=label)

    def _define(self):
        from qiskit.circuit.quantumcircuit import QuantumCircuit
        from qiskit.circuit.library import SwapGate, CZGate

        q = QuantumRegister(2, "q")
        qc = QuantumCircuit(q, name=self.name)
        rules = [
            (SwapGate(), [q[0], q[1]], []),
            (CZGate(), [q[0], q[1]], []),
        ]
        for instr, qargs, cargs in rules:
            qc._append(instr, qargs, cargs)

        self.definition = qc

    def inverse(self):
        """Return inverse xx_pump gate."""
        return XXPump()  # self-inverse
