# src/utils.py
import geopandas as gpd

def load_shapefile(path, crs='EPSG:4326'):
    gdf = gpd.read_file(path)
    return gdf.to_crs(crs)
