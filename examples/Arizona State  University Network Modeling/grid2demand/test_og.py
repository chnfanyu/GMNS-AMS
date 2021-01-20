# -*- coding:utf-8 -*-
import osm2gmns as og

"""
Step 1: get network from .osm file
Step 2: consolidate complex intersections based on automatically identified complex intersection information
Step 3: output the network with intersections consolidated
"""
# net = og.getNetFromOSMFile('map.osm', strict_mode=True, remove_isolated=True, simplify=True, int_buffer=18.0)
# og.consolidateComplexIntersections(net)
# og.outputNetToCSV(net)



"""
Step 1: get network from .osm file
Step 2: output the network and automatically identified complex intersection information to CSV files
Step 3: modify complex intersection information manually according to the network topology
Step 4: load network from CSV files
Step 5: consolidate complex intersections based on the modified complex intersection information
Step 6: output the network with intersections consolidated
"""

net = og.getNetFromOSMFile(r'map.osm', network_type=('railway','aeroway','auto','walk','bike'),\
                           POIs=True,default_lanes=True,default_speed=True)
og.connectPOIWithNet(net)

og.generateNodeActivityInfo(net)

og.outputNetToCSV(net)

# net = og.getNetFromCSV()
# og.consolidateComplexIntersections(net, external_file='complex_intersection.csv')
# og.outputNetToCSV(net, output_folder='consolidated')
