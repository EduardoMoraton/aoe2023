from collections import deque

class CircuitModule:
    def __init__(self, label, gate_type, outputs):
        self.label = label
        self.gate_type = gate_type
        self.outputs = outputs

        if gate_type == "%":
            self.memory_state = "off"
        else:
            self.memory_state = {}

    def __repr__(self):
        return f"{self.label}{{gate_type={self.gate_type}, outputs={','.join(self.outputs)}, memory_state={str(self.memory_state)}}}"

modules_dict = {}
broadcast_targets_list = []

path =  '../input.txt'

for line in open(path):
    input_str, output_str = line.strip().split(" -> ")
    outputs_list = output_str.split(", ")

    if input_str == "broadcaster":
        broadcast_targets_list = outputs_list
    else:
        gate_type = input_str[0]
        label = input_str[1:]
        modules_dict[label] = CircuitModule(label, gate_type, outputs_list)

for module_name, circuit_module in modules_dict.items():
    for output_name in circuit_module.outputs:
        if output_name in modules_dict and modules_dict[output_name].gate_type == "&":
            modules_dict[output_name].memory_state[module_name] = "lo"

low_signal_count = high_signal_count = 0

for _ in range(1000):
    low_signal_count += 1
    queue = deque([(None, target_name, "lo") for target_name in broadcast_targets_list])

    while queue:
        origin_name, target_name, signal_type = queue.popleft()

        if signal_type == "lo":
            low_signal_count += 1
        else:
            high_signal_count += 1

        if target_name not in modules_dict:
            continue

        current_module = modules_dict[target_name]

        if current_module.gate_type == "%":
            if signal_type == "lo":
                current_module.memory_state = "on" if current_module.memory_state == "off" else "off"
                outgoing_signal = "hi" if current_module.memory_state == "on" else "lo"
                for output_name in current_module.outputs:
                    queue.append((current_module.label, output_name, outgoing_signal))
        else:
            current_module.memory_state[origin_name] = signal_type
            outgoing_signal = "lo" if all(x == "hi" for x in current_module.memory_state.values()) else "hi"
            for output_name in current_module.outputs:
                queue.append((current_module.label, output_name, outgoing_signal))

print(low_signal_count * high_signal_count)
