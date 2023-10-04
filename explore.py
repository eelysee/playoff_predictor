import pandas as pd
import os

def import_nba():
    '''
    retrieves data from .csv files.
    assigns them to variables
    '''
    nbastats = pd.read_csv('csv/nbastats_2022.csv')
    nbapo = pd.read_csv('csv/datanba_po_2022.csv')
    nbadata = pd.read_csv('csv/datanba_2022.csv')
    nbastats_po = pd.read_csv('csv/nbastats_po_2022.csv')
    pbpstats = pd.read_csv('csv/pbpstats_2022.csv')
    shotdetail = pd.read_csv('csv/shotdetail_2022.csv')
    shotdetail_po = pd.read_csv('csv/shotdetail_po_2022.csv')
    
    return nbastats, nbapo, nbadata, nbastats_po, pbpstats, shotdetail, shotdetail_po

