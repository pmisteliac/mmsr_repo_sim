Github Repository Similarity Detector
--------------------------------------------------------------

MSSR Special Assignment

Group 14:

Philippe D. Misteli - 4932129

Jan Gerling - 4807367



## Dependencies:
* python 3
* gensim
* matplotlib
* sklearn
* stop_words
* nltk
* numpy


## Usage:

### Feature Extraction
1. Import the Java Project in the extractor folder into Eclipse
2. Run App.java with the JVM Arguments -Xms4g -Xmx8g -XX:UseG1GC


### Similarity Calculation
1. Open the python project in Intellij Idea
2. Install all dependencies in an environment and set this as the execution environment for the project
3. Open Experiment.py in src
4. Define the characteristics of your experiment in experiment function:
    1. Define the locations for the data corpi
    2. Define a name for your experiment (make sure there is no equally named folder in results)
    3. (Optional) in the pipeline function you can change the topic counts, distance metric etc.
5. Run the experiment in Intellij Idea
6. You can find the results of your experiment in: results/[your experiment name]
