class SimpleThermostat:
    def __init__(self, threshold=20):
        self.threshold = threshold  # Temperature threshold in Celsius

    def perceive_and_act(self, temperature):
        """Decide whether to turn the heater ON or OFF based on the current temperature"""
        if temperature < self.threshold:
            action = "Turn ON heater"
        else:
            action = "Turn OFF heater"
        return action

# Simulate a sequence of temperatures
temperatures = [18, 20, 22, 19, 21, 17, 23]

# Initialize thermostat
thermostat = SimpleThermostat(threshold=20)

# Run the simulation
for temp in temperatures:
    action = thermostat.perceive_and_act(temp)
    print(f"Temperature: {temp}°C - Action: {action}")