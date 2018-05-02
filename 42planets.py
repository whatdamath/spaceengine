
def planetoid(name, anomaly):
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
                SemiMajorAxis   1
                Eccentricity    0
                Inclination     0
                AscendingNode   93.9278942
                ArgOfPericenter 24.2314588
                MeanAnomaly     {}
            }}
        }}\n'''.format(name, anomaly)
    return planet_info

with open ("planet.sc", "a") as f:

    for x in range(52):
        name = "Earth" + str(x)
        anomaly = x*(360/42)
        f.write(planetoid(name, anomaly))

