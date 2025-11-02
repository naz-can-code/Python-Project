# {
#  "cells": [
#   {
#    "cell_type": "code",
#    "execution_count": None,
#    "id": "026d1669-fe9b-4c7c-819c-fd935120dd40",
#    "metadata": {},
#    "outputs": [],
#    "source": [
#     "import pandas as pd\n",
#     "import os\n",
#     "from sqlalchemy import create_engine\n",
#     "import logging\n",
#     "import time\n",
#     "\n",
#     "logging.basicConfig(\n",
#     "    filename = \"logs/ingestion_db.log\",\n",
#     "    level=logging.DEBUG,\n",
#     "    format=\"%(asctime)s - %(levelname)s - %(message)s\",\n",
#     "    filemode=\"a\"\n",
#     ")\n",
#     "\n",
#     "engine = create_engine('sqlite:///inventory.db')\n",
#     "\n",
#     "'''INSERT CONTINUOUS DATA FRAME INTO DATABASE TABLE'''\n",
#     "def ingest_db(df, table_name, engine):\n",
#     "    df.to_sql(table_name, con = engine, if_exists = 'replace', index=False)\n",
#     "\n",
#     "def load_raw_data():\n",
#     "    '''This function will load the CSVs as dataframe and ingest into db'''\n",
#     "    start = time.time()\n",
#     "    for file in os.listdir(r'C:\\Users\\harsh\\OneDrive\\Desktop\\vendor performance\\data'):\n",
#     "                           if '.csv' in file:\n",
#     "                               full_path = os.path.join(r'C:\\Users\\harsh\\OneDrive\\Desktop\\vendor performance\\data', file)\n",
#     "                               df = pd.read_csv(full_path)\n",
#     "                               logging.info(f'Ingesting {file} in db')\n",
#     "                               ingest_db(df, file[:-4], engine)\n",
#     "\n",
#     "    end = time.time()\n",
#     "    total_time = (end - start)/60\n",
#     "    \n",
#     "    logging.info('------------Ingestion Complete------------')\n",
#     "    logging.info(f'\\nTotal TIme Taken: {total_time} minutes')\n",
#     "\n",
#     "if __name__=='__main__':\n",
#     "    load_raw_data()"
#    ]
#   },
#   {
#    "cell_type": "code",
#    "execution_count": 7,
#    "id": "fd59bc3f-626c-457f-a3ae-8952b8123482",
#    "metadata": {},
#    "outputs": [
#     {
#      "name": "stdout",
#      "output_type": "stream",
#      "text": [
#       "C:\\Users\\harsh\\OneDrive\\Desktop\\vendor performance\\data\n"
#      ]
#     }
#    ],
#    "source": [
#     "# print(os.getcwd())"
#    ]
#   }
#  ],
#  "metadata": {
#   "kernelspec": {
#    "display_name": "Python 3 (ipykernel)",
#    "language": "python",
#    "name": "python3"
#   },
#   "language_info": {
#    "codemirror_mode": {
#     "name": "ipython",
#     "version": 3
#    },
#    "file_extension": ".py",
#    "mimetype": "text/x-python",
#    "name": "python",
#    "nbconvert_exporter": "python",
#    "pygments_lexer": "ipython3",
#    "version": "3.12.5"
#   }
#  },
#  "nbformat": 4,
#  "nbformat_minor": 5
# }

import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename = "logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

engine = create_engine('sqlite:///inventory.db')

'''INSERT CONTINUOUS DATA FRAME INTO DATABASE TABLE'''
def ingest_db(df, table_name, engine):
    df.to_sql(table_name, con = engine, if_exists = 'replace', index=False)

def load_raw_data():
    '''This function will load the CSVs as dataframe and ingest into db'''
    start = time.time()
    for file in os.listdir(r'C:\Users\harsh\OneDrive\Desktop\vendor performance\data'):
                           if '.csv' in file:
                               full_path = os.path.join(r'C:\Users\harsh\OneDrive\Desktop\vendor performance\data', file)
                               df = pd.read_csv(full_path)
                               logging.info(f'Ingesting {file} in db')
                               ingest_db(df, file[:-4], engine)

    end = time.time()
    total_time = (end - start)/60
    
    logging.info('------------Ingestion Complete------------')
    logging.info(f'\nTotal TIme Taken: {total_time} minutes')

if __name__=='__main__':
    load_raw_data()