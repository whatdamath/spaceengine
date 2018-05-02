
# coding: utf-8

# In[48]:


def planetoid(name, sma, incl, anomaly):
    planet_info='''Planet	"{}"
        {{
            ParentBody     "RS 1228-511-0-0-320"
            Class          "Terra"
            Mass            1
            Radius          6500
            InertiaMoment   0.33111
            Oblateness      0.0055007
            RotationPeriod  24
            RotationEpoch   0
            Obliquity       -36.12
            EqAscendNode    88.924

            AbsMagn         -2.9442
            SlopeParam      2.3619
            AlbedoBond      0.15
            AlbedoGeom      0.36
            Brightness      1
            BrightnessHDR   1


            Orbit
            {{
                RefPlane        "Equator"
                Period          1
                SemiMajorAxis   {}
                Eccentricity    0
                Inclination     {}
                AscendingNode   93.9278942
                ArgOfPericenter 24.2314588
                MeanAnomaly     {}
            }}
        }}\n'''.format(name, sma, incl, anomaly)
    return planet_info

import math
hill_sphere = 2*math.pi*1/104
semiMajorAxis = hill1 +1
axis = [1, semiMajorAxis]
inclination =180
inclin_list = [-inclination, inclination]
for x in range(6):
    inclination *= -1
    hill = 2*math.pi*semiMajorAxis/104
    semiMajorAxis = semiMajorAxis + hill
    axis.append(semiMajorAxis)
    inclin_list.append(inclination)

with open ("planet.sc", "a") as f:
    for y in range(8):
        sma = axis[y]
        incl = inclin_list[y]
        for x in range(52):
            name = "Ring"+str(y)+"Earth" + str(x)
            anomaly = x*(360/52)
            f.write(planetoid(name, sma, incl, anomaly))

