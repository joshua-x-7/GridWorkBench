# Containers: Container types for GridWorkbench
#
# Adam Birchfield, Texas A&M University
# 
# Log:
# 9/29/2021 Initial version, rearranged from prior draft so that most object fields
#   are only listed in one place, the PW_Fields table. Now to add a field you just
#   need to add it in that list.
# 11/2/2021 Renamed this file to core and added fuel type object
# 1/22/22 Separated this from main gridworkbench
# 4/2/22 Need to add some default fields
# 8/18/22 Throw exception if device or container does not exist
# 
from typing import OrderedDict
from .utils.exceptions import FieldDataException, GridObjDNE, \
    ContainerDeletedException

class Region:

    def __init__(self, wb, number):
        self._wb = wb
        self.number = number
        self._area_map = OrderedDict()
        
        self.name = ""
    
    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if hasattr(self, "_number"):
            del self.wb._region_map[self._number]
        if not isinstance(value, int):
            raise FieldDataException(f"Region number must be integer")
        if value < 1:
            raise FieldDataException(f"Region number {value} must be positive")
        if value in self.wb._region_map:
            raise FieldDataException(f"Region number {value} already exists!")
        self._number = value
        self.wb._region_map[self._number] = self

    def __str__(self):
        return f"Region {self.number} {self.name if hasattr(self, 'name') else ''}"

    def __repr__(self):
        return str(self) + f" {hex(id(self))}"

    @property
    def wb(self):
        return self._wb
    
    def area(self, number):
        if number in self._area_map:
            return self._area_map[number]
        else:
            raise GridObjDNE("Area {number} does not exist in Region {self.number}")

    @property
    def areas(self):
        return tuple(area for area in self._area_map.values())

    @property
    def subs(self):
        return tuple(sub for area in self.areas for sub in area.subs)

    @property
    def buses(self):
        return tuple(bus for area in self.areas for bus in area.buses)

    @property
    def gens(self):
        return tuple(gen for area in self.areas for gen in area.gens)

    @property
    def loads(self):
        return tuple(load for area in self.areas for load in area.loads)

    @property
    def shunts(self):
        return tuple(shunt for area in self.areas for shunt in area.shunts)
    
    @property
    def branches(self):
        return tuple(branch for area in self.areas for branch in area.branches)
    

class Area:
    
    def __init__(self, region, number):
        if not isinstance(region, Region):
            raise FieldDataException(f"Invalid region given to create area {number}")
        self._region = region
        self.number = number
        self._sub_map = OrderedDict()

        self.name = ""

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if hasattr(self, "_number"):
            del self.wb._area_map[self._number]
            del self.region._area_map[self._number]
        if not isinstance(value, int):
            raise FieldDataException(f"Area number must be integer")
        if value < 1:
            raise FieldDataException(f"Area number {value} must be positive")
        if value in self.region.wb._area_map:
            raise FieldDataException(f"Area number {value} already exists!")
        self._number = value
        self.wb._area_map[self._number] = self
        self.region._area_map[self._number] = self

    def __str__(self):
        return f"Area {self.number} {self.name if hasattr(self, 'name') else ''}"

    def __repr__(self):
        return str(self) + f" {hex(id(self))}"

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        if not isinstance(value, Region):
            raise FieldDataException(f"Invalid region given to move area {self.number}")
        del self.region._area_map[self._number]
        self._region = value
        self.region._area_map[self._number] = self

    @property
    def wb(self):
        return self._region._wb
    
    def sub(self, number):
        if number in self._sub_map:
            return self._sub_map[number]
        else:
            raise GridObjDNE("Substation {number} does not exist in Area" \
                + " {self.number}")

    @property
    def subs(self):
        return tuple(sub for sub in self._sub_map.values())

    @property
    def buses(self):
        return tuple(bus for sub in self.subs for bus in sub.buses)

    @property
    def gens(self):
        return tuple(gen for sub in self.subs for gen in sub.gens)

    @property
    def loads(self):
        return tuple(load for sub in self.subs for load in sub.loads)

    @property
    def shunts(self):
        return tuple(shunt for sub in self.subs for shunt in sub.shunts)
    
    @property
    def branches(self):
        return tuple(branch for sub in self.subs for branch in sub.branches)
    

class Sub:

    def __init__(self, area, number):
        if not isinstance(area, Area):
            raise FieldDataException(f"Invalid area provided to create sub {number}")
        self._area = area
        self.number = number
        self._bus_map = OrderedDict()
        
        self.name = ""
        self.latitude = 0
        self.longitude = 0

    def delete(self):
        for bus in list(self._bus_map.values()):
            bus.delete()
        del self._area._sub_map[self.number]
        del self.wb._sub_map[self.number]
        self._area = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if hasattr(self, "_number"):
            del self.area.wb._sub_map[self._number]
            del self.area._sub_map[self._number]
        if not isinstance(value, int):
            raise FieldDataException(f"Sub number must be integer")
        if value < 1:
            raise FieldDataException(f"Sub number {value} must be positive")
        if value in self.wb._sub_map:
            raise FieldDataException(f"Sub number {value} already exists!")
        self._number = value
        self.wb._sub_map[self._number] = self
        self.area._sub_map[self._number] = self

    def __str__(self):
        return f"Sub {self.number} {self.name if hasattr(self, 'name') else ''}"

    def __repr__(self):
        return str(self) + f" {hex(id(self))}"

    @property
    def area(self):
        if self._area is None: raise ContainerDeletedException("Sub deleted!")
        return self._area

    @area.setter
    def area(self, value):
        if not isinstance(value, Area):
            raise FieldDataException(f"Invalid area given to move sub {self.number}")
        del self.area._sub_map[self._number]
        self._area = value
        self.area._sub_map[self._number] = self

    @property
    def region(self):
        return self.area.region

    @property
    def wb(self):
        return self.area.wb
    
    def bus(self, number):
        if number in self._bus_map:
            return self._bus_map[number]
        else:
            raise GridObjDNE("Bus {number} does not exist in Substation" \
                " {self.number}")

    @property
    def buses(self):
        return tuple(bus for bus in self._bus_map.values())

    @property
    def gens(self):
        return tuple(gen for bus in self.buses for gen in bus.gens)

    @property
    def loads(self):
        return tuple(load for bus in self.buses for load in bus.loads)

    @property
    def shunts(self):
        return tuple(shunt for bus in self.buses for shunt in bus.shunts)
    
    @property
    def branches(self):
        return tuple(branch for bus in self.buses for branch in bus.branches)
    

class Bus:

    def __init__(self, sub, number):
        if not isinstance(sub, Sub):
            raise FieldDataException(f"Invalid sub provided to create bus {number}")
        self._sub = sub
        self.number = number
        self._node_map = OrderedDict()
        for f in self.wb.bus_pw_fields:
            setattr(self, f[0], f[2])

        self.name = ""
        self.vpu = 1.0
        self.vang = 0
        self.nominal_kv = 138.0
        self.zone_number = 1

    def delete(self):
        for node in list(self._node_map.values()):
            node.delete()
        del self._sub._bus_map[self.number]
        del self.wb._bus_map[self.number]
        self._sub = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if hasattr(self, "_number"):
            del self.wb._bus_map[self._number]
            del self.sub._bus_map[self._number]
        if not isinstance(value, int):
            raise FieldDataException(f"Bus number must be integer")
        if value < 1:
            raise FieldDataException(f"Bus number {value} must be positive")
        if value in self.wb._bus_map:
            raise FieldDataException(f"Bus number {value} already exists!")
        self._number = value
        self.wb._bus_map[self._number] = self
        self.sub._bus_map[self._number] = self

    def __str__(self):
        return f"Bus {self.number} {self.name if hasattr(self, 'name') else ''}"

    def __repr__(self):
        return str(self) + f" {hex(id(self))}"

    @property
    def sub(self):
        if self._sub is None: raise ContainerDeletedException("Bus deleted!")
        return self._sub

    @sub.setter
    def sub(self, value):
        if not isinstance(value, Sub):
            raise FieldDataException(f"Invalid sub given to move bus {self.number}")
        del self.sub._bus_map[self._number]
        self._sub = value
        self.sub._bus_map[self._number] = self
    
    @property
    def area(self):
        return self.sub.area

    @property
    def region(self):
        return self.sub.region

    @property
    def wb(self):
        return self.sub.wb

    def node(self, number):
        if number in self._node_map:
            return self._node_map[number]
        else:
            raise GridObjDNE("Node {number} does not exist in Bus {self.number}")

    @property
    def nodes(self):
        return tuple(node for node in self._node_map.values())

    def gen(self, id):
        for node in self.nodes:
            if id in node._gen_map:
                return node._gen_map[id]
        else:
            raise GridObjDNE("Gen {id} does not exist at Bus {self.number}")

    @property
    def gens(self):
        return tuple(gen for node in self.nodes for gen in node.gens)

    def load(self, id):
        for node in self.nodes:
            if id in node._load_map:
                return node._load_map[id]
        else:
            raise GridObjDNE("Load {id} does not exist at Bus {self.number}")

    @property
    def loads(self):
        return tuple(load for node in self.nodes for load in node.loads)

    def shunt(self, id):
        for node in self.nodes:
            if id in node._shunt_map:
                return node._shunt_map[id]
        else:
            raise GridObjDNE("Shunt {id} does not exist at Bus {self.number}")

    @property
    def shunts(self):
        return tuple(shunt for node in self.nodes for shunt in node.shunts)

    def branch_from(self, to_node_number, id):
        for node in self.nodes:
            if (to_node_number, id) in node._branch_from_map:
                return node._branch_from_map[(to_node_number, id)]
        else:
            raise GridObjDNE("Branch {self.number}-{to_node_number}-{id} does not" \
                " exist")

    @property
    def branches_from(self):
        return tuple(branch for node in self.nodes for branch in node.branches_from)

    def branch_to(self, from_node_number, id):
        for node in self.nodes:
            if (from_node_number, id) in node._branch_to_map:
                return node._branch_to_map[(from_node_number, id)]
        else:
            raise GridObjDNE("Branch {from_node_number}-{self.number}-{id} does not"\
                " exist")

    @property
    def branches_to(self):
        return tuple(branch for node in self.nodes for branch in node.branches_to)

    @property
    def branches(self):
        return tuple(branch for branchset in (self.branches_to, self.branches_from) 
            for branch in branchset)


class Node:

    def __init__(self, bus, number):
        self._bus = bus
        if not isinstance(bus, Bus):
            raise FieldDataException(f"Invalid bus provided to create node {number}")
        self.number = number
        self._gen_map = OrderedDict()
        self._load_map = OrderedDict()
        self._shunt_map = OrderedDict()
        self._branch_from_map = OrderedDict()
        self._branch_to_map = OrderedDict()

    def delete(self):
        del self._bus._node_map[self.number]
        del self.wb._node_map[self.number]
        self._gen_map = OrderedDict()
        self._load_map = OrderedDict()
        self._shunt_map = OrderedDict()
        self._branch_from_map = OrderedDict()
        self._branch_to_map = OrderedDict()
        self._bus = None

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if hasattr(self, "_number"):
            del self.wb._node_map[self._number]
            del self.bus._node_map[self._number]
        if not isinstance(value, int):
            raise FieldDataException(f"Node number must be integer")
        if value < 1:
            raise FieldDataException(f"Node number {value} must be positive")
        if value in self.wb._node_map:
            raise FieldDataException(f"Node number {value} already exists!")
        self._number = value
        self.wb._node_map[self._number] = self
        self.bus._node_map[self._number] = self

    def __str__(self):
        return f"Node {self.number} {self.name if hasattr(self, 'name') else ''}"

    def __repr__(self):
        return str(self) + f" {hex(id(self))}"

    @property
    def bus(self):
        if self._bus is None: raise ContainerDeletedException("Node deleted!")
        return self._bus

    @property
    def sub(self):
        return self.bus.sub

    @property
    def area(self):
        return self.bus.area

    @property
    def region(self):
        return self.bus.region

    @property
    def wb(self):
        return self.bus.wb
    
    def gen(self, id):
        if id in self._gen_map:
            return self._gen_map[id]
        else:
            raise GridObjDNE(f"Gen {id} does not exist at node {self.number}")

    def load(self, id):
        if id in self._load_map:
            return self._load_map[id]
        else:
            raise GridObjDNE(f"Load {id} does not exist at node {self.number}")

    def shunt(self, id):
        if id in self._shunt_map:
            return self._shunt_map[id]
        else:
            raise GridObjDNE(f"Shunt {id} does not exist at node {self.number}")

    def branch_from(self, to_node_number, id):
        if (to_node_number, id) in self._branch_from_map:
            return self._branch_from_map[(to_node_number, id)]
        else:
            raise GridObjDNE(f"Branch {self.number}-{to_node_number}-{id} does " \
                "not exist")

    def branch_to(self, from_node_number, id):
        if (from_node_number, id) in self._branch_to_map:
            return self._branch_to_map[(from_node_number, id)]
        else:
            raise GridObjDNE(f"Branch {from_node_number}-{self.number}-{id} does " \
                "not exist")

    @property
    def gens(self):
        return tuple(gen for gen in self._gen_map.values())

    @property
    def loads(self):
        return tuple(load for load in self._load_map.values())

    @property
    def shunts(self):
        return tuple(shunt for shunt in self._shunt_map.values())

    @property
    def branches_from(self):
        return tuple(branch for branch in self._branch_from_map.values())

    @property
    def branches_to(self):
        return tuple(branch for branch in self._branch_to_map.values())
    
    @property
    def branches(self):
        return tuple(branch for branchset in (self.branches_to, self.branches_from) 
            for branch in branchset)
