#This code uses the range and sum functions to calculate the sum of the numbers from 1-100. The range function is used to gather all the numbers from 1-100 together,and sum calculates the sum of it all, adding up to 5050. I also use list to list the numbers from 1-100
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a5ef0c56",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "5050\n",
      "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]\n"
     ]
    }
   ],
   "source": [
    "num = 100\n",
    "\n",
    "total = sum(range(1, num + 1))\n",
    "print(total)\n",
    "\n",
    "print(list(range(1, num + 1)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "83a64260",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
