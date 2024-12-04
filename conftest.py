import sys
import os

# Ajouter le chemin racine du projet au sys.path pour que pytest trouve les modules
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))