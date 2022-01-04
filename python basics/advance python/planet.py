from weakref import WeakKeyDictionary
class Positive:
    def __init__(self):
        self._instance_data = WeakKeyDictionary()
    def __get__(self, instance, owner):
        return self._instance_data[instance]
    def __set__(self, instance, value):
        if value <=0:
            raise ValueError("value {} is not positive".format(value)) 
        self._instance_data[instance] = value

    def __delete__(self, instance):
        raise AttributeError("Cannot delete attribute")

                   
class planet:
    def __init__(self, 
                 name,
                 radius_meters,
                 mass_kilograms,
                 orbital_period_seconds,
                 surface_temparature_kelvin):
        self.name = name
        self.radius_meters = radius_meters
        self.mass_kilograms = mass_kilograms
        self.orbital_period_seconds = orbital_period_seconds
        self.surface_temparature_kelvin = surface_temparature_kelvin

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Cannot set empty planet.name")
        self._name = value

    radius_meters = Positive()
    mass_kilograms = Positive()
    orbital_period_seconds = Positive()
    surface_temparature_kelvin = Positive()            
