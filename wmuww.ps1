# Define the paths
$virtualEnvPath = ".\venv"  # Replace with the path to your virtual environment
$pythonScriptPath = "WakeMeUpWithWeather.py"  # Replace with the path to your Python script

# Activate the virtual environment
& "$virtualEnvPath\Scripts\Activate.ps1"

# Run the Python script
& "$virtualEnvPath\Scripts\python.exe" $pythonScriptPath


# Explicitly deactiveate
deactivate

# Exit the script
exit

