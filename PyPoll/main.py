{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 132,
   "id": "e1ea7a53",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv\n",
    "from collections import Counter\n",
    "import pprint"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 133,
   "id": "13ca2cf3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Resources/election_data.csv'"
      ]
     },
     "execution_count": 133,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data_path=os.path.join('Resources' , 'election_data.csv')\n",
    "data_path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "id": "427dbf38",
   "metadata": {},
   "outputs": [],
   "source": [
    "voter_id=[]\n",
    "country=[]\n",
    "candidate=[]\n",
    "counter={}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 137,
   "id": "ba42632a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "---------------------\n",
      "Total Votes: 10563003\n",
      "---------------------\n",
      "Correy: 20.0%,(2112600)\n",
      "Khan: 63.0%,(6654693)\n",
      "Li: 14.0%,(1478820)\n",
      "---------------------\n",
      "Winner: Khan\n"
     ]
    }
   ],
   "source": [
    "with open (data_path) as election_data:\n",
    "    \n",
    "    csvreader=csv.reader(election_data,delimiter=',')\n",
    "    header=next(csvreader)\n",
    "    \n",
    "    for row in csvreader:\n",
    "        voter_id.append(row[0])\n",
    "   # \n",
    "        country.append(row[1])\n",
    "        candidate.append(row[2])\n",
    "        \n",
    "    counter = Counter(candidate)\n",
    "\n",
    "   # pprint.pprint(dict(counter),width=1)\n",
    "   \n",
    "\n",
    "Correy_percent=round((counter['Correy']/len(voter_id))*100,3)\n",
    "\n",
    "Khan_percent=round((counter['Khan']/len(voter_id))*100,3)\n",
    "\n",
    "Li_percent=round((counter['Li']/len(voter_id))*100,3)\n",
    "\n",
    "Tooley_percent=round((counter[\"O'Tooley\"]/len(voter_id))*100,3)\n",
    "\n",
    "\n",
    "#winner\n",
    "winner = max(counter,key=counter.get)\n",
    "\n",
    "print(\"Election Results\")\n",
    "print(\"---------------------\")\n",
    "print(f\"Total Votes: {len(voter_id)}\")\n",
    "print(\"---------------------\")\n",
    "print(f\"Correy: {Correy_percent}%,({counter['Correy']})\")\n",
    "print(f\"Khan: {Khan_percent}%,({counter['Khan']})\")\n",
    "print(f\"Li: {Li_percent}%,({counter['Li']})\")\n",
    "#print(F\"\"\"O'Tooley:\"{Tooley_percent}\"%\"({counter[\"O'Tooley\"]}\"\"\"))\n",
    "print(\"---------------------\")\n",
    "print(f\"Winner: {winner}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d40d22c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
