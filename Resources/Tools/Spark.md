---
tags:
  - Data
  - Tool
---
Learn to implement distributed data management and machine learning in Spark using the PySpark package.

# What is Spark

==Spark is a platform for cluster computing==. Spark lets you spread data and computations over ==clusters== with multiple ==nodes== (think of each node as a separate computer). Splitting up your data makes it easier to work with very large datasets because each node only works with a small amount of data.

As each node works on its own subset of the total data, it also carries out a part of the total calculations required, so that both ==data processing and computation are performed in parallel over the nodes in the cluster==. It is a fact that parallel computation can make certain types of programming tasks much faster.

However, with greater computing power comes greater complexity.

Deciding whether or not Spark is the best solution for your problem takes some experience, but you can consider questions like:

- Is my data too big to work with on a single machine?
- Can my calculations be easily parallelized?

# Using Spark in Python

==**PySpark is the Python API for Apache Spark**, an open source, distributed computing framework and set of libraries for real-time, large-scale data processing. If you're already familiar with Python and libraries such as Pandas, then PySpark is a good language to learn to create more scalable analyses and pipelines.==

The first step in using Spark is connecting to a cluster.

In practice, the cluster will be hosted on a remote machine that's connected to all other nodes. There will be one computer, called the ==master== that manages splitting up the data and the computations. The master is connected to the rest of the computers in the cluster, which are called ==worker==. The master sends the workers data and calculations to run, and they send their results back to the master.

When you're just getting started with Spark it's simpler to just run a cluster locally. Thus, for this course, instead of connecting to another computer, all computations will be run on DataCamp's servers in a simulated cluster.

Creating the connection is as simple as creating an instance of the `SparkContext` class. The class constructor takes a few optional arguments that allow you to specify the attributes of the cluster you're connecting to.

An object holding all these attributes can be created with the `SparkConf()` constructor. Take a look at the [documentation](http://spark.apache.org/docs/2.1.0/api/python/pyspark.html) for all the details!

```python
# Verify SparkContext
print(SparkContext)

# Print Spark version
print(SparkContext.version)
```

## DataFrames

Spark's core data structure is the Resilient Distributed Dataset (RDD). This is a low level object that lets Spark work its magic by splitting data across multiple nodes in the cluster. However, RDDs are hard to work with directly, so we'll be using the Spark DataFrame abstraction built on top of RDDs.

==The Spark DataFrame was designed to behave a lot like a SQL table== (a table with variables in the columns and observations in the rows). Not only are they easier to understand, DataFrames are also more optimized for complicated operations than RDDs.

When you start modifying and combining columns and rows of data, there are many ways to arrive at the same result, but some often take much longer than others. ==When using RDDs, it's up to the data scientist to figure out the right way to optimize the query, but the DataFrame implementation has much of this optimization built in==

To start working with Spark DataFrames, you first have to create a `SparkSession` object from your `SparkContext`. You can think of ==the `SparkContext` as your connection to the cluster== and ==the `SparkSession` as your interface with that connection.==

==Which of the following is an advantage of Spark DataFrames over RDDs?==

Operations using DataFrames are automatically optimized.

Exactly! This is another way DataFrames are like SQL tables.

# Creating a SparkSession

We've already created a `SparkSession` for you called `spark`, but what if you're not sure there already is one? 

Creating multiple `SparkSession`s and `SparkContext`s can cause issues, so it's best practice to use the `SparkSession.builder.getOrCreate()` method. This returns an existing `SparkSession` if there's already one in the environment, or creates a new one if necessary!

```python
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession

# Create my_spark
my_spark = SparkSession.builder.getOrCreate()

# Print my_spark
print(my_spark)
```

# Viewing tables

Once you've created a `SparkSession`, you can start poking around to see what data is in your cluster!

Your `SparkSession.catalog` which lists all the data inside the cluster. This attribute has a few methods for extracting different pieces of information.

One of the most useful is the `.listTables()` method, which returns the names of all the tables in your cluster as a list.

```python
# Print the tables in the catalog
print(spark.catalog.listTables())

# [Table(name='flights', database=None, description=None, tableType='TEMPORARY', isTemporary=True)]
```

# Are you query-ious?

==One of the advantages of the DataFrame interface is that you can run SQL queries on the tables in your Spark cluster.==

This table contains a row for every flight that left Portland International Airport (PDX) or Seattle-Tacoma International Airport (SEA) in 2014 and 2015.

Running a query on this table is as easy as using the `.sql()` method on your `SparkSession`. This method takes a string containing the query and returns a DataFrame with the results!

If you look closely, you'll notice that the table `flights` is only mentioned in the query, not as an argument to any of the methods. This is because there isn't a local object in your environment that holds that data, so it wouldn't make sense to pass the table as an argument.

```python
# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()
```

# Pandafy a Spark DataFrame

Suppose you've run a query on your huge dataset and aggregated it down to something a little more manageable.

Sometimes it makes sense to then take that table and work with it locally using a tool like `pandas`. Spark DataFrames make that easy with the `.toPandas()` method. Calling this method on a Spark DataFrame returns the corresponding `pandas` DataFrame.

This time the query counts the number of flights to each airport from SEA and PDX.

```python
# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())
```

# Put some Spark in your data

Convert between Pandas DataFrame 

In the last exercise, you saw how to move data from Spark to `pandas`. However, maybe you want to go the other direction, and put a `pandas` DataFrame into a Spark cluster! The `SparkSession` class has a method for this as well.

==The `.createDataFrame()` method takes a `pandas` DataFrame and returns a Spark DataFrame.==

The output of this method is stored locally, not in the `SparkSession` catalog. This means that you can use all the Spark DataFrame methods on it, but you can't access the data in other contexts.

For example, a SQL query (using the `.sql()` method) that references your DataFrame will throw an error. To access the data in this way, you have to save it as a _temporary table_.

You can do this using the `.createTempView()` Spark DataFrame method, which takes as its only argument the name of the temporary table you'd like to register. This method registers the DataFrame as a table in the catalog, but as this table is temporary, it can only be accessed from the specific `SparkSession` used to create the Spark DataFrame.

There is also the method `.createOrReplaceTempView()`. This safely creates a new temporary table if nothing was there before, or updates an existing table if one was already defined. You'll use this method to avoid running into problems with duplicate tables.

Check out the diagram to see all the different ways your Spark data structures interact with each other.

![[Pasted image 20240823155507.png]]

```python
# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp)

# Examine the tables in the catalog
print(spark.catalog.listTables())

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")

# Examine the tables in the catalog again
print(spark.catalog.listTables())

# []
# [Table(name='temp', database=None, description=None, tableType='TEMPORARY', isTemporary=True)]
```

# Dropping the middle man

Now you know how to put data into Spark via `pandas`, but you're probably wondering why deal with `pandas` at all? Wouldn't it be easier to just read a text file straight into Spark? Of course it would!

The`SparkSession` has a `.read` attribute which has several methods for reading different data sources into Spark DataFrames. Using these you can create a DataFrame from a .csv file just like with regular `pandas` DataFrames!

The variable `file_path` is a string with the path to the file `airports.csv`. This file contains information about different airports all over the world.

```python
# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"

# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()
```

## Manipulating data

Learn about the pyspark.sql module, which provides optimized data queries to your Spark session.

# Creating columns

Learn how to use the methods defined by Spark's `DataFrame` class to perform common data operations.

Let's look at performing column-wise operations. In Spark you can do this using the `.withColumn()` method, which takes two arguments. First, a string with the name of your new column, and second the new column itself.

The new column must be an object of class `Column`. Creating one of these is as easy as extracting a column from your DataFrame using `df.colName`.

Updating a Spark DataFrame is somewhat different than working in `pandas` because the Spark DataFrame is ==immutable==. This means that it can't be changed, and so columns can't be updated in place.

All these methods return a new DataFrame. To overwrite the original DataFrame you must reassign the returned DataFrame using the method like so:

```python
df = df.withColumn("newCol", df.oldCol + 1)
```

The above code creates a DataFrame with the same columns as `df` plus a new column, `newCol`, where every entry is equal to the corresponding entry from `oldCol`, plus one

To overwrite an existing column, just pass the name of the column as the first argument!

```python
# Create the DataFrame flights
flights = spark.table("flights")

# Show the head
flights.show()

# Add duration_hrs
flights = flights.withColumn("duration_hrs", flights.air_time/60)
```

# SQL in a nutshell

As you move forward, it will help to have a basic understanding of SQL. A more in depth look can be found [here](https://www.datacamp.com/courses/intro-to-sql-for-data-science).

==A SQL query returns a table derived from one or more tables contained in a database.==

Every SQL query is made up of commands that tell the database what you want to do with the data. The two commands that every query has to contain are `SELECT` and `FROM`.

The `SELECT` command is followed by the _columns_ you want in the resulting table.

The `FROM` command is followed by the name of the table that contains those columns. The minimal SQL query is:

```
SELECT * FROM my_table;
```

The `*` selects all columns, so this returns the entire table named `my_table`.

Similar to `.withColumn()`, you can do column-wise computations within a `SELECT` statement. For example,

```
SELECT origin, dest, air_time / 60 FROM flights;
```

returns a table with the origin, destination, and duration in hours for each flight.

Another commonly used command is `WHERE`. This command filters the rows of the table based on some logical condition you specify. The resulting table contains the rows where your condition is true. For example, if you had a table of students and grades you could do:

```
SELECT * FROM students
WHERE grade = 'A';
```

to select all the columns and the rows containing information about students who got As.

==Another common database task is aggregation. That is, reducing your data by breaking it into chunks and summarizing each chunk.==

This is done in SQL using the `GROUP BY` command. This command breaks your data into groups and applies a function from your `SELECT` statement to each group.

For example, if you wanted to count the number of flights from each of two origin destinations, you could use the query

```sql
SELECT COUNT(*) FROM flights
GROUP BY origin;
```

`GROUP BY origin` tells SQL that you want the output to have a row for each unique value of the `origin` column. The `SELECT` statement selects the values you want to populate each of the columns. Here, we want to `COUNT()` every row in each of the groups.

It's possible to `GROUP BY` more than one column. When you do this, the resulting table has a row for every combination of the unique values in each column. The following query counts the number of flights from SEA and PDX to every destination airport:

```
SELECT origin, dest, COUNT(*) FROM flights
GROUP BY origin, dest;
```

The output will have a row for every combination of the values in `origin` and `dest` (i.e. a row listing each origin and destination that a flight flew to). There will also be a column with the `COUNT()` of all the rows in each group.

Remember, a more in depth look at SQL can be found [here](https://www.datacamp.com/courses/intro-to-sql-for-data-science).

---

What information would this query get? Remember the `flights` table holds information about flights that departed PDX and SEA in 2014 and 2015. Note that `AVG()` function gets the average value of a column!

```
SELECT AVG(air_time) / 60 FROM flights
GROUP BY origin, carrier;
```

# Filtering Data

The analogous operations using Spark DataFrames.

Let's take a look at the `.filter()` method. As you might suspect, this is the Spark counterpart of SQL's `WHERE` clause. The `.filter()` method takes either an expression that would follow the `WHERE` clause of a SQL expression as a string, or a Spark Column of boolean (`True`/`False`) values.

For example, the following two expressions will produce the same output:

```python
flights.filter("air_time > 120").show()
flights.filter(flights.air_time > 120).show()
```

Notice that in the first case, we pass a _string_ to `.filter()`. In SQL, we would write this filtering task as `SELECT * FROM flights WHERE air_time > 120`. Spark's `.filter()` can accept any expression that could go in the `WHERE`clause of a SQL query (in this case, `"air_time > 120"`), as long as it is passed as a string. Notice that in this case, we do not reference the name of the table in the string -- as we wouldn't in the SQL request.

In the second case, we actually pass a _column of boolean values_ to `.filter()`. Remember that `flights.air_time > 120` returns a column of boolean values that has `True` in place of those records in `flights.air_time` that are over 120, and `False` otherwise.

PySpark often provides a few different ways to get the same results.

```python
# Filter flights by passing a string
long_flights1 = flights.filter("distance > 1000")

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

# Print the data to check they're equal
long_flights1.show()
long_flights2.show()
```

# Selecting

The Spark variant of SQL's `SELECT` is the `.select()` method. This method takes multiple arguments - one for each column you want to select. These arguments can either be the column name as a string (one for each column) or a column object (using the `df.colName` syntax). When you pass a column object, you can perform operations like addition or subtraction on the column to change the data contained in it, much like inside `.withColumn()`.

The difference between `.select()` and `.withColumn()` methods is that `.select()` returns only the columns you specify, while `.withColumn()` returns all the columns of the DataFrame in addition to the one you defined. It's often a good idea to drop columns you don't need at the beginning of an operation so that you're not dragging around extra data as you're wrangling. In this case, you would use `.select()` and not `.withColumn()`.

```python
# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)

selected2.show()
```

---

Similar to SQL, you can also use the `.select()` method to perform column-wise operations. When you're selecting a column using the `df.colName` notation, you can perform any column operation and the `.select()` method will return the transformed column. For example,

```python
flights.select(flights.air_time/60)
```

returns a column of flight durations in hours instead of minutes. You can also use the `.alias()` method to rename a column you're selecting. So if you wanted to `.select()` the column `duration_hrs` (which isn't in your DataFrame) you could do

```python
flights.select((flights.air_time/60).alias("duration_hrs"))
```

The equivalent Spark DataFrame method `.selectExpr()` takes SQL expressions as a string:

```python
flights.selectExpr("air_time/60 as duration_hrs")
```

with the SQL `as` keyword being equivalent to the `.alias()` method. To select multiple columns, you can pass multiple strings.

```python
# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")
```

# Aggregating

All of the common aggregation methods, like `.min()`, `.max()`, and `.count()` are `GroupedData` methods. These are created by calling the `.groupBy()` DataFrame method. You'll learn exactly what that means in a few exercises. For now, all you have to do to use these functions is call that method on your DataFrame. For example, to find the minimum value of a column, `col`, in a DataFrame, `df`, you could do

```python
df.groupBy().min("col").show()

# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()

# Find the longest flight from SEA in terms of air time
flights.filter(flights.origin == "SEA").groupBy().max("air_time").show()

# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()

# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()
```

This creates a `GroupedData` object (so you can use the `.min()` method), then finds the minimum value in `col`, and returns it as a DataFrame.

# Grouping and Aggregating I

Part of what makes aggregating so powerful is the addition of groups. PySpark has a whole class devoted to grouped data frames: `pyspark.sql.GroupedData`, which you saw in the last two exercises.

You've learned how to create a grouped DataFrame by calling the `.groupBy()` method on a DataFrame with no arguments.

Now you'll see that when you pass the name of one or more columns in your DataFrame to the `.groupBy()` method, the aggregation methods behave like when you use a `GROUP BY` statement in a SQL query!

```python
# Group by tailnum
by_plane = flights.groupBy("tailnum")

# Number of flights each plane made
by_plane.count().show()

# Group by origin
by_origin = flights.groupBy("origin")

# Average duration of flights from PDX and SEA
by_origin.avg("air_time").show()
```

In addition to the `GroupedData` methods you've already seen, there is also the `.agg()` method. This method lets you pass an aggregate column expression that uses any of the aggregate functions from the `pyspark.sql.functions` submodule.

This submodule contains many useful functions for computing things like standard deviations. All the aggregation functions in this submodule take the name of a column in a `GroupedData` table.

Remember, a `SparkSession` called `spark` is already in your workspace, along with the Spark DataFrame `flights`. The grouped DataFrames you created in the last exercise are also in your workspace.

```python
# Import pyspark.sql.functions as F
import pyspark.sql.functions as F

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")

# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()

# Standard deviation of departure delay
by_month_dest.agg(F.stddev("dep_delay")).show()
```

# Joining

Another very common data operation is the ==join==. Joins are a whole topic unto themselves, so in this course we'll just look at simple joins. If you'd like to learn more about joins, you can take a look [here](https://www.datacamp.com/courses/joining-data-with-pandas).

A join will combine two different tables along a column that they share. This column is called the _key_. Examples of keys here include the `tailnum` and `carrier` columns from the `flights` table.

For example, suppose that you want to know more information about the plane that flew a flight than just the tail number. This information isn't in the `flights` table because the same plane flies many different flights over the course of two years, so including this information in every row would result in a lot of duplication. To avoid this, you'd have a second table that has only one row for each plane and whose columns list all the information about the plane, including its tail number. You could call this table `planes`

When you join the `flights` table to this table of airplane information, you're adding all the columns from the `planes` table to the `flights` table. To fill these columns with information, you'll look at the tail number from the `flights` table and find the matching one in the `planes` table, and then use that row to fill out all the new columns.

Now you'll have a much bigger table than before, but now every row has all information about the plane that flew that flight!

In PySpark, joins are performed using the DataFrame method `.join()`. This method takes three arguments. The first is the second DataFrame that you want to join with the first one. The second argument, `on`, is the name of the key column(s) as a string. The names of the key column(s) must be the same in each table. The third argument, `how`, specifies the kind of join to perform. In this course we'll always use the value `how="leftouter"`.

The `flights` dataset and a new dataset called `airports` are already in your workspace.

```python
# Examine the data
airports.show()

# Rename the faa column
airports = airports.withColumnRenamed("faa", "dest")

# Join the DataFrames
flights_with_airports = flights.join(airports, on="dest", how="leftouter")

# Examine the new DataFrame
flights_with_airports.show()
```

# Machine Learning Pipelines

In the next two chapters you'll step through every ==stage of the machine learning pipeline, from data intake to model evaluation==.

At the core of the `pyspark.ml` module are the `Transformer` and `Estimator` classes. Almost every other class in the module behaves similarly to these two basic classes.

`Transformer` classes have a `.transform()` method that takes a DataFrame and returns a new DataFrame; usually the original one with a new column appended. For example, you might use the class `Bucketizer` to create discrete bins from a continuous feature or the class `PCA` to reduce the dimensionality of your dataset using principal component analysis.

`Estimator` classes all implement a `.fit()` method. These methods also take a DataFrame, but instead of returning another DataFrame they return a model object. This can be something like a `StringIndexerModel` for including categorical data saved as strings in your models, or a `RandomForestModel` that uses the random forest algorithm for classification or regression.

==Which of the following is not true about machine learning in Spark?==

- ~~Spark's algorithms give better results than other algorithms.~~
- Working in Spark allows you to create reproducible machine learning pipelines.
- Machine learning pipelines in Spark are made up of Transformers and Estimators.
- PySpark uses the pyspark.ml submodule to interface with Spark's machine learning routines.

That's right! Spark is just a platform that implements the same algorithms that can be found elsewhere.

# Join the DataFrames

In the next two chapters you'll be working to ==build a model that predicts whether or not a flight will be delayed based on the flights data==. This model will also include information about the plane that flew the route, so the first step is to join the two tables: `flights` and `planes`!

- Rename the `year` column of `planes` to `plane_year` to avoid duplicate column names.
- Create a new DataFrame called `model_data` by joining the `flights` table with `planes` using the `tailnum` column as the key.

```python
# Rename year column
planes = planes.withColumnRenamed("year", "plane_year")

# Join the DataFrames
model_data = flights.join(planes, on="tailnum", how="leftouter")
```

# Data types

Before you get started modeling, it's important to know that ==Spark only handles numeric (doubles or integers) data==. That means all of the columns in your DataFrame must be either integers or decimals (called 'doubles' in Spark).

When we imported our data, we let Spark guess what kind of information each column held. Unfortunately, Spark doesn't always guess right and you can see that some of the columns in our DataFrame are strings containing numbers as opposed to actual numeric values.

To ==remedy== this, you can use the `.cast()` method in combination with the `.withColumn()` method. It's important to note that `.cast()` works on columns, while `.withColumn()` works on DataFrames.

The only argument you need to pass to `.cast()` is the kind of value you want to create, in string form. For example, to create integers, you'll pass the argument `"integer"` and for decimal numbers you'll use `"double"`.

You can put this call to `.cast()` inside a call to `.withColumn()` to overwrite the already existing column, just like you did in the previous chapter!

## String to Integer

```python
dataframe = dataframe.withColumn("col", dataframe.col.cast("new_type"))

# Cast the columns to integers
model_data = model_data.withColumn("arr_delay", model_data.arr_delay.cast("integer"))
model_data = model_data.withColumn("air_time", model_data.air_time.cast("integer"))
model_data = model_data.withColumn("month", model_data.month.cast("integer"))
model_data = model_data.withColumn("plane_year", model_data.plane_year.cast("integer"))
```

# Create a new column

In the last exercise, you converted the column `plane_year` to an integer. This column holds the year each plane was manufactured. However, your model will use the planes' _age_, which is slightly different from the year it was made!

```python
# Create the column plane_age
model_data = model_data.withColumn("plane_age", model_data.year - model_data.plane_year)
```

# Making a Boolean

Consider that you're modeling a yes or no question: is the flight late? However, your data contains the arrival delay in minutes for each flight. Thus, you'll need to create a boolean column which indicates whether the flight was late or not!

- Use the `.withColumn()` method to create the column `is_late`. This column is equal to `model_data.arr_delay > 0`.
- Convert this column to an integer column so that you can use it in your model and name it `label` (this is the default name for the response variable in Spark's machine learning routines).
- Filter out missing values (this has been done for you).

```python
# Create is_late
model_data = model_data.withColumn("is_late", model_data.arr_delay > 0)

# Convert to an integer
model_data = model_data.withColumn("label", model_data.is_late.cast("integer"))

# Remove missing values
model_data = model_data.filter("arr_delay is not NULL and dep_delay is not NULL and air_time is not NULL and plane_year is not NULL")
```

# Strings and factors

As you know, Spark requires numeric data for modeling. So far this hasn't been an issue; even boolean columns can easily be converted to integers without any trouble. ==But you'll also be using the airline and the plane's destination as features in your model==. These are coded as strings and there isn't any obvious way to convert them to a numeric data type.

Fortunately, PySpark has functions for handling this built into the `pyspark.ml.features` submodule. You can create what are called 'one-hot vectors' to represent the carrier and the destination of each flight. A ==one-hot vector== is a way of representing a categorical feature where every observation has a vector in which all elements are zero except for at most one element, which has a value of one (1).

Each element in the vector corresponds to a level of the feature, so it's possible to tell what the right level is by seeing which element of the vector is equal to one (1).

The first step to encoding your categorical feature is to create a `StringIndexer`. Members of this class are `Estimator`s that take a DataFrame with a column of strings and map each unique string to a number. Then, the `Estimator` returns a `Transformer` that takes a DataFrame, attaches the mapping to it as metadata, and returns a new DataFrame with a numeric column corresponding to the string column.

The second step is to encode this numeric column as a one-hot vector using a `OneHotEncoder`. This works exactly the same way as the `StringIndexer` by creating an `Estimator` and then a `Transformer`. The end result is a column that encodes your categorical feature as a vector that's suitable for machine learning routines!

This may seem complicated, but don't worry! All you have to remember is that you need to create a `StringIndexer` and a `OneHotEncoder`, and the `Pipeline` will take care of the rest.

# Carrier

Create a `StringIndexer` and a `OneHotEncoder` to code the `carrier` column. To do this, you'll call the class constructors with the arguments `inputCol` and `outputCol`.

The `inputCol` is the name of the column you want to index or encode, and the `outputCol` is the name of the new column that the `Transformer` should create.

```python
# Create a StringIndexer
carr_indexer = StringIndexer(inputCol="carrier", outputCol="carrier_index")

# Create a OneHotEncoder
carr_encoder = OneHotEncoder(inputCol="carrier_index", outputCol="carrier_fact")
```

# Assemble a vector

The last step in the `Pipeline` is to combine all of the columns containing our features into a single column. This has to be done before modeling can take place because every Spark modeling routine expects the data to be in this form. You can do this by storing each of the values from a column as an entry in a vector. Then, from the model's point of view, every observation is a vector that contains all of the information about it and a label that tells the modeler what value that observation corresponds to.

Because of this, the `pyspark.ml.feature` submodule contains a class called `VectorAssembler`. This `Transformer` takes all of the columns you specify and combines them into a new vector column.

- Create a `VectorAssembler` by calling `VectorAssembler()` with the `inputCols` names as a list and the `outputCol` name `"features"`.
    - The list of columns should be `["month", "air_time", "carrier_fact", "dest_fact", "plane_age"]`.

```python
# Make a VectorAssembler
vec_assembler = VectorAssembler(inputCols=["month", "air_time", "carrier_fact", "dest_fact", "plane_age"], outputCol="features")
```

# Create the pipeline

`Pipeline` is a class in the `pyspark.ml` module that combines all the `Estimators` and `Transformers` that you've already created. This lets you reuse the same modeling process over and over again by wrapping it up in one simple object. Neat, right?

```python
# Import Pipeline
from pyspark.ml import Pipeline

# Make the pipeline
flights_pipe = Pipeline(stages=[dest_indexer, dest_encoder, carr_indexer, carr_encoder, vec_assembler])
```

---
# Machine Learning & Spark

==Learn how to build Machine Learning models on large datasets using distributed computing techiniques.==

Spark is a powerful, general purpose tool for working with Big Data. Spark transparently handles the distribution of compute tasks across a cluster. This means that operations are fast, but it also allows you to focus on the analysis rather than worry about technical details. In this course you'll learn how to get data into Spark and then delve into the three fundamental Spark Machine Learning algorithms: Linear Regression, Logistic Regression/Classifiers, and creating pipelines. Along the way you'll analyse a large dataset of flight delays and spam text messages. With this background you'll be ready to harness the power of Spark and apply it on your own Machine Learning projects!

Spark is a framework for working with Big Data. In this chapter you'll cover some background about Spark and Machine Learning. You'll then find out how to connect to Spark using Python and load CSV data.

## Data in RAM


==The performance of a Machine Learning model depends on data==. In general, more data is a good thing. If an algorithm is able to train on a larger set of data, then its ability to generalize to new data will inevitably improve. However, there are some practical constraints. ==If the data can fit entirely into RAM then the algorithm can operate efficiently==. What happens when those data no longer fit into memory?

The computer will start to use ==virtual memory== and data will be ==paged== back and forth between RAM and disk. Relative to RAM access, retrieving data from disk is slow. As the size of the data grows, paging become more intense and the computer begins to spend more and more time waiting for data. ==Performance plummets==

### Data distributed across a cluster

How then do we deal with truly large datasets? One option is to distribute the problem across multiple computers in a cluster. We will divided up into partitions which are processed seperately. Ideally each data partition can fit into RAM on a single computer in the cluster. This is the approach used by Spark.
# Spark

Spark is a general purpose framework for cluster computing. It is popular for 2 main reasons

1. It's generally much faster than other Big Data technologies like Hadoop because it does most processing in memory (It mean Hadoop process data in what?)
2. It has a developer-friendly interface which hides much of the complexity of distributed computing.

![[Pasted image 20240823182005.png]]
### Components: nodes

The cluster itself consists of one or more nodes. Each node is a computer with CPU, RAM and physical storage.

### Components: cluster manager

A cluster manager allocates resources and coordinates activity across the cluster.

### Components: driver

Every application running on the Spark cluster has a driver program. Using the Spark API, the driver communicates with the cluster manager, which in turn distributes work to the nodes.

### Component: executors

On each node Spark launches an executor process which persists for the duration of the application. Work is divided up into ==tasks==, which are simply units of computation. The executors run tasks in multiple threads across the cores in a node. When working with Spark you normally don't need to worry *too* much about the details of the cluster. Spark sets up all of that infrastructure for you and handles all interactions within the cluster. However, it's still useful to know how it works under the hood.

# Characteristics of Spark

Spark is currently the most popular technology for processing large quantities of data. Not only is it able to handle enormous data volumes, but it does so very efficiently too! Also, unlike some other distributed computing technologies, developing with Spark is a pleasure.

Which of these describe Spark?

- A framework for cluster computing
- Spark does most processing in memory
- Spark has a high-level API, which conceals a lot of complexity.

# Components in a Spark Cluster

Spark is a distributed computing platform. It achieves efficiency by distributing data and computation across a cluster of computers.

A Spark cluster consists of a number of hardware and software components which work together.

Which of these is not part of a Spark cluster?

- A load balancer

A load balancer distributes work across multiple resources, preventing overload on any one resource. In Spark this function is performed by the cluster manager.

# Interacting with Spark

The connection with Spark is established by the driver, which can be written in either Java, Scala, Python or R. Each of these languages has advantages and disadvantages. Java is relatively verbose, requiring a lot of code to accomplish even simple tasks. By contrast, Scala, Python and R, are high-level languages which can accomplish much with only a small amount of code. They also offer a REPL, or Read-Evaluate-Print loop, which is crucial for interactive development. You'll be using Python.

Python doesn't talk natively to Spark, so we'll kick off by importing the pyspark module, which makes Spark functionality available in the Python interpreter. Spark is under vigorous development. Because the interface is evolving it's important to know what version you're working with. We'll be using version 2.4.1, which was released in March 2019.

## Sub-modules

In addition to the main pyspark module, there are a few sub-modules which implement different aspects of the Spark interface. There are two versions of Spark Machine Learning: mllib, which uses an unstructured representation of data in RDDs and has been deprecated, and ml which is based on a structured, tabular representation of data in DataFrames. We'll be using the latter.

- Structured Data - `pyspark.sql`
- Streaming Data - `pyspark.streaming
- Machine Learning - `pyspark.ml`

### Spark URL

With the pyspark module loaded, you are able to connect to Spark. The next thing you need to do is tell Spark where the cluster is located. Here there are two options. 

You can either connect to a remote cluster, in which case you need to specify a Spark URL, which gives the network location of the cluster's master node. The URL is composed of an IP address or DNS name and a port number. The default port for Spark is 7077, but this must still be explicitly specified. When you're figuring out how Spark works, the infrastructure of a distributed cluster can get in the way. That's why it's useful to create a local cluster, where everything happens on a single computer. This is the setup that you're going to use throughout this course. 

==Remote Cluster==

Using Spark URL: `spark://<IP address | DNS name>:<port>

Example:`spark://13.59.151.161:7077`

==Local Cluster==

- `local` - 1 core
- `local[8]` - 8 cores
- `local[*]` - all available cores

For a local cluster, you need only specify "local" and, optionally, the number of cores to use. By default, a local cluster will run on a single core. Alternatively, you can give a specific number of cores or simply use the wildcard to choose all available cores.

## Creating a SparkSession

You connect to Spark by creating a SparkSession object. The SparkSession class is found in the pyspark.sql sub-module. You specify the location of the cluster using the master() method. Optionally you can assign a name to the application using the appName() method. Finally you call the getOrCreate() method, which will either create a new session object or return an existing object. Once the session has been created you are able to interact with Spark. Finally, although it's possible for multiple SparkSessions to co-exist, it's good practice to stop the SparkSession when you're done.

```python
# Import the SparkSession class
from pyspark.sql import SparkSession

# Create SparkSession object
spark = SparkSession.builder \
                    .master('local[*]') \
                    .appName('test') \
                    .getOrCreate()

# What version of Spark?
print(spark.version)

# Terminate the cluster
spark.stop()
```

## Loading data

- Read data from a CSV file called 'flights.csv'. Assign data types to columns automatically. Deal with missing data.
- How many records are in the data?
- Take a look at the first five records.
- What data types have been assigned to the columns? Do these look correct?

## DataFrames: A refresher

Spark represents tabular data using the DataFrame class. The data are captured as rows (or "records"), each of which is broken down into one or more columns (or "fields"). Every column has a name and a specific data type. Some selected methods and attributes of the DataFrame class are listed here. The count() method gives the number of rows. The show() method will display a subset of rows. The printSchema() method and the dtypes attribute give different views on column types. This is really scratching the surface of what's possible with a DataFrame. You can find out more by consulting the extensive documentation.

```python
# Read data from CSV file
flights = spark.read.csv('flights.csv',
                         sep=',',
                         header=True,
                         inferSchema=True, # Deduce column data types from data
                         nullValue='NA') # Placeholder for missing data

# Get number of records
print("The data contain %d records." % flights.count())

# View the first five records
flights.show(5)

# Check column data types
print(flights.dtypes)
```

```python
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

# Specify column names and types
schema = StructType([
    StructField("id", IntegerType()),
    StructField("text", StringType()),
    StructField("label", IntegerType())
])

# Load data from a delimited file
sms = spark.read.csv("sms.csv",
					 sep=';',
					 header=False,
					 schema=schema) # Explicit column data types

# Print schema of DataFrame or check column types
sms.printSchema()
```

Excellent! You now know how to initiate a Spark session and load data. In the next chapter you'll use the data you've just loaded to build a classification model.

# Data Preperation

- Dropping column or select column
- Filtering out missing data or mulating columns
- Indexing categorical data
- Assembling columns

The final step in preparing the cars data is to consolidate the various input columns into a single column. This is necessary because ==the Machine Learning algorithms in Spark operate on a single vector of predictors==, although each element in that vector may consist of multiple values. To illustrate the process you'll start with just a pair of features, cylinders and size. First you create an instance of the VectorAssembler class, providing it with the names of the columns that you want to consolidate and the name of the new output column. The assembler is then used to transform the data. Taking a look at the relevant columns you see that the new "features" column consists of values from the cylinders and size columns consolidated into a vector. Ultimately you are going to assemble all of the predictors into a single column.

```python
from pyspark.sql.functions import round
from pyspark.ml.feature import StringIndexer
from pyspark.ml.feature import VectorAssembler

# Remove the 'flight' column
flights_drop_column = flights.drop('flight')

# Number of records with missing 'delay' values
flights_drop_column.filter('delay IS NULL').count()

# Remove records with missing 'delay' values
flights_valid_delay = flights_drop_column.filter('delay IS NOT NULL')

# Remove records with missing values in any column and get the number of remaining rows
flights_none_missing = flights_valid_delay.dropna()
print(flights_none_missing.count())

# Convert 'mile' to 'km' and drop 'mile' column (1 mile is equivalent to 1.60934 km)
flights_km = flights.withColumn('km', round(flights.mile * 1.60934, 0)).drop('mile')

# Create 'label' column indicating whether flight delayed (1) or not (0)
flights_km = flights_km.withColumn('label', (flights_km.delay >= 15).cast('integer'))

# Create an indexer
indexer = StringIndexer(inputCol='carrier', outputCol='carrier_idx')

# Indexer identifies categories in the data
indexer_model = indexer.fit(flights)

# Indexer creates a new column with numeric index values
flights_indexed = indexer_model.transform(flights)

# Repeat the process for the other categorical feature
flights_indexed = StringIndexer(inputCol='org', outputCol='org_idx').fit(flights_indexed).transform(flights_indexed)

# Create an assembler object
assembler = VectorAssembler(
	inputCols=['mon', 'dom', 'dow', 'carrier_idx', 'org_idx', 'km', 'depart', 'duration'],
	outputCol='features'
)

# Consolidate predictor columns
flights_assembled = assembler.transform(flights)

# Check the resulting column
flights_assembled.select('features', 'delay').show(5, truncate=False)
```

```python
# Split into training and testing sets in a 80:20 ratio
flights_train, flights_test = flights.randomSplit([0.8, 0.2], seed=43)

# Check that training set has around 80% of records
training_ratio = flights_train.count() / flights.count()
print(training_ratio)
```

# Test vs. Train

After you've cleaned your data and gotten it ready for modeling, one of the most important steps is to split the data into a _test set_ and a _train set_. After that, don't touch your test data until you think you have a good model! As you're building models and forming hypotheses, you can test them on your training data to get an idea of their performance.

Once you've got your favorite model, you can see how well it predicts the new data in your test set. This never-before-seen data will give you a much more realistic idea of your model's performance in the real world when you're trying to predict or classify new data.

In Spark it's important to make sure you split the data **after** all the transformations. This is because operations like `StringIndexer` don't always produce the same index even when given the same list of strings.

# Transform the data

Hooray, now you're finally ready to pass your data through the `Pipeline` you created!

```python
# Fit and transform the data
piped_data = flights_pipe.fit(model_data).transform(model_data)
```

# Split the data

Now that you've done all your manipulations, the last step before modeling is to split the data!

- Use the DataFrame method `.randomSplit()` to split `piped_data` into two pieces, `training` with 60% of the data, and `test` with 40% of the data by passing the list `[.6, .4]` to the `.randomSplit()` method.

```python
# Split the data into training and test sets
training, test = piped_data.randomSplit([.6, .4])
```

# Model

```python
# Import the Decision Tree Classifier class
from pyspark.ml.classification import DecisionTreeClassifier

# Create a classifier object and fit to the training data
tree = DecisionTreeClassifier()
tree_model = tree.fit(flights_train)

# Create predictions for the testing data and take a look at the predictions
prediction = tree_model.transform(flights_test)
prediction.select('label', 'prediction', 'probability').show(5, False)
```

# Model tuning and selection

In this last chapter, you'll apply what you've learned to create a model that predicts which flights will be delayed.

# Create the modeler

The `Estimator` you'll be using is a `LogisticRegression` from the `pyspark.ml.classification` submodule.

```python
# Import LogisticRegression
from pyspark.ml.classification import LogisticRegression

# Create a LogisticRegression Estimator
lr = LogisticRegression()
```

# Cross validation

Tuning logistic regression model using a procedure called ==k-fold cross validation==. This is a method of estimating the model's performance on unseen data (like your `test` DataFrame).

It works by splitting the training data into a few different partitions. The exact number is up to you, but in this course you'll be using PySpark's default value of three. Once the data is split up, one of the partitions is set aside, and the model is fit to the others. Then the error is measured against the held out partition. This is repeated for each of the partitions, so that every block of data is held out and used as a test set exactly once. Then the error on each of the partitions is averaged. This is called the ==cross validation error== of the model, and is a good estimate of the actual error on the held out data.

You'll be using cross validation to choose the hyperparameters by creating a grid of the possible pairs of values for the two hyperparameters, `elasticNetParam` and `regParam`, and using the cross validation error to compare all the different models so you can choose the best one!

# Create the evaluator

The first thing you need when doing cross validation for model selection is a way to compare different models. Luckily, the `pyspark.ml.evaluation` submodule has classes for evaluating different kinds of models. Your model is a binary classification model, so you'll be using the `BinaryClassificationEvaluator` from the `pyspark.ml.evaluation` module.

This evaluator calculates the area under the ROC. This is a metric that combines the two kinds of errors a binary classifier can make (false positives and false negatives) into a simple number. You'll learn more about this towards the end of the chapter!

```python
# Import the evaluation submodule
import pyspark.ml.evaluation as evals

# Create a BinaryClassificationEvaluator
evaluator = evals.BinaryClassificationEvaluator(metricName="areaUnderROC")
```

# Make a grid

Next, you need to create a grid of values to search over when looking for the optimal hyperparameters. The submodule `pyspark.ml.tuning` includes a class called `ParamGridBuilder` that does just that (maybe you're starting to notice a pattern here; PySpark has a submodule for just about everything!).

You'll need to use the `.addGrid()` and `.build()` methods to create a grid that you can use for cross validation. The `.addGrid()` method takes a model parameter (an attribute of the model `Estimator`, `lr`, that you created a few exercises ago) and a list of values that you want to try. The `.build()` method takes no arguments, it just returns the grid that you'll use later.

- Call the class constructor `ParamGridBuilder()` with no arguments. Save this as `grid`.
- Call the `.addGrid()` method on `grid` with `lr.regParam` as the first argument and `np.arange(0, .1, .01)` as the second argument. This second call is a function from the `numpy` module (imported `as np`) that creates a list of numbers from 0 to .1, incrementing by .01. Overwrite `grid` with the result.
- Update `grid` again by calling the `.addGrid()` method a second time create a grid for `lr.elasticNetParam` that includes only the values `[0, 1]`.
- Call the `.build()` method on `grid` and overwrite it with the output.

```python
# Import the tuning submodule
import pyspark.ml.tuning as tune

# Create the parameter grid
grid = tune.ParamGridBuilder()

# Add the hyperparameter
grid = grid.addGrid(lr.regParam, np.arange(0, .1, .01))
grid = grid.addGrid(lr.elasticNetParam, [0, 1])

# Build the grid
grid = grid.build()
```

Awesome! That's the last ingredient in your cross validation recipe!

# Make the validator

The submodule `pyspark.ml.tuning` also has a class called `CrossValidator` for performing cross validation. This `Estimator` takes the modeler you want to fit, the grid of hyperparameters you created, and the evaluator you want to use to compare your models.

The submodule `pyspark.ml.tune` has already been imported as `tune`. You'll create the `CrossValidator` by passing it the logistic regression `Estimator` `lr`, the parameter `grid`, and the `evaluator` you created in the previous exercises.

```python
# Create the CrossValidator
cv = tune.CrossValidator(estimator=lr,
                         estimatorParamMaps=grid,
                         evaluator=evaluator
                         )
```

## Fit the model(s)

You're finally ready to fit the models and select the best one!

Unfortunately, cross validation is a very computationally intensive procedure. Fitting all the models would take too long on DataCamp.

To do this locally you would use the code:

```
# Fit cross validation models
models = cv.fit(training)

# Extract the best model
best_lr = models.bestModel
```

Remember, the training data is called `training` and you're using `lr` to fit a logistic regression model. Cross validation selected the parameter values `regParam=0` and `elasticNetParam=0` as being the best. These are the default values, so you don't need to do anything else with `lr` before fitting the model.

```python
# Call lr.fit()
best_lr = lr.fit(training)

# Print best_lr
print(best_lr)
```

# Evaluating binary classifiers

We'll be using a common metric for binary classification algorithms call the ==AUC==, or area under the curve. In this case, the curve is the ROC, or receiver operating curve. The details of what these things actually measure isn't important for this course. All you need to know is that for our purposes, the closer the AUC is to one (1), the better the model is!

```python
# Use the model to predict the test set
test_results = best_lr.transform(test)

# Evaluate the predictions
print(evaluator.evaluate(test_results))
```

Congratulations! You went from knowing nothing about Spark to doing advanced machine learning. Great job on making it to the end of the course! The next steps are learning how to create large scale Spark clusters and manage and submit jobs so that you can use models in the real world. Check out some of the other DataCamp courses that use Spark! And remember, Spark is still being actively developed, so there's new features coming all the time!

```python
# Create a confusion matrix
prediction.groupBy('label', 'prediction').count().show()

# Calculate the elements of the confusion matrix
TN = prediction.filter('prediction = 0 AND label = prediction').count()
TP = prediction.filter('prediction = 1 AND label = prediction').count()
FN = prediction.filter('prediction = 0 AND label != prediction').count()
FP = prediction.filter('prediction = 1 AND label != prediction').count()

# Accuracy measures the proportion of correct predictions
accuracy = (TN + TP) / (TN + TP + FN + FP)
print(accuracy)
```

# Ensembles & Pipelines

Finally you'll learn how to make your models more efficient. You'll find out how to use pipelines to make your code clearer and easier to maintain. Then you'll use cross-validation to better test your models and select good model parameters. Finally you'll dabble in two types of ensemble model.

```python
from pyspark.ml import Pipeline

pipeline = Pipeline(stages=[indexer, onehot, assemble, regression])

pipeline = pipeline.fit(train)
```

# Others

### Apache [Spark](Resources/Tools/Spark.md), Hadoop, Kafka

https://www.logicmonitor.com/blog/kafka-vs-spark-vs-hadoop

- Distributed Data Processing knowledge, Big Data processing (Hadoop, Spark)
- Gain experience in handling big data, including knowledge of distributed computing frameworks such as Apache Spark, to manage and process large datasets effectively.

- Cluster Management