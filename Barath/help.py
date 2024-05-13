import os
import importlib.util

# Directory containing plugins
PLUGIN_DIRECTORY = "Barath/plugins"

# Function to load plugins and their help text
def load_plugin_help():
    help_texts = {}
    for filename in os.listdir(PLUGIN_DIRECTORY):
        if filename.endswith(".py"):
            plugin_path = os.path.join(PLUGIN_DIRECTORY, filename)
            spec = importlib.util.spec_from_file_location("module.name", plugin_path)
            plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin_module)
            help_texts[plugin_module.__mod_name__] = plugin_module.__help__
    return help_texts

# Function to handle .help command, just an example
def handle_help_command():
    help_texts = load_plugin_help()
    help_message = "\n".join(f"{mod}: {help}" for mod, help in help_texts.items())
    return help_message

# Example of usage
print(handle_help_command())
