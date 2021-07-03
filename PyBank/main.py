{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 108,
   "id": "25569a41",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv \n",
    "from statistics import mean"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "id": "2cbb873b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Resources/budget_data.csv'"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "budget_data_path=os.path.join('Resources', 'budget_data.csv')\n",
    "budget_data_path"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "id": "60b00411",
   "metadata": {},
   "outputs": [],
   "source": [
    "date=[]\n",
    "profit=[]\n",
    "profit_change=[]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "id": "a6ad89db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "-------------------\n",
      "Total month: 86\n",
      "Total : 38382578\n",
      "Average  Change :-2315.12\n",
      "Greatest Increase in Profits: Feb-2012,(1926159)\n",
      "Greatest Decrease in Profit: Sep-2013,(-2196167)\n"
     ]
    }
   ],
   "source": [
    "with open (budget_data_path) as bank_data_file:\n",
    "    \n",
    "    csvreader=csv.reader(bank_data_file, delimiter=',')\n",
    "    header=next(csvreader)\n",
    "    \n",
    "    \n",
    "    for row in csvreader:\n",
    "    \n",
    "#Total_month\n",
    "        date.append(row[0])\n",
    "    \n",
    "#total_revenue\n",
    "        profit.append(int(row[1]))\n",
    "# avrage_change\n",
    "    for i in range(len(profit)-1):\n",
    "        profit_change.append(profit[i+1]-profit[i])\n",
    "#greatest_increas  \n",
    "        max_increa=max(profit_change)\n",
    "#greates_decreas   \n",
    "        max_decrease=min(profit_change)\n",
    "#Avrage change\n",
    "        avrage_change=mean(profit_change)\n",
    "            \n",
    "\n",
    "    print(\"Financial Analysis\")\n",
    "    print(\"-------------------\")\n",
    "    print(f\"Total month: {len(date)}\")\n",
    "    print(f\"Total : {sum(profit)}\")\n",
    "    print(f\"Average  Change :{round(avrage_change,2)}\")\n",
    "    print(f\"Greatest Increase in Profits: {date[profit_change.index(max(profit_change))+1]},({max_increa})\")\n",
    "    print(f\"Greatest Decrease in Profit: {date[profit_change.index(min(profit_change))+1]},({max_decrease})\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "904c9239",
   "metadata": {},
   "outputs": [],
   "source": [
    "output = \"result.txt\"\n",
    "with open(\"result\",\"w\") as new:\n",
    "    new.write(\"Financial Analysis\")\n",
    "    new.write(\"\\n\")\n",
    "    new.write(\"--------------------\")\n",
    "    new.write(\"\\n\")\n",
    "    new.write(f\"Total month: {len(date)}\")\n",
    "    new.write(\"\\n\")\n",
    "    new.write(f\"Total: ${sum(profit)}\")\n",
    "    new.write(\"\\n\")\n",
    "    new.write(f\"Average Change: {round(avrage_change,2)}\")\n",
    "    new.write(\"\\n\")\n",
    "    new.write(f\"Greatest Increase in Profits: {date[profit_change.index(max(profit_change))+1]},({max_increa})\")\n",
    "    new.write(\"\\n\")\n",
    "    new.write(f\"Greatest Decrease in Profits: {date[profit_change.index(min(profit_change))+1]},({max_decrease})\")"
   ]
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
