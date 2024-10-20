# Drone-Swarm

## Project Overview
The **Drone Swarm** project enables the synchronized movement of multiple drones without the need for a remote controller. Our system uses the **CherryPy** framework and **DroneKit** to act as a server, providing users with a web interface to control the drones or watch a pre-choreographed drone show. 

### Features:
- **Choreographed Drone Show**: Users can play a pre-recorded video that triggers synchronized movements of the drones, similar to drone shows.
- **Manual Drone Control**: The web interface allows manual control over one to four drones with buttons for:
  - Arming the drones
  - Takeoff and landing
  - Changing altitude
- **LED Panel Display**: Each drone is equipped with a **NeoPixel LED panel** that can display letters or symbols to enhance the visual appeal of the swarm.

## Technologies Used:
- **CherryPy Framework**: Acts as the backend server handling drone communication.
- **DroneKit**: Provides drone control capabilities, including movements and status management.
- **HTML/CSS And React**: For designing the user-friendly web interface.
- **NeoPixel LED Panel**: Attached to each drone to display customizable letters or symbols.

## Instructions for setup:

1. **Python Version Requirement**
Make sure you are using Python 3.7 or 3.9. To verify:
python --version
If you don’t have the correct version installed, download and install from the official Python website.

2. **Install DroneKit on Raspberry Pi and Laptop**
Install DroneKit on both the Raspberry Pi and your laptop:

pip install dronekit
3. **Install QGroundControl**
Download and install QGroundControl from here.
4. HTML, CSS, React Setup
For the frontend (HTML, CSS, React), these dependencies are handled via npm or yarn:

**Initialize a React project:**

npx create-react-app drone-swarm-ui
Navigate to your project folder:

cd drone-swarm-ui
Install additional React dependencies (if any):

npm install
With these instructions, your requirements.txt will handle the Python dependencies, and the rest can be handled via system-specific setup steps.









