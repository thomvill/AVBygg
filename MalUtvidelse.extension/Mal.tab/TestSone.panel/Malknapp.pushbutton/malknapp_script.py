# -*- coding: utf-8 -*-
#  Denne headeren må du ha om scriptet inneholder æøå.

__title__ = 'Sjekk logging'  # Denne overstyrer navnet på scriptfilen
__author__ = 'Asplan Viak'  # Dette kommer opp som navnet på utvikler av knappen
__doc__ = "Sjekker om loggingsystemet fungerer"  # Dette blir hjelp teksten som kommer opp når man holder musepekeren over knappen.

__cleanengine__ = False  # Dette forteller tolkeren at den skal sette opp en ny ironpython motor for denne knappen, slik at den ikke kommer i konflikt med andre funksjoner, settes nesten alltid til FALSE, TRUE når du jobber med knappen.
__fullframeengine__ = False  # Denne er nødvendig for å få tilgang til noen moduler, denne gjør knappen vesentrlig tregere i oppstart hvis den står som TRUE
__context__ = "zerodoc"  # Denne forteller tolkeren at knappen skal kunne brukes selv om et Revit dokument ikke er åpent.

from pyrevit import DB, UI  # Dette er alt du trenger for å få tilgang til nesten hele Revit sin API.
