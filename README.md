# Tiny Python LGA

A version of the little genetic algorithm in python.  Finds the maximum value of a function with a population of binary numbers.

To change the function to be maximized, just replace the content of the fit_func method.  

You can also tweak the other general parameters; population size, and the size of the genome.  For larger genomes, the population tends to get locked in suboptimal local maximums.  

To run, simply exectute the script:
````
> python src/lga.py
````