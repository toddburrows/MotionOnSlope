#Todd 03-05-21
#Slope Modelling (Released from rest down slope)
import math
import matplotlib.pyplot as plt

g = 9.80665

#Initial Parameters
u=0.0
t=0.0

#Slope Parameters
elevation_degrees = 80.0
coefficient_friction = 0.2
length_slope_m = 5.0

#Object Parameters
mass_kg = 3.0

#Calculations
weight_object = mass_kg * g
elevation_rad = math.radians(elevation_degrees)
reaction_force = weight_object * (math.cos(elevation_rad))
friction_force = reaction_force * coefficient_friction
force_down_slope = weight_object * (math.sin(elevation_rad))

#If component of weight is not greater than friction then wont move
move=True
if friction_force >= force_down_slope:
    friction_force = force_down_slope
    move=False

if move:
    resultant_force = force_down_slope - friction_force
    a = resultant_force / mass_kg

    #Solving Quadratic using Suvat
    A = 0.5 * a
    B = u
    C = -1 * length_slope_m

    t1 = ((-1*B)+(((B*2)-(4*A*C))**0.5)) / (2 * A)
    t2 = ((-1*B)+(((B*2)-(4*A*C))**0.5)) / (2 * A)

    #Taking the positive solution as t>=0
    if t1 <= 0:
        final_time = float(t2)
    else:
        final_time = float(t1)

    t_array = []
    v_array = []
    v=u

    #generating values
    while t<final_time:
        t=t+0.000001
        t_array.append(t)
        v = v + (a * 0.000001)
        v_array.append(v)

    #giving results
    print("Object moves, acceleration is",a,"m/s/s")
    print("Reaches bottom after",final_time,"s\nIt is travelling at",v_array[(len(v_array)-1)],"m/s when it reaches the bottom.\nSee graph")

    #plotting graph
    plt.plot(t_array,v_array,linewidth=2)
    plt.xlabel("time (s)")
    plt.ylabel("velocity (m/s)")
    plt.show()
        
else:
    print("Object will stay stationary")

#just a subroutine for testing
def test():
    print(weight_object)
    print(elevation_rad)
    print(reaction_force)
    print(friction_force)
    print(force_down_slope)
    print(a)
    print(final_time)

test()
