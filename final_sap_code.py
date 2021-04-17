import numpy as np # linear algebra
#C:\Users\Yashmitha R\Downloads\SAP\SAP\StudentsPerformance.csv
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from assistant import read
import time
import matplotlib
from matplotlib import colors
import matplotlib.cm as cm
import altair as alt
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import PIL.Image
from PIL import ImageTk
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

#Importing the Necessary Libraries
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter

import warnings
warnings.filterwarnings('ignore')

file1 = open('myfile.txt', 'w')

def on_barclick(event=None):
   
    #top.destroy()
    sns.set_style('darkgrid')
    count=0
    categorical_variables = ['gender', 'parental level of education', 'lunch', 'test preparation course']
    title=["Frequency of students under male and female graph","Frequency of parents depending on educational level","Frequency of students under the lunch feature","Frequency of students under the test preparation & course completion"]
    conclusion=["Females are higher with 518","Some college educated parents are highest with 226","Standard lunch is more popular with 645","No test-preparation is higher with 642"]
    i=0
    for c in categorical_variables:
        count+=1
        if count==1:
            var = dataset[c]
            varValue = var.value_counts()
            f, ax = plt.subplots(figsize=(7, 8), dpi=90)
            ax.set_facecolor('lightgray')
            f.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
            colours=["red","#228B22"]
            plt.bar(varValue.index, varValue,width = .8,color=colours,label=conclusion[0],edgecolor='black')
            for i in range(len(varValue)):
                plt.annotate(str(varValue[i]), xy=(varValue.index[i],varValue[i]), ha='center', va='bottom') 
            plt.xticks(varValue.index, varValue.index.values,rotation=10)
            plt.xlabel(c.capitalize(),weight='bold',fontsize=20)
            plt.ylabel("Frequency",weight='bold',fontsize=20)
            plt.title(title[0],weight='bold',fontsize=15)
            plt.legend()
            plt.show(block=False)
            plt.pause(3)
            read(" The bar plot depicts the number of female students as 518 and number of male students as 482. Gender distribution can be said to be balanced.",lang)
            plt.close()
        elif count==2:
            var = dataset[c]
            # count number of categorical variable(value/sample)
            varValue = var.value_counts()
            # visualize
            f, ax = plt.subplots(figsize=(7, 8), dpi=90)
            ax.set_facecolor('lightgray')
            f.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
            colours=[]
            for i in range(len(varValue)):
                if (varValue[i]>500 or varValue[i]==226):
                    colours.append("red")
            for i in ["c","blue","pink","yellow","#F1AB00"]:
                colours.append(i)
            plt.bar(varValue.index, varValue,width = .8,color=colours,label=conclusion[1],edgecolor='black')
            for i in range(len(varValue)):
                plt.annotate(str(varValue[i]), xy=(varValue.index[i],varValue[i]), ha='center', va='bottom') 
            plt.xticks(varValue.index, varValue.index.values,rotation=10)
            plt.xlabel(c.capitalize(),weight='bold',fontsize=20)
            plt.ylabel("Frequency",weight='bold',fontsize=20)
            plt.title(title[1],weight='bold',fontsize=15)
            plt.legend()
            plt.show(block=False)
            plt.pause(3)
            read("The bar plot indicates that the education level of the parents is not evenly distributed. It also indicates that the parents with a Master's degree are in the minority, and the ones with Some College are in the majority.",lang)
            plt.close()
        elif count==3:
            var = dataset[c]
            # count number of categorical variable(value/sample)
            varValue = var.value_counts()
            # visualize
            f, ax = plt.subplots(figsize=(7, 8), dpi=90)
            ax.set_facecolor('lightgray')
            f.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
            colours=["red","#00bfff"]
            plt.bar(varValue.index, varValue,width = .8,color=colours,label=conclusion[2],edgecolor='black')
            for i in range(len(varValue)):
                plt.annotate(str(varValue[i]), xy=(varValue.index[i],varValue[i]), ha='center', va='bottom') 
            plt.xticks(varValue.index, varValue.index.values,rotation=10)
            plt.xlabel(c.capitalize(),weight='bold',fontsize=20)
            plt.ylabel("Frequency",weight='bold',fontsize=20)
            plt.title(title[2],weight='bold',fontsize=15)
            plt.legend()
            plt.show(block=False)
            plt.pause(3)
            read("In the 'lunch' feature, it can be said that the 'standard' doubles the ‘free/reduced’ category.",lang)
            plt.close()
        else:
            var = dataset[c]
            # count number of categorical variable(value/sample)
            varValue = var.value_counts()
            # visualize
            f, ax = plt.subplots(figsize=(7, 8), dpi=90)
            ax.set_facecolor('lightgray')
            f.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
            colours=["red","#64D13E"]
            plt.bar(varValue.index, varValue,width = .8,color=colours,label=conclusion[3],edgecolor='black')
            for i in range(len(varValue)):
                plt.annotate(str(varValue[i]), xy=(varValue.index[i],varValue[i]), ha='center', va='bottom') 
            plt.xticks(varValue.index, varValue.index.values,rotation=10)
            plt.xlabel(c.capitalize(),weight='bold',fontsize=20)
            plt.ylabel("Frequency",weight='bold',fontsize=20)
            plt.title(title[3],weight='bold',fontsize=15)
            plt.legend()
            plt.show(block=False)
            plt.pause(3)
            read("The plot depicts that 642 students did not take test preparation courses while 358 of them did.",lang)
            plt.close()
def plot_hist(variable):
    fig, ax = plt.subplots(1, 1,figsize =(9, 5) ,tight_layout = True)
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    # Creating histogram
    N, bins, patches = ax.hist(dataset[variable], bins = 50,density=True)
    # Setting color
    fracs = N / N.max()
    norm = colors.Normalize(fracs.min(), fracs.max())
    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)
    # Make some labels.
    rects = ax.patches
    labels = [i for i in range(len(rects))]
    for rect, label in zip(rects, labels):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2, height+0.0001, label,ha='center', va='bottom',fontsize=5)
    plt.xlabel(variable.capitalize(),weight='bold',fontsize=15)
    plt.ylabel("Frequency",weight='bold',fontsize=15)
    plt.title("{} distribution".format(variable.capitalize()),weight='bold',fontsize=15)
    plt.show(block=False)
    plt.pause(3)
def on_histclick(event=None):    
    val=0
    numerical_variables = ['math score', 'reading score', 'writing score']
    for n in numerical_variables:
        plot_hist(n)
        val+=1
        if val==1:
            read(" In the 'math score', there is an accumulation in the range of 60-80.",lang)
        elif val==2:
            read("There is no congestion in reading score like math. It can be said that the grade of the majority varies between 75-80.",lang)
        else:
            read("The distribution in the 'writing score' feature is like in reading score.",lang)
        plt.close()

def on_compclick(event=None):
    #gender
    global ax
    dataset[["gender","math score"]].groupby(["gender"], as_index = False).mean().sort_values(by="math score",ascending = False)
    dataset[["gender","reading score"]].groupby(["gender"], as_index = False).mean().sort_values(by="reading score",ascending = False)
    dataset[["gender","writing score"]].groupby(["gender"], as_index = False).mean().sort_values(by="writing score",ascending = False)
    race_math = dataset[["gender","math score"]].groupby(["gender"], as_index = False).mean()
    race_writing = dataset[["gender","writing score"]].groupby(["gender"], as_index = False).mean()
    race_reading = dataset[["gender","reading score"]].groupby(["gender"], as_index = False).mean()
    fig, ax = plt.subplots(figsize =(9, 8) ,tight_layout = True,dpi=80)
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    sns.set_theme(style="darkgrid")
    plt.title('Math - Reading - Writing Scores according to Gender', fontweight='bold', size = 15)
    barWidth = 0.25
    bars1 = race_math['math score']
    bars2 = race_writing['writing score']
    bars3 = race_reading['reading score']
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
    r4 = [x + barWidth for x in r3]
    rects1=plt.bar(r1, bars1, color='#09FF00', width=barWidth, edgecolor='white', label='Math score', yerr=0.3,ecolor="black",capsize=10)
    rects2=plt.bar(r2, bars2, color='#FF0067', width=barWidth, edgecolor='white', label='Writing score', yerr=0.5,ecolor="black",capsize=10, alpha = .50)
    rects3=plt.bar(r3, bars3, color='#009FFF', width=barWidth, edgecolor='white', label='Reading score', yerr=0.5,ecolor="black",capsize=10,hatch = '-')
    modelNames = race_math['gender']    
    plt.xlabel('Gender', fontweight='bold', fontsize = 15)
    plt.ylabel('Scores', fontweight='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(bars1))], modelNames, rotation = 0, size = 24)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    plt.legend()
    plt.show(block=False)
    plt.pause(3)
    read("With respect to gender, the female students have a higher average in reading and writing than the male students. The male students have a higher average in maths.",lang)
    plt.close()
    #parental level of education
    dataset[["parental level of education","math score"]].groupby(["parental level of education"], as_index = False).mean().sort_values(by="math score",ascending = False)
    dataset[["parental level of education","reading score"]].groupby(["parental level of education"], as_index = False).mean().sort_values(by="reading score",ascending = False)
    dataset[["parental level of education","writing score"]].groupby(["parental level of education"], as_index = False).mean().sort_values(by="writing score",ascending = False)

    race_math = dataset[["parental level of education","math score"]].groupby(["parental level of education"], as_index = False).mean()
    race_writing = dataset[["parental level of education","writing score"]].groupby(["parental level of education"], as_index = False).mean()
    race_reading = dataset[["parental level of education","reading score"]].groupby(["parental level of education"], as_index = False).mean()
    fig, ax = plt.subplots(figsize =(9, 8) ,tight_layout = True,dpi=80)
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    plt.title('Math - Reading - Writing Scores according to Parental Level of Education', fontweight='bold', fontsize = 15)
    barWidth = 0.25
    bars1 = race_math['math score']
    bars2 = race_writing['writing score']
    bars3 = race_reading['reading score']
 
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
 
    rects1=plt.bar(r1, bars1, color='#E2D810', width=barWidth, edgecolor='white', label='math score', yerr=0.5,ecolor="black",capsize=10)
    rects2=plt.bar(r2, bars2, color='#D9138A', width=barWidth, edgecolor='white', label='writing score', yerr=0.5,ecolor="black",capsize=10, alpha = .50)
    rects3=plt.bar(r3, bars3, color='#12A4D9', width=barWidth, edgecolor='white', label='reading score', yerr=0.5,ecolor="black",capsize=10, hatch = '-')
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    modelNames = race_math['parental level of education']
    plt.xlabel('Parental Level of Education', fontweight='bold', fontsize = 15)
    plt.ylabel('Scores', fontweight='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(bars1))], modelNames, rotation = 10, fontsize = 10) 
    plt.legend()
    plt.show(block=False)
    plt.pause(3)
    read("From the plot,we come to an understanding that the average of students whose parents have completed a Master is the highest in all tests. The lowest averages are those whose parents have High school degree. However, here, too, it is necessary to consider the size of the sample set. While there are 59 samples in Master's Degree, there are 196 samples in the 'High School' set. ",lang)
    plt.close()


    #lunch
    dataset[["lunch","math score"]].groupby(["lunch"], as_index = False).mean().sort_values(by="math score",ascending = False)
    dataset[["lunch","reading score"]].groupby(["lunch"], as_index = False).mean().sort_values(by="reading score",ascending = False)
    dataset[["lunch","writing score"]].groupby(["lunch"], as_index = False).mean().sort_values(by="writing score",ascending = False)
    race_math = dataset[["lunch","math score"]].groupby(["lunch"], as_index = False).mean()
    race_writing = dataset[["lunch","writing score"]].groupby(["lunch"], as_index = False).mean()
    race_reading = dataset[["lunch","reading score"]].groupby(["lunch"], as_index = False).mean()
    fig, ax = plt.subplots(figsize =(9, 8) ,tight_layout = True,dpi=80)
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    plt.title('Math - Reading - Writing Scores according to Lunch feature', fontweight='bold', fontsize = 15)
    barWidth = 0.25
    bars1 = race_math['math score']
    bars2 = race_writing['writing score']
    bars3 = race_reading['reading score']
 
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
 
    rects1=plt.bar(r1, bars1, color='#00DD9B', width=barWidth, edgecolor='white', label='math score', yerr=0.5,ecolor="black",capsize=10)
    rects2=plt.bar(r2, bars2, color='#0C5578', width=barWidth, edgecolor='white', label='writing score', yerr=0.5,ecolor="black",capsize=10, alpha = .50)
    rects3=plt.bar(r3, bars3, color='#FFB600', width=barWidth, edgecolor='white', label='reading score', yerr=0.5,ecolor="black",capsize=10, hatch = '-')
 
    modelNames = race_math['lunch']
    
    plt.xlabel('Lunch', fontweight='bold', fontsize = 15)
    plt.ylabel('Scores', fontweight='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(bars1))], modelNames, rotation = 0, size = 24)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    plt.legend()
    plt.show(block=False)
    plt.pause(3)
    read("The plot depicts that the 'standard' ones in the 'lunch' feature appear to be more successful than the 'free/reduced' ones.",lang)
    plt.close()

    #test preparation course

    dataset[["test preparation course","math score"]].groupby(["test preparation course"], as_index = False).mean().sort_values(by="math score",ascending = False)
    dataset[["test preparation course","reading score"]].groupby(["test preparation course"], as_index = False).mean().sort_values(by="reading score",ascending = False)
    dataset[["test preparation course","writing score"]].groupby(["test preparation course"], as_index = False).mean().sort_values(by="writing score",ascending = False)

    race_math = dataset[["test preparation course","math score"]].groupby(["test preparation course"], as_index = False).mean()
    race_writing = dataset[["test preparation course","writing score"]].groupby(["test preparation course"], as_index = False).mean()
    race_reading = dataset[["test preparation course","reading score"]].groupby(["test preparation course"], as_index = False).mean()

    fig, ax = plt.subplots(figsize =(9, 8) ,tight_layout = True,dpi=80)
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    plt.title('Math - Reading - Writing Scores according to Test Preparation Course Completion', fontweight='bold', size =15)

    barWidth = 0.25
 
    bars1 = race_math['math score']
    bars2 = race_writing['writing score']
    bars3 = race_reading['reading score']
 
    r1 = np.arange(len(bars1))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]
 
    rects1=plt.bar(r1, bars1, color='#CC41FF', width=barWidth, edgecolor='white', label='math score', yerr=0.5,ecolor="black",capsize=10)
    rects2=plt.bar(r2, bars2, color='#05BBAA', width=barWidth, edgecolor='white', label='writing score', yerr=0.5,ecolor="black",capsize=10, alpha = .50)
    rects3=plt.bar(r3, bars3, color='#EB5951', width=barWidth, edgecolor='white', label='reading score', yerr=0.5,ecolor="black",capsize=10, hatch = '-')
 
    modelNames = race_math['test preparation course']
    
    plt.xlabel('Test Preparation Course', fontweight='bold', size = 15)
    plt.ylabel('Scores', fontweight='bold', size =15)
    plt.xticks([r + barWidth for r in range(len(bars1))], modelNames, rotation = 0, weight="bold",size = 10)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3) 
    plt.legend()
    plt.show(block=False)
    plt.pause(3)
    read("The plot clearly indicates that those who completed test preparation course scored higher than who did not.",lang)
    plt.close()
def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(round(height,2)),xy=(rect.get_x() + rect.get_width() / 2, height),xytext=(0, 3),textcoords="offset points",ha='center', va='bottom')
            
def detect_outliers(df,features):
    outlier_indices = []
    
    for c in features:
        # 1st quartile
        Q1 = np.percentile(df[c],25)
        # 3rd quartile
        Q3 = np.percentile(df[c],75)
        # IQR
        IQR = Q3 - Q1
        # Outlier step
        outlier_step = IQR * 1.5
        # detect outlier and their indeces
        outlier_list_col = df[(df[c] < Q1 - outlier_step) | (df[c] > Q3 + outlier_step)].index
        # store indeces
        outlier_indices.extend(outlier_list_col)
    
    outlier_indices = Counter(outlier_indices)
    multiple_outliers = list(i for i, v in outlier_indices.items() if v > 2)
    
    return multiple_outliers

def on_pieclick(event=None):
    dataset.loc[detect_outliers(dataset,['math score', 'reading score', 'writing score'])]
    # drop outliers
    #train_df = train_df.drop(detect_outliers(train_df,["Age","SibSp","Parch","Fare"]),axis = 0).reset_index(drop = True)
    #Visualization
    #labels = dataset['gender'].value_counts().index
    sizes = dataset['gender'].value_counts().values
    fig, ax = plt.subplots(figsize =(5, 5) ,tight_layout = True,dpi=130)
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    plt.pie(sizes, labels=["Female","Male"], colors = ["#FF2281","#87CEFA"], autopct='%1.1f%%')
    plt.title('Distribution of Students by Gender',color = 'black',fontsize = 10, weight = "bold")
    plt.pause(3)
    read("This graphic shows the distribution of samples according to their gender.",lang)
    plt.close()
def on_violinclick(event=None):
    """Violin Plot :A Violin Plot is used to visualize the distribution and probability density of the data. The thick black bar in the middle represents the interquartile range; The vertically extended thin black line represents 95% confidence intervals and the white point is the media.
    """

    plt.figure(figsize=(20,15))
    sns.set_theme(style="darkgrid")
    plt.suptitle('Scores with respect to Gender', fontsize=14, fontweight='bold')

    plt.subplot(2,3,1)
    my_pal = {'female':'r', 'male':'b'}
    ax1 = sns.violinplot(x = 'gender', y = 'math score', data = dataset, palette = my_pal)
    ax1.set(xlabel = "Gender", ylabel = "Math Score", title = "Gender vs Math Score")
    ax1.set_xticklabels(['Females','Males'])


    plt.subplot(2,3,2)
    my_pal1 = {'female':'pink', 'male':'deepskyblue'}
    ax2 = sns.violinplot(x = 'gender', y = 'reading score', data = dataset, palette = my_pal1)
    ax2.set(xlabel = "Gender", ylabel = "Reading Score", title = "Gender vs Reading Score")
    ax2.set_xticklabels(['Females','Males'])

    plt.subplot(2,3,3)
    my_pal2 = {'female':'coral','male':'lightgreen'}
    ax3 = sns.violinplot(x = 'gender', y = 'writing score', data = dataset, palette = my_pal2)
    ax3.set(xlabel = "Gender", ylabel = "Writing Score", title = "Gender vs Writing Score")
    ax3.set_xticklabels(['Females','Males'])
    plt.pause(3)
    read("With these graphs, we see the distribution of the scores of men and women.For the Math Score: Bloating is in almost the same location, but female show a line to under 20. It ends around 20 in male.For Reading Score: There is an accumulation of 70-80 in females. In males, the notes are more evenly spread.For Writing Score: It can be seen that the average of females is significantly higher than that of males.",lang)
    plt.close()
                            
def on_boxenclick(event=None):
    #Boxen plot
    """
    The Boxen plot is very similar to box plot, except for the fact that it plots different quartile values. By plotting different quartile values, we are able to understand the shape of the distribution particularly in the head end and tail end.
    Source for this explanation: https://madhuramiah.medium.com/some-interesting-visualizations-with-seaborn-python-ad207f50b844#:~:text=The%20Boxen%20plot%20is%20very,head%20end%20and%20tail%20end.
    """

    import seaborn as sns
    sns.set_theme(style="darkgrid")

    fig, ax = plt.subplots(figsize =(14, 8) ,tight_layout = True,dpi=110)
    fig.suptitle('Distribution of Students score by Lunch', fontsize=14, fontweight='bold')
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))

    plt.subplot(3,3,1)
    sns.boxenplot(x=dataset["lunch"], y=dataset["math score"], hue="lunch",scale="linear",
              data=dataset)

    plt.subplot(3,3,3)
    sns.boxenplot(x=dataset['lunch'], y=dataset['reading score'], hue="lunch", scale="linear", data=dataset)

    plt.subplot(3,3,5)
    sns.boxenplot(x=dataset['lunch'], y=dataset['writing score'], hue="lunch", scale="linear", data=dataset)

    plt.pause(3)
    read("These plots show the change of the Score according to the 'lunch' feature. In general, the 'standard' ones appear to have higher scores.",lang)
    plt.close()
def on_swarmclick(event=None):
    #swarmplot
    import seaborn as sns
    sns.set_theme(style="darkgrid")

    fig, ax = plt.subplots(figsize =(14, 8) ,tight_layout = True,dpi=110)
    fig.suptitle('3D Distribution of Student scores with respect to test preparation course & parental level of education', fontsize=14, fontweight='bold')
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))
    
    plt.subplot(1,3,1)
    sns.swarmplot(x="test preparation course", y="math score",hue="parental level of education", data=dataset, palette="PRGn")

    plt.subplot(1,3,2)
    sns.swarmplot(x="test preparation course", y="reading score",hue="parental level of education", data=dataset, palette="PRGn")

    plt.subplot(1,3,3)
    sns.swarmplot(x="test preparation course", y="writing score",hue="parental level of education", data=dataset, palette="PRGn")

    plt.show(block=False)
    plt.pause(3)
    read("From the graphs we can come to a conclusion that if the parents have a bachelor’s degree, master’s degree or some college level education ,whether the student takes up the test preparation course or not, they seem to score higher. Taking the test preparation course increases the number of students who have a high score with the above mentioned parental education qualifications.",lang)
    plt.close()
def on_jointclick(event=None):
    """
    Draw a plot of two variables with bivariate and univariate graphs.

    This function provides a convenient interface to the JointGrid class, with several canned plot kinds. This is intended to be a fairly lightweight wrapper; if you need more flexibility, you should use JointGrid directly.

    Source: http://seaborn.pydata.org/generated/seaborn.jointplot.html  
    """

    dataset['overall'] = (dataset['math score'] + dataset['reading score'] + dataset['writing score'])/3

    """
    Why did I create an 'overall' column?

    I got the average of reading, writing and math scores to see the students' success in all tests in a single variable. In the following graphs, I will compare 'overall' to other scores.
    """
    sns.set_theme(style="darkgrid")
    plt.rcParams['axes.facecolor'] = 'silver'
    ax2 = sns.jointplot(x = dataset['math score'], y = dataset['overall'], kind = 'hex', size=7,color="#FFAA01").set_axis_labels('Math Score',"Overall Score")
    ax2.fig.suptitle("Relationship between the overall score and math score", weight = "bold")
    ax2.fig.subplots_adjust(top=0.95)
    plt.show(block=False)
    plt.pause(3)
    read("As per the dataset, there is a linear relationship between the overall - math score. It is observed that the largest concentration is between 60-80.",lang)
    plt.close()

    #As expected, there is a linear relationship between the overall - math score. It is observed that the largest concentration is between 60-80.
    #plt.suptitle('Relationship between the overall score and reading score', fontsize=14, fontweight='bold')
    plt.rcParams['axes.facecolor'] = 'silver'
    ax1 = sns.jointplot(x = dataset['reading score'], y = dataset['overall'],kind="kde", cmap = cm.jet, size=7,marginal_kws={'lw':3,'color':'black'}).set_axis_labels('Reading Score',"Overall Score")
    ax1.fig.suptitle("Relationship between the overall score and reading score", weight = "bold")
    ax1.fig.subplots_adjust(top=0.95)
    plt.show(block=False)
    plt.pause(3)
    read("The joint plot shows that the points where the lines are concentrated show that there are more students in the grade range Between 60-80.",lang)
    plt.close()

    #Another kind of Joint Plot. The points where the lines are concentrated show that there are more students in that grade range. Between 60-80.
    p=sns.jointplot(x = dataset['writing score'], y = dataset['overall'],color="#FF2079", kind="reg", size=7,marginal_kws={'lw':3,'color':'black'}).set_axis_labels('Writing Score',"Overall Score")
    p.ax_marg_x.set_facecolor('#ccffccaa')
    p.ax_marg_y.set_facecolor('#ccffccaa')
    p.fig.suptitle("Relationship between the overall score and writing score", weight = "bold")
    p.fig.subplots_adjust(top=0.95)
    plt.show(block=False)
    plt.pause(3)
    read("In this graph, as in the others, a linear increase is observed between 'overall' and any Score value. The distribution of students seems balanced between 50-85.",lang)
    plt.close()
def on_swarmclick(event=None):                     
    #swarmplot

    import seaborn as sns
    sns.set_theme(style="darkgrid")

    fig, ax = plt.subplots(figsize =(14, 8) ,tight_layout = True,dpi=110)
    fig.suptitle('3D Distribution of Student scores with respect to test preparation course & parental level of education', fontsize=14, fontweight='bold')
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))

    plt.subplot(1,3,1)
    sns.swarmplot(x="test preparation course", y="math score",hue="parental level of education", data=dataset, palette="PRGn")

    plt.subplot(1,3,2)
    sns.swarmplot(x="test preparation course", y="reading score",hue="parental level of education", data=dataset, palette="PRGn")

    plt.subplot(1,3,3)
    sns.swarmplot(x="test preparation course", y="writing score",hue="parental level of education", data=dataset, palette="PRGn")

    plt.show(block=False)
    plt.pause(3)
    read("From the graphs we can come to a conclusion that if the parents have a bachelor’s degree, master’s degree or some college level education ,whether the student takes up the test preparation course or not, they seem to score higher. Taking the test preparation course increases the number of students who have a high score with the above mentioned parental education qualifications.",lang)
    plt.close()
def on_overallclick(event=None):
    #Bar plot

    """
    The Classic Bar Plot is useful for distinguishing between categories and showing numerical comparisons using horizontal or vertical columns. One axis of the chart shows the categories being compared, and the other axis shows a scale of values.
    Bar plots differ from Histograms in that they do not show continuous and continuous improvements over a period of time. The discrete data of the Bar Plot are categorical data and therefore "How many?" gives an answer to the question.
    Major mistake made in Bar Plot makes definitions problematic as there are too many columns.
    """

    counts = dataset['parental level of education'].value_counts()

    f, ax = plt.subplots(figsize=(9, 8), dpi=90)
    ax.set_facecolor('white')
    f.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    sns.barplot(x=counts.index, y=counts.values, palette="rocket" )

    plt.ylabel('Number of Degree',fontsize=15,weight="bold")
    plt.xlabel('Degrees', style = 'normal',fontsize=15,weight="bold")

    plt.xticks(rotation = 10, size = 10)
    plt.yticks(rotation = 10, size = 10)
    
    plt.title('Distribution of Parental Level of Education',color = 'black',fontsize=15,weight="bold")
    plt.show(block=False)
    plt.pause(3)
    read("This chart shows the distribution of the Parental Level of Education.",lang)
    plt.close()

#   This chart shows the distribution of the Parental Level of Education.

    #Heatmap
    """
    Heat maps visualize data with color changes. When applied to the table format, its variables are placed in rows and columns. Coloring the boxes in the table is useful for examining multivariate crosstab data. Heat maps are good for showing more than one variable, revealing any patterns or showing if any variables are alike, and detecting whether there is any correlation between them.
    """
    dataset.corr()
    f, ax = plt.subplots(figsize=(10, 6), dpi=90)
    ax.set_facecolor('white')
    f.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    lab = ['Math Score','Reading Score','Writing Score']
    ax = sns.heatmap(dataset.corr(), annot=True, cmap='viridis', linewidths = .2, xticklabels = lab, yticklabels = lab)
    plt.title("Correlation between the different subjects", weight = "bold")
    plt.show(block=False)
    plt.pause(3)
    read("It can be deduced from the chart that there is a positive correlation between reading and writing.",lang)
    plt.close()



    #Pair Plot
    """Plot pairwise relationships in a dataset.
    By default, this function will create a grid of Axes such that each numeric variable in data will by shared across the y-axes across a single row and the x-axes across a single column. The diagonal plots are treated differently: a univariate distribution plot is drawn to show the marginal distribution of the data in each column.
    It is also possible to show a subset of variables or plot different variables on the rows and columns.
    Source: https://seaborn.pydata.org/generated/seaborn.pairplot.html
    """

    f= plt.subplots()
    plt.show(block=False)
    plt.close()
    g=sns.pairplot(dataset, hue="lunch",markers=["o", "s"],height=2,palette="flare")
    g.fig.subplots_adjust(top=0.95)
    g.fig.suptitle('Pairplot of Lunch type with respect to Scores', fontsize=12, fontweight='bold')
    plt.show(block=False)
    plt.pause(3)
    read("As we have reached in previous plots and reviews, students with 'lunch' = 'standard' generally do better than others.",lang)
    plt.close()


    #How effective is the test preparation course?
    f= plt.subplots()
    plt.show(block=False)
    plt.close()
    g=sns.pairplot(dataset, hue="test preparation course",diag_kind="hist",palette="viridis",height=2,markers=["d", "s"])
    g.fig.subplots_adjust(top=0.95)
    g.fig.suptitle('Pairplot of  Scores with respect to Test Preparation', fontsize=12, fontweight='bold',color="black")
    plt.show(block=False)
    plt.pause(3)
    read("We see that the green squares with 'test preparation course' = 'completed' are higher on the graphs.",lang)
    plt.close()


    #Box plot
    dataset['overall'] = (dataset['math score'] + dataset['reading score'] + dataset['writing score'])/3
    """
    Box charts are an easy way to visually show the distribution of a quarter of the data.
    Lines running parallel to the box are known as "Whiskers" and are used to indicate variation between data above or below a quarter. Extreme values are drawn with individual points in line with the lines sometimes called whiskers. Box-Whisker charts can be drawn horizontally or vertically.
    Although box plots look very primitive compared to Histograms and density lines, they have the advantage of taking up less space, which is useful when comparing many group or dataset distributions
    """

    #Which major factors contribute to test outcomes?
    sns.set_theme(style="darkgrid", palette="pastel")       
    fig, ax = plt.subplots(figsize =(20, 10) ,tight_layout = True,dpi=70)
    fig.suptitle('The graph represents overall score with respect to all categories', fontsize=14, fontweight='bold')
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))

    plt.subplot(2,2,1)
    sns.boxplot(x="gender", y="overall", hue="test preparation course", data=dataset)
    plt.subplot(2,2,2)
    sns.boxplot(x="gender", y="overall", hue="parental level of education", data=dataset)
    plt.subplot(2,2,3)
    sns.boxplot(x="gender", y="overall", hue="lunch", data=dataset)
    sns.despine(offset=10, trim=True)
    plt.show(block=False)
    plt.pause(3)
    read("For female students, 'test preparation course' = 'completed' and 'parental level of education' = 'master's degree' and 'lunch' = 'standard' values can be shown as factors that increase success.For male students, 'test preparation course' = 'completed' and 'parental level of education' = 'master's degree' and 'lunch' = 'standard' values can be shown as factors that increase success.Since all values are equal for males and females, they can be cited as factors that increase the success of any student.",lang)
    plt.close()

def center(win):
    """
    centers a tkinter window
    :param win: the root or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()

path=""
lang=""

def execute1():
    global path
    global lang
    global dataset
    #print(e1.get())
    path=e1.get()
    lang = clicked.get()
    read("Data for storytelling!! The topic under consideration is Students Performance in Examinations in the United States of America.The dataset is a public dataset from Kaggle. The factors taken into consideration are: gender, parental level of education, lunch, test preparation score, math score, reading score and writing score. ",lang)
    read("Univariate Variable Analysis!!Categorical Variables are 'gender', 'parental level of education', 'lunch', 'test preparation course' and Numerical Variables are 'math score', 'reading score', 'writing score'. Moving onto the visualizations of the data.",lang)
    #Read Datas & Explanation of Features & Information About Datasets
    dataset = pd.read_csv(path, encoding="windows-1252")
    dataset.sample(10)
    dataset.info()
    root=Toplevel(top)
    root.geometry("700x650")
    #Length and width window :D
    root.title("Dashboard")
    root.configure(background="#7E77D2")
    root.geometry("+300+15")
    lab = Label(root, text = "Welcome to the Dashboard!", font = ('Veranda',20, 'bold'), borderwidth = 4,bg="#7E77D2", fg = "mediumspringgreen").grid(row = 0, column = 1)
    #Button for BAR PLOT
    fp1 = open("bar.png","rb")
    img1=PIL.Image.open(fp1)
    img1 = img1.resize((120,120))
    imgbtn1 = ImageTk.PhotoImage(img1)
    lab1 = Label(root, text = 'Frequency of students under\neach categorical feature', bg = "gold", font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 0)
    b1 = Button(root, image = imgbtn1, compound = TOP, bg = "black",command=on_barclick)
    b1.image = imgbtn1
    b1.grid(row=2,column=0, pady = 20, padx = 20)
    #Button for HISTOGRAM
    fp2 = open(r"hist.png","rb")
    img2=PIL.Image.open(fp2)
    img2 = img2.resize((120,120))
    imgbtn2 = ImageTk.PhotoImage(img2)
    lab2 = Label(root, text = 'Distribution of\nstudent scores', bg = "gold", font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 1)
    b2 = Button(root, image = imgbtn2, compound = TOP, bg = "black",command=on_histclick)
    b2.image = imgbtn2
    b2.grid(row=2,column=1, pady = 20, padx = 20)

    #Button for COMPARITIVE BAR PLOT
    fp4= open(r"comp bar.png","rb")
    img4=PIL.Image.open(fp4)
    img4 = img4.resize((120,120))
    imgbtn4 = ImageTk.PhotoImage(img4)
    lab4 = Label(root, text = 'Student Scires wrt\nCategorical Features', bg = "gold", font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 2)
    b4 = Button(root, image = imgbtn4, compound = TOP, bg = "black",command=on_compclick)
    b4.image = imgbtn4
    b4.grid(row=2,column=2, pady = 20, padx = 20)

    #Button for PIE CHART
    fp3= open(r"piechart.jpg","rb")
    img3=PIL.Image.open(fp3)
    img3 = img3.resize((120,120))
    imgbtn3 = ImageTk.PhotoImage(img3)
    lab3 = Label(root, text = 'Distribution of students\nby Gender', bg = "gold", font = ('Veranda', 9), borderwidth = 2, padx = 10).grid(row = 3, column = 0)
    b3 = Button(root, image = imgbtn3, compound = TOP, bg = "black",command=on_pieclick)
    b3.image = imgbtn3
    b3.grid(row=4,column=0, pady = 20, padx = 20)

    #Button for VIOLIN PLOT
    fp= open(r"violin.png","rb")
    img=PIL.Image.open(fp)
    img = img.resize((120,120))
    imgbtn = ImageTk.PhotoImage(img)
    lab = Label(root, text = 'Scores wrt Gender', font = ('Veranda', 9), bg = "gold", borderwidth = 2).grid(row = 3, column = 1)
    b = Button(root, image = imgbtn, compound = TOP, bg = "black",command=on_violinclick)
    b.image = imgbtn
    b.grid(row=4,column=1, pady = 20, padx = 20)

    #Button for BOXEN PLOT
    fp5= open(r"boxen.png","rb")
    img5=PIL.Image.open(fp5)
    img5 = img5.resize((120,120))
    imgbtn5 = ImageTk.PhotoImage(img5)
    lab5 = Label(root, text = 'Distribution of\nScores wrt Lunch', bg = "gold", font = ('Veranda', 9), borderwidth = 2).grid(row = 3, column = 2)
    b5 = Button(root, image = imgbtn5, compound = TOP, bg = "black",command=on_boxenclick)
    b5.image = imgbtn5
    b5.grid(row=4,column=2, pady = 20, padx = 20)

    #Button for SWARM PLOT
    fp6= open(r"swarm1.png","rb")
    img6=PIL.Image.open(fp6)
    img6 = img6.resize((120,120))
    imgbtn6 = ImageTk.PhotoImage(img6)
    lab6 = Label(root, text = '3D Distribution\nof Scores', bg = "gold", font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 0)
    b6 = Button(root, image = imgbtn6, compound = TOP, bg = "black",command=on_swarmclick)
    b6.image = imgbtn6
    b6.grid(row=6,column=0, pady = 20, padx = 20)

    #Button for JOINT PLOT
    fp7= open(r"hexplot.png","rb")
    img7=PIL.Image.open(fp7)
    img7 = img7.resize((120,120))
    imgbtn7 = ImageTk.PhotoImage(img7)
    lab7 = Label(root, text = 'Overall Scores and\nIndividual Scores', bg = "gold", font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 1)
    b7 = Button(root, image = imgbtn7, compound = TOP, bg = "black",command=on_jointclick)
    b7.image = imgbtn7
    b7.grid(row=6,column=1, pady = 20, padx = 20)

    #Button for GROUP 9
    fp9= open(r"overall.jpeg","rb")
    img9=PIL.Image.open(fp9)
    img9 = img9.resize((120,120))
    imgbtn9 = ImageTk.PhotoImage(img9)  
    lab9 = Label(root, text = 'Overall view of\nRelationships', bg = "gold", font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 2, sticky = '')
    b9 = Button(root, image = imgbtn9, compound = TOP, bg = "black",command=on_overallclick)
    b9.image = imgbtn9
    b9.grid(row=6, column=2, sticky='')
    root.mainloop()
    

from tkinter import Tk, Button, Entry, Label
top = Tk()
#top.eval('tk::PlaceWindow . center')
top.geometry("300x200")
center(top)
top.configure(background="salmon")
name = Label(top, text = "Enter dataset path").place(x = 30,y = 50)
# Import module
from tkinter import *


# Dropdown menu options
options = [
	"ENGLISH",
	"SPANISH",
	"FRENCH",
        "CHINESE",
        
        "VIETNAMESE"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "ENGLISH" )

# Create Dropdown menu
drop = OptionMenu( top , clicked , *options )
drop.pack()
drop.place(x = 30,y = 100)

# Create Label
label = Label( top , text = " " )
label.pack()


#emp_id = Label(top, text = "Enter video path").place(x = 30, y = 90)   
e1 = Entry(top)
e1.place(x = 150, y = 50)


sbmitbtn = Button(top, text = "Demystify",activebackground = "pink", activeforeground = "blue",command=execute1).place(x = 140, y = 130)
#sbmitbtn.pack()
#close()
top.mainloop()
top.destroy()


