# Basic Data Exploration with pandas on Bikeshare Data
_A Python project using pandas to explore bikeshare data._

# Project Overview

This project focuses on pandas library usage and simple statistics methods to perform descriptive analysis on the bikeshare data from three major U.S. cities - Chicago, Washington, and New York City - to display information such as most popular days or most common stations.

### Running the program

You can input 'python bikeshare.py' on your terminal to run this program. I use Anaconda's command prompt on a Windows 10 machine.

### Program Details

The program takes user input for the city (e.g. Chicago), month for which the user wants to view data (e.g. January; also includes an 'all' option), and day for which the user wants to view data (e.g. Monday; also includes an 'all' option).

Upon receiving the user input, it goes ahead and asks the user if they want to view the raw data (5 rows of data initially) or not. Following the input received, the program prints the following details:

* Most popular month
* Most popular day
* Most popular hour
* Most popular start station
* Most popular end station
* Most popular combination of start and end stations
* Total trip duration
* Average trip duration
* Types of users by number
* Types of users by gender (if available)
* The oldest user (if available)
* The youngest user (if available)
* The most common birth year amongst users (if available)

Finally, the user is prompted with the choice of restarting the program or not.

# Requirements

* Language: Python 3.6 or above
* Libraries: pandas, numpy, time

# Project Data

* chicago.csv - Stored in the data folder, the chicago.csv file is the dataset containing all bikeshare information for the city of Chicago provided by Udacity.

* new_york_city.csv - Dataset containing all bikeshare information for the city of New York provided by Udacity.

* washington.csv - Dataset containing all bikeshare information for the city of Washington provided by Udacity. Note: This does not include the 'Gender' or 'Birth Year' data.

# Built with

* [Python 3.6.6](https://www.python.org/) - The language used to develop this.
* [pandas](https://pandas.pydata.org/) - One of the libraries used for this.
* [numpy](http://www.numpy.org/) - One of the libraries used for this.
* [time](https://docs.python.org/2/library/time.html) - One of the libraries used for this.

# Author

 * [Aritra Chattaraj](https://github.com/aritra96) - Sole author for this program. Mentioned all the help received in 'Acknowledgements' section.
  
# Acknowledgements

* [xhlow](https://github.com/xhlow) - xhlow's repository helped with understanding the structure and details of certain functions.
* [philribbens](https://github.com/philribbens) - philribben's repository also added to better understanding of the structure for this project.
* [pandas docs](http://pandas.pydata.org/pandas-docs/stable/) - pandas documentation was immensely helpful in understanding the implemention of pandas methods used in this project.
* [Udacity](https://udacity.com) - Udacity's Data Analyst Nanodegree program and their instructors were extremely helpful while I was pursuing this project.
* Finally, I'd like to mention my college courses on Principles of Econometrics and Intermediary Econometrics for introducing me to data analysis and R programming. The concepts embodied in the pandas library (e.g. data frame) were very similar to the ones used while I was working on my R projects for college assignments.
