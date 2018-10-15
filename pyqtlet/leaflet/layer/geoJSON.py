from .featuregroup import FeatureGroup

class GeoJSON(FeatureGroup):
    def __init__(self, geoJSONTemplate, options=None):
        self.geoJSONTemplate = geoJSONTemplate
        self.options = options
        super().__init__()
        #self._initJs()
        
    def _initJs(self):
        #print("Init GeoJSON : {} - {}".format(self.geoJSONTemplate, self.options))
        leafletJsObject = 'L.geoJSON({geojson}'.format(geojson=self.geoJSONTemplate)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)
