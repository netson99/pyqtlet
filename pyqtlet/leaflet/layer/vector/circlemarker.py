from .path import Path


class CircleMarker(Path):
    def __init__(self, latLng, options=None):
        super().__init__()
        self.latLng = latLng
        self.options = options
        self._initJs()

    def _initJs(self):
        leafletJsObject = 'L.circleMarker({latLng}'.format(latLng=self.latLng)
        if self.options:
            leafletJsObject += ', {options}'.format(options=self.options)
        leafletJsObject += ')'
        self._createJsObject(leafletJsObject)

    def setLatLng(self, latLng):
        js = '{layerName}.setLatLng({latLng})'.format(
                layerName=self._layerName, latLng=latLng)
        self.runJavaScript(js)
        
    def setStyle(self, styleNew):
        js = '{layerName}.setStyle({style})'.format(
                layerName=self._layerName, style=styleNew)
        self.runJavaScript(js)
        
    def openPopup(self):
        js = '{layerName}.openPopup()'.format(layerName=self._layerName)
        self.runJavaScript(js)
