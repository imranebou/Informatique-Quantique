from qiskit import QuantumCircuit, transpile, Aer, execute

qc = QuantumCircuit(2)
qc.h(0)
qc.cx(0, 1)

simulator = Aer.get_backend('statevector_simulator')
result = execute(qc, simulator).result()

print(result.get_statevector())
