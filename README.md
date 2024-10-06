PARABOLIC REFLECTOR FOR 4G INTERNET ACCESS

This project demonstrates how to build a custom parabolic reflector to enhance 4G internet connectivity in rural or remote areas. The reflector design is based on a self-made structure using readily available materials, with the goal of improving signal reception using a 4G modem and MIMO/SISO feed antenna. For more details refer to the report file Parabolic_reflector_Ru.pdf (Russian) or Parabolic_reflector_Eng.pdf (English).

Based on the Python code templates (Sphere.py and Parabolic_reflector.py), we generated JavaScript codes with graphical user interfaces (GUI) that are accessible in a web browser: Sphere.html and Parabolic_reflector.html. To run the program, simply click on the file and allow your browser to open the corresponding webpage, where you can input the parameters for the paraboloid or sphere. To avoid errors when entering parameters, switch your keyboard to the English layout. Since the frequencies may be decimal numbers (e.g., 0.9 GHz), use a period "." to input non-integer values.

The JavaScript codes along with browser GUIs, used for generating G-files for laser cutting of the petals, are also provided: Cutting_paraboloid_petal.html and Cutting_sphere_petal.html.

KEY FEATURES:

  Design & Construction:
  
    Detailed algorithms for cutting parabolic reflector and sphere petals.
    
    Python and JavaScript codes to generate the reflector’s and sphere's petal profiles.

    Instructions for constructing the protective spherical housing for the reflector.

    Instructions for selecting 4G modems and MIMO/SISO feed antennae. 
    
  Customization:
  
    Adaptable for various reflector sizes and materials.
    
    Easy-to-follow assembly and installation steps for use in attic spaces.
    
  Signal Optimization:
  
    Guidance for selecting the optimal azimuth angle based on geographic location and nearest cellular towers.
    
    Real-world results of signal enhancement and performance testing.

GETTING STARTED:

1. Clone the repository:
   
    git clone https://github.com/DYK-Team/Parabolic_reflector.git

2. Set up Python environment:
   
    pip install numpy csv

3. Run calculations:

    Modify the Parabolic_reflector.py or Sphere.py script with your desired parameters.
  
    Use the generated profiles for cutting the petals and assembling the reflector or sphere.
