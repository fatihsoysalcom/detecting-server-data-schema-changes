def get_server_status_pre_update():
    """Simulates server status data before an update."""
    return {
        "status": "online",
        "online_players": 15,
        "max_players": 20,
        "server_version": "1.19.4",
        "motd": "Welcome to the old server!"
    }

def get_server_status_post_update():
    """Simulates server status data after an update, with schema changes."""
    # --- SIMULATING AN MCP SERVER UPDATE ---
    # The server's data reporting structure has changed. 
    # Key names are different, some keys might be removed or added.
    return {
        "server_state": "running",       # 'status' changed to 'server_state'
        "current_players": 18,           # 'online_players' changed to 'current_players'
        "max_capacity": 25,              # 'max_players' changed to 'max_capacity'
        "minecraft_version": "1.20.1", # 'server_version' changed to 'minecraft_version'
        "uptime_hours": 24,              # New key added
        "description": "Welcome to the new server!" # 'motd' changed to 'description'
    }

class MonitoringAgent:
    """
    A simple monitoring agent designed to parse server status data.
    It has hardcoded expectations about the data structure.
    """
    def __init__(self, name):
        self.name = name

    def process_status(self, server_data):
        print(f"\n--- {self.name} processing server status ---")
        try:
            # --- AGENT'S HARDCODED EXPECTATIONS ---
            # The agent expects specific keys ('online_players', 'server_version').
            # This simulates how monitoring tools rely on a stable data schema.
            players = server_data["online_players"]
            version = server_data["server_version"]
            print(f"Successfully retrieved: Players Online = {players}, Server Version = {version}")
            print("Agent reports: Server is healthy based on expected metrics.")
        except KeyError as e:
            # --- DEMONSTRATING DATA INCONSISTENCY ISSUE ---
            # If the server updates and changes key names, the agent fails to find them.
            # This highlights the challenge of maintaining monitoring tools in dynamic environments.
            print(f"ERROR: Agent failed to find expected key '{e}'.")
            print("This indicates a fundamental data structure change post-update.")
            print("Agent cannot accurately report server status due to schema mismatch.")
            print(f"Raw data received: {server_data}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# --- Main simulation ---
if __name__ == "__main__":
    agent = MonitoringAgent("MCP Monitor v1.0")

    print("Scenario 1: Agent monitoring pre-update server data")
    pre_update_data = get_server_status_pre_update()
    agent.process_status(pre_update_data)

    print("\n" + "="*50)
    print("SERVER UPDATE OCCURS: The server's data reporting schema changes!")
    print("="*50)

    print("\nScenario 2: Agent monitoring post-update server data")
    post_update_data = get_server_status_post_update()
    agent.process_status(post_update_data)

    print("\n--- End of Simulation ---")
    print("The agent, designed for the old data structure, fails to interpret the new one.")
    print("This demonstrates the challenge of data inconsistencies for monitoring agents in frequently updated systems like MCP servers.")
