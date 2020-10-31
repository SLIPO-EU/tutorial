import numpy as np
import matplotlib
from matplotlib import colors
from matplotlib import cm
import matplotlib.pyplot as plt
import folium
from folium.plugins import HeatMap
from folium.plugins import MarkerCluster
from loci.analytics import bbox, kwds_freq
from wordcloud import WordCloud
from pysal.viz.mapclassify import Natural_Breaks
from pandas import DataFrame, concat
from geopandas import GeoDataFrame
import osmnx

def map_cluster_diff(clusters_a, clusters_b, intersection_color='#00ff00', diff_ab_color='#0000ff',
                     diff_ba_color='#ff0000', tiles='OpenStreetMap', width='100%', height='100%'):
    """Returns a Folium Map displaying the differences between two sets of clusters. Map center and zoom level
    are set automatically.
    Args:
         clusters_a (GeoDataFrame): The first set of clusters.
         clusters_b (GeoDataFrame): The second set of clusters.
         intersection_color (color code): The color to use for A & B.
         diff_ab_color (color code): The color to use for A - B.
         diff_ba_color (color code): The color to use for B - A.
         tiles (string): The tiles to use for the map (default: `OpenStreetMap`).
         width (integer or percentage): Width of the map in pixels or percentage (default: 100%).
         height (integer or percentage): Height of the map in pixels or percentage (default: 100%).
    Returns:
        A Folium Map object displaying cluster intersections and differences.
    """

    if clusters_a.crs['init'] != '4326':
        clusters_a = clusters_a.to_crs({'init': 'epsg:4326'})

    if clusters_b.crs['init'] != '4326':
        clusters_b = clusters_b.to_crs({'init': 'epsg:4326'})

    spatial_index_b = clusters_b.sindex
    prev_size_list = []
    prev_cid_list = []

    after_cid_list = []
    after_size_list = []
    intersect_area_percentage_list = []

    intersection_polygons = []
    diff_ab_polygs = []
    diff_ba_polygs = []
    new_polygs = []

    intersection_polygons_attr = []
    diff_ab_polygs_attr = []
    diff_ba_polygs_attr = []
    new_polygs_attr = []

    for index_1, row_1 in clusters_a.iterrows():
        size = row_1['size']
        poly = row_1['geometry']
        cid = row_1['cluster_id']

        prev_area = poly.area
        prev_cid_list.append(cid)
        prev_size_list.append(size)

        possible_matches_index = list(spatial_index_b.intersection(poly.bounds))
        possible_matches = clusters_b.iloc[possible_matches_index]

        max_area = 0.0
        max_cid_intersect = -1
        max_size = 0

        max_polyg = None
        max_intersect_polyg = None

        for index_2, row_2 in possible_matches.iterrows():
            size_2 = row_2['size']
            poly_2 = row_2['geometry']
            cid_2 = row_2['cluster_id']

            intersect_polyg = poly.intersection(poly_2)
            area = intersect_polyg.area

            if area > max_area:
                max_area = area
                max_cid_intersect = cid_2
                max_size = size_2
                max_polyg = poly_2
                max_intersect_polyg = intersect_polyg

        if max_cid_intersect == -1:
            after_cid_list.append(np.nan)
            after_size_list.append(np.nan)
            intersect_area_percentage_list.append(0.0)
            new_polygs.append(poly)
            new_polygs_attr.append('A (' + str(cid) + ')')
        else:
            after_cid_list.append(max_cid_intersect)
            after_size_list.append(max_size)
            intersect_area_percentage_list.append(max_area / prev_area)

            ab_diff_poly = poly.difference(max_polyg)
            ba_diff_poly = max_polyg.difference(poly)

            intersection_polygons.append(max_intersect_polyg)
            diff_ab_polygs.append(ab_diff_poly)
            diff_ba_polygs.append(ba_diff_poly)

            intersection_polygons_attr.append('A(' + str(cid) + ') & B(' + str(max_cid_intersect) + ')')
            diff_ab_polygs_attr.append('A(' + str(cid) + ') - B(' + str(max_cid_intersect) + ')')
            diff_ba_polygs_attr.append('B(' + str(max_cid_intersect) + ') - A(' + str(cid) + ')')

    spatial_index_a = clusters_a.sindex
    old_polys = []
    old_poly_attr = []

    for index, row in clusters_b.iterrows():
        poly = row['geometry']
        cid = row['cluster_id']

        possible_matches_index = list(spatial_index_a.intersection(poly.bounds))
        possible_matches = clusters_a.iloc[possible_matches_index]

        max_area = 0.0

        for index_2, row_2 in possible_matches.iterrows():
            poly_2 = row_2['geometry']

            intersect_polyg = poly.intersection(poly_2)
            area = intersect_polyg.area

            if area > max_area:
                max_area = area

        if max_area == 0.0:
            old_polys.append(poly)
            old_poly_attr.append('B (' + str(cid) + ')')

    intersection_gdf = GeoDataFrame(list(zip(intersection_polygons, intersection_polygons_attr)),
                                    columns=['geometry', 'diff'], crs=clusters_a.crs)

    diff_ab_gdf = GeoDataFrame(list(zip(diff_ab_polygs + new_polygs, diff_ab_polygs_attr + new_polygs_attr)),
                               columns=['geometry', 'diff'], crs=clusters_a.crs)

    diff_ba_gdf = GeoDataFrame(list(zip(diff_ba_polygs + old_polys, diff_ba_polygs_attr + old_poly_attr)),
                               columns=['geometry', 'diff'], crs=clusters_a.crs)

    # Filter out erroneous rows
    intersection_gdf = intersection_gdf[(intersection_gdf.geometry.area > 0.0)]
    diff_ab_gdf = diff_ab_gdf[(diff_ab_gdf.geometry.area > 0.0)]
    diff_ba_gdf = diff_ba_gdf[(diff_ba_gdf.geometry.area > 0.0)]

    # Add colors
    intersection_style = {'fillColor': intersection_color, 'weight': 2, 'color': 'black', 'fillOpacity': 0.8}
    diff_ab_style = {'fillColor': diff_ab_color, 'weight': 2, 'color': 'black', 'fillOpacity': 0.8}
    diff_ba_style = {'fillColor': diff_ba_color, 'weight': 2, 'color': 'black', 'fillOpacity': 0.8}
    intersection_gdf['style'] = intersection_gdf.apply(lambda x: intersection_style, axis=1)
    diff_ab_gdf['style'] = diff_ab_gdf.apply(lambda x: diff_ab_style, axis=1)
    diff_ba_gdf['style'] = diff_ba_gdf.apply(lambda x: diff_ba_style, axis=1)

    # Concatenate results
    return concat([diff_ab_gdf, diff_ba_gdf, intersection_gdf], ignore_index=True, sort=False)
