#!/usr/bin/python
import sys


def lb_to_kg(pounds):
    output_kg = pounds/2.20462
    return output_kg

def kg_to_lb(kg):
    output_lb = kg*2.20462
    return output_lb

def lt_to_gal(litre):
    output_gal = litre/3.78541
    return output_gal

def gal_to_lt(gal):
    output_lt = gal*3.78541
    return output_lt

def km_to_mi(k_meter):
    output_miles = k_meter/1.609344
    return output_miles

def mi_to_km(mile):
    output_km = mile*1.609344
    return output_km
