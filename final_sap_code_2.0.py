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
import numpy as np # linear algebra
#C:\Users\Yashmitha R\Downloads\Final folder\netflix_titles.csv
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from assistant import read
import time
import matplotlib
from matplotlib import colors
import matplotlib.cm as cm
from matplotlib import gridspec
import altair as alt
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import PIL.Image
from PIL import ImageTk
import gc
import re

#Importing the Necessary Libraries
import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
import matplotlib
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
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
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
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
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
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
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
            mng = plt.get_current_fig_manager()
            mng.window.state('zoomed')
            plt.ylabel("Frequency",weight='bold',fontsize=20)
            plt.title(title[3],weight='bold',fontsize=12)
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.pie(sizes, labels=["Female","Male"], colors = ["#FF2281","#87CEFA"], autopct='%1.1f%%')
    plt.title('Distribution of Students by Gender',color = 'black',fontsize = 10, weight = "bold")
    plt.pause(3)
    read("This graphic shows the distribution of samples according to their gender.",lang)
    plt.close()
def on_violinclick(event=None):
    """Violin Plot :A Violin Plot is used to visualize the distribution and probability density of the data. The thick black bar in the middle represents the interquartile range; The vertically extended thin black line represents 95% confidence intervals and the white point is the media.
    """

    fig, ax = plt.subplots(figsize =(10, 7) ,tight_layout = True,dpi=90)
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    
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
    ax2.fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    ax1.fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    ax1.fig.subplots_adjust(top=0.95)
    plt.show(block=False)
    plt.pause(3)
    read("The joint plot shows that the points where the lines are concentrated show that there are more students in the grade range Between 60-80.",lang)
    dataset.info()
    plt.close()

    #Another kind of Joint Plot. The points where the lines are concentrated show that there are more students in that grade range. Between 60-80.
    p=sns.jointplot(x = dataset['writing score'], y = dataset['overall'],color="#FF2079", kind="reg", size=7,marginal_kws={'lw':3,'color':'black'}).set_axis_labels('Writing Score',"Overall Score")
    p.fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    p.ax_marg_x.set_facecolor('#ccffccaa')
    p.ax_marg_y.set_facecolor('#ccffccaa')
    p.fig.suptitle("Relationship between the overall score and writing score", weight = "bold")
    p.fig.subplots_adjust(top=0.95)
    plt.show(block=False)
    plt.pause(3)
    read("In this graph, as in the others, a linear increase is observed between 'overall' and any Score value. The distribution of students seems balanced between 50-85.",lang)
    dataset.drop('overall', axis=1, inplace=True)
    dataset.info()
    plt.close()
    
def on_swarmclick(event=None):                     
    #swarmplot

    import seaborn as sns
    sns.set_theme(style="darkgrid")

    fig, ax = plt.subplots(figsize =(14, 8) ,tight_layout = True,dpi=110)
    fig.suptitle('3D Distribution of Student scores with respect to test preparation course & parental level of education', fontsize=14, fontweight='bold')
    fig.canvas.manager.window.wm_geometry("+%d+%d" % (0, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    f, ax = plt.subplots(figsize=(9, 8), dpi=90)
    f.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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

    
    plt.show(block=False)
    plt.close()
    g=sns.pairplot(dataset, hue="lunch",markers=["o", "s"],height=2,palette="flare")
    g.fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    g.fig.subplots_adjust(top=0.95)
    g.fig.suptitle('Pairplot of Lunch type with respect to Scores', fontsize=12, fontweight='bold')
    plt.show(block=False)
    plt.pause(3)
    read("As we have see in the previous plots and reviews, students with 'lunch' = 'standard' generally do better than others.",lang)
    plt.close()


    #How effective is the test preparation course?
    f= plt.subplots()
    plt.show(block=False)
    plt.close()
    g=sns.pairplot(dataset, hue="test preparation course",diag_kind="hist",palette="viridis",height=2,markers=["d", "s"])
    g.fig.canvas.manager.window.wm_geometry("+%d+%d" % (300, 0))
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
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
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')

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
    read("In conclusion, students who completed the test preparation course, whose parents have a master’s degree and the lunch category has a standard value tend to score higher in maths, reading and writing examinations. Thus in education institutions, students should be encouraged to take up the test preparation course. Factors parental education and lunch cannot be changed, but if the student puts in effort by completing the course,he/she will definitely score well.",lang)
    dataset.drop('overall', axis=1, inplace=True)
    dataset.info()
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


lang=""

def on_execute1():
    
    global lang
    global dataset
    #print(e1.get())
    lang = clicked.get()
    read("Data for storytelling!! The topic under consideration is Students Performance in Examinations in the United States of America.The dataset is a public dataset from Kaggle. The factors taken into consideration are: gender, parental level of education, lunch, test preparation score, math score, reading score and writing score. ",lang)
    read("Univariate Variable Analysis!!Categorical Variables are 'gender', 'parental level of education', 'lunch', 'test preparation course' and Numerical Variables are 'math score', 'reading score', 'writing score'. Moving onto the visualizations of the data.",lang)
    #Read Datas & Explanation of Features & Information About Datasets
    dataset = pd.read_csv("StudentsPerformance.csv", encoding="windows-1252")
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
    
#netflix
def on_ContentGenreplot(event=None):
    # 1. Netflix Content By Type
    fig, ax = plt.subplots(figsize =(12, 6))
    plt.title("Percentation of Netflix Titles that are either Movies or TV Shows",weight='bold',fontsize=18)
    g = plt.pie(netflix_df.type.value_counts(),explode=(0.025,0.025), labels=netflix_df.type.value_counts().index, colors=['red','lightgrey'],autopct='%1.1f%%', startangle=180,textprops={'color':"k"},wedgeprops={"edgecolor":"k",'linewidth': 2})
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("There are far more movie titles (69.1%) that TV shows titles (21.9%) in terms of title",lang)
    plt.close()
    """There are far more movie titles (68,5%) that TV shows titles (31,5%) in terms of title.
    """
    #2. Countries by the Amount of the Produces Content
    filtered_countries = netflix_df.set_index('title').country.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
    filtered_countries = filtered_countries[filtered_countries != 'Country Unavailable']
    plt.figure(figsize=(13,7))
    g = sns.countplot(y = filtered_countries, order=filtered_countries.value_counts().index[:15],palette='magma')
    plt.title('Top 15 Countries Contributor on Netflix',weight='bold',fontsize=18)
    plt.xlabel('Titles')
    plt.ylabel('Countries')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("we can see the top 15 countries contributor to Netflix. The country by the amount of the produces content is the United States.",lang)
    plt.close()
    """
    From the images above, we can see the top 15 countries contributor to Netflix. The country by the amount of the produces content is the United States.
    """
    #4. Top Genres on Netflix
    filtered_genres = netflix_df.set_index('title').listed_in.str.split(', ', expand=True).stack().reset_index(level=1, drop=True);
    plt.figure(figsize=(10,10),dpi=70)
    g = sns.countplot(y = filtered_genres, order=filtered_genres.value_counts().index[:20],palette="viridis")
    plt.title('Top 20 Genres on Netflix',weight='bold',fontsize=18)
    plt.xlabel('Titles')
    plt.ylabel('Genres')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.ylabel('Genres',rotation=90)
    plt.show(block=False)
    plt.pause(3)
    read("From the graph, we know that International Movies take the first place, followed by dramas and comedies.",lang)
    plt.close()
    """
    From the graph, we know that International Movies take the first place, followed by dramas and comedies.
    """
    #5. Top-20 countries producing most contents:
    #Since there are contents that are produced in different countries sp we have to consider those too. So we have to split those rows and get the indivisual country.
    country_data = netflix_df['country']
    country_count = pd.Series(dict(Counter(','.join(country_data).replace(' ,',',').replace(', ',',').split(',')))).sort_values(ascending=False)
    top20country = country_count.head(20)
    fig = plt.figure(figsize=(20,7))
    gs = gridspec.GridSpec(nrows=1, ncols=2, height_ratios=[6], width_ratios=[10, 5])
    ax=plt.subplot(gs[0])
    sns.barplot(top20country, top20country.index, ax=ax, palette="RdGy")
    ax.set_ylabel("Countries")
    ax.set_xlabel("Content Number")
    ax.set_title('Top 20 countries with most contents', fontsize=18, fontweight='bold')
    ax2=plt.subplot(gs[1])
    ax2.pie(top20country, labels=top20country.index, shadow=True, startangle=0, colors=sns.color_palette("RdGy", n_colors=20),autopct='%1.2f%%',textprops={'fontsize': 8})
    ax2.axis('equal') 
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("We can see that US, India, United Kingdom, Canada and France contribute 75% of the top20 countries",lang)
    plt.close() 
    """
    We can see that US, India, United Kingdom, Canada and France contribute 75% of the top20 countries
    """
    #7.Year wise content added growth in movies and TV shows (2008 to 2019)
    survey_df =netflix_df.copy() #make a copy of original dataframe for reference or to avoid making changes in that
    survey_df.drop(['show_id'],axis=1,inplace=True)
    survey_df.country.fillna(value="United States",inplace=True)
    survey_df['date_added']=pd.to_datetime(survey_df['date_added'],errors='coerce')
    #converting to datetime format
    #importing libraries for visualization and setting some parameters for nice plots
    sns.set_style('darkgrid')
    matplotlib.rcParams['font.size'] = 14
    matplotlib.rcParams['figure.figsize'] = (9, 5)
    matplotlib.rcParams['figure.facecolor'] = '#00000000'
    survey_df['year_added']=pd.DatetimeIndex(survey_df.date_added).year
    years = range(2008,2020)
    movies = count_per_year(survey_df,'Movie',2008,2019)
    tv_shows =count_per_year(survey_df,'TV Show',2008,2019)
    plt.plot(years,movies,'b-x')
    plt.plot(years,tv_shows,'r-o')
    plt.legend(['Movies', 'TV Shows'])
    plt.ylabel('Count')
    plt.xlabel('Year')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.title('Netflix content added from 2008 to 2019',weight='bold',fontsize=18)
    plt.show(block=False)
    plt.pause(3)
    read("The plot shows the Year wise content added growth in movies and TV shows (2008 to 2019)",lang)
    plt.close()
    survey_df =netflix_df.copy() #make a copy of original dataframe for reference or to avoid making changes in that
    #11. Genres of Netflix content (TV Show and Movies)
    movie_df = survey_df.loc[survey_df.type=='Movie']
    Movie_genre= pd.Series(movie_df.listed_in.str.split(', ').sum()).value_counts()
    Genres_m = Movie_genre.index
    Count_m = Movie_genre.values/Movie_genre.values.sum() *100
    tv_df = survey_df.loc[survey_df.type=='TV Show']
    tv_genre= pd.Series(tv_df.listed_in.str.split(', ').sum()).value_counts()
    Genres_tv = tv_genre.index
    Count_tv = tv_genre.values/Movie_genre.values.sum() *100
    fig, (ax1,ax2) = plt.subplots(1,2,figsize=(20,10),dpi=70)
    ax1.set_title("Genres of Movies and their percentage on Netflix",weight='bold',fontsize=18)
    sns.barplot(y=Genres_m,x=Count_m,ax=ax1)
    ax1.set_xlabel('Total Percentage (%)',labelpad=20, fontsize=20);
    ax1.plot()
    ax2.set_title("Genres of TV and their percentage on Netflix",weight='bold',fontsize=18)
    sns.barplot(y=Genres_tv,x=Count_tv,ax=ax2)
    ax2.set_xlabel('Total Percentage (%)',labelpad=20, fontsize=20);
    fig.tight_layout(pad=3.0)
    fig.suptitle('Distribution of Movie and TV show with genres',y=1.0,fontsize=25,weight='bold');
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("The plot shows the Distribution of Movie and TV show with genres.",lang)
    plt.close()
def count_per_year(df,type_content,start_year,end_year):
    count=[]
    for i in range(start_year,end_year+1):
        m=len(df.loc[(df.type==type_content) & (df.year_added==i)]) #where both conditions satisfied, will return those in list
        count.append(m)
    return count
def on_MainCategoriesplot(event=None):
    #10.CATEGORIZING ALL INTO 5 CATEGORIES
    survey_df =netflix_df.copy() #make a copy of original dataframe for reference or to avoid making changes in that
    survey_df.drop(['show_id'],axis=1,inplace=True)
    survey_df.country.fillna(value="United States",inplace=True)
    survey_df['date_added']=pd.to_datetime(survey_df['date_added'],errors='coerce')
    #converting to datetime format
    #importing libraries for visualization and setting some parameters for nice plots
    sns.set_style('darkgrid')
    matplotlib.rcParams['font.size'] = 14
    matplotlib.rcParams['figure.figsize'] = (9, 5)
    matplotlib.rcParams['figure.facecolor'] = '#00000000'
    Little_kids= survey_df.rating.value_counts()['G']+survey_df.rating.value_counts()['TV-Y']+survey_df.rating.value_counts()['TV-G']
    Older_kids= survey_df.rating.value_counts()['PG']+survey_df.rating.value_counts()['TV-Y7']+survey_df.rating.value_counts()['TV-Y7-FV']+survey_df.rating.value_counts()['TV-PG']
    Teens = survey_df.rating.value_counts()['TV-14']++survey_df.rating.value_counts()['PG-13']
    Mature = survey_df.rating.value_counts()['TV-MA']+survey_df.rating.value_counts()['NC-17']+survey_df.rating.value_counts()['R']
    Not_Rated = survey_df.rating.value_counts()['UR']+survey_df.rating.value_counts()['NR']
    #plot pie chart
    plt.pie(x=[Mature,Teens,Older_kids,Little_kids,Not_Rated],labels=['Mature','Teens','Older Kids','Little Kids','Not Rated'],autopct='%1.1f%%',radius=1,pctdistance=0.7)
    plt.title('Netflix content listed rating',fontsize=15,weight='bold')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("The plot depicts that More than 70% content is for teens and mature audience",lang)
    plt.close()

    
def on_DirectorsArtistsplot(event=None):
    #3. Top Directors on Netflix
    filtered_directors = netflix_df[netflix_df.director != 'No Director'].set_index('title').director.str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
    plt.figure(figsize=(13,7),dpi=70)
    plt.title('Top 10 Director Based on The Number of Titles',fontsize=15,weight='bold')
    plt.ylabel('Director Names',rotation=90)
    ax=sns.countplot(y = filtered_directors, order=filtered_directors.value_counts().index[:10], palette='prism')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.xlabel('Count of Titles')
    for i, v in enumerate(filtered_directors.value_counts()[:10]):
        ax.text(v + 0.2, i + .16, str(v), color='black', fontweight='light', fontsize=10)
    plt.show(block=False)
    plt.pause(3)
    read("The most popular director on Netflix, with the most titles, is mainly international.",lang)
    plt.close()

    """
    The most popular director on Netflix, with the most titles, is mainly international.
    """
    #12.Top20 artist present on Netflix:
    netflix_df['cast_name'] = netflix_df['cast'].apply(lambda x :  x.replace(' ,',',').replace(', ',',').split(','))    
    cast_count = []
    for i in netflix_df['cast_name']:
        cast_count += i
    cast_dict = dict((i, cast_count.count(i)) for i in cast_count)
    df_cast=pd.DataFrame(cast_dict.values(),cast_dict.keys()).reset_index().sort_values(0,ascending=False).rename(columns = {'index' : 'cast_name', 0 : 'count'}).iloc[1:21]
    plt.figure(figsize=(15,5))
    sns.barplot(x='count',y='cast_name',data=df_cast,palette="RdGy")
    plt.title("Top20 Artist on Netflix",fontweight="bold")
    plt.xticks(rotation=0)
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("The plot shows the top 20 artists present on netflix,out of which the top 4 are from India.",lang)
    plt.close()
    #18
    netflix_df.director.value_counts()[1:20].sort_values(ascending=False).plot(kind='barh', width=0.5, color='red');
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.title("Number of movies /tv shows with respect to director",fontsize=15,weight='bold')
    plt.show(block=False)
    plt.pause(3)
    read("Raúl Campos, Jan Suter are most common director that direct the TV Show or movie that are found on the Netflix. We can also check the what type of content i.e. TV Show or Movie they were direct.",lang)
    plt.close()

    """
    Raúl Campos, Jan Suter are most common director that direct the TV Show or movie that are found on the Netflix. We can also check the what type of content i.e. TV Show or Movie they were direct.
    """
    #19
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8),dpi=70)
    data = netflix_df.groupby('type')['director'].value_counts()['Movie'][1: 20]
    data = pd.DataFrame(data)
    ax1.barh(data.index,data.director, color='red')
    ax1.tick_params(labelrotation=0)
    ax1.set_title('Movie', fontsize=24, fontweight='bold')
    data2 = netflix_df.groupby('type')['director'].value_counts()['TV Show'][1: 20]
    data2 = pd.DataFrame(data2)
    ax2.barh(data2.index,data2.director, color='grey')
    ax2.tick_params(labelrotation=0)
    ax2.set_title('TV Show', fontsize=24, fontweight='bold');
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("The plot depicts that Raúl Campos, Jan Suter directs the Movie only that are uploaded on the Netflix and Alastair Fothergill mostly directs TV Show that were found on the Netflix",lang)
    plt.close()


"""
Raúl Campos, Jan Suter directs the Movie only that are uploaded on the Netflix and Alastair Fothergill mostly directs TV Show that were found on the Netflix
"""

 
def on_Additionplot(event=None):
    #8. Month wise netflix content
    survey_df =netflix_df.copy() #make a copy of original dataframe for reference or to avoid making changes in that
    survey_df.drop(['show_id'],axis=1,inplace=True)
    survey_df.country.fillna(value="United States",inplace=True)
    survey_df['date_added']=pd.to_datetime(survey_df['date_added'],errors='coerce')
    #converting to datetime format
    #importing libraries for visualization and setting some parameters for nice plots
    sns.set_style('darkgrid')
    matplotlib.rcParams['font.size'] = 14
    matplotlib.rcParams['figure.figsize'] = (9, 5)
    matplotlib.rcParams['figure.facecolor'] = '#00000000'
    monthly_content=pd.DatetimeIndex(survey_df.date_added).month.value_counts().sort_index()
    order=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    plt.title("Monthly added content on netflix",y=1.1,fontsize=15,weight='bold')
    sns.barplot(y=monthly_content.values,x=order,palette='bwr',edgecolor='black');
    plt.xlabel("Months")
    plt.ylabel("Frequency");
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("The plot depicts that most of the TV Shows and Movie that were added on the Netflix is in the month of December.",lang)
    plt.close()
    #9 On which day of week Netflix uploads the content?
    survey_df['weekday'] = pd.DatetimeIndex(survey_df.date_added).weekday
    b=survey_df.weekday.value_counts().sort_index()
    #0 is for Monday
    order=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
    sns.barplot(x=order,y=b.values,palette='crest',edgecolor='black');
    plt.xlabel("Weekday")
    plt.ylabel("Frequency")
    plt.title("Distribution of netflix content on the days of week",y=1.1);
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("The plot depicts that netflix uploads content on friday most of the times",lang)
    plt.close()
    
def on_SeasonTimeplot(event=None):
    #14
    plt.figure(figsize=(6, 6))
    labels=['1 Season', '2 Season', '3 Season']
    _, _, texts = plt.pie(netflix_df.duration.value_counts()[:3], labels=labels, autopct='%1.2f%%', startangle=90, 
                      explode=(0.1, 0.0, 0.0), colors=['red', 'grey', 'black'])
    plt.axis('equal')
    plt.title('Season Duration', fontsize=22, fontweight='bold');
    for text in texts:
        text.set_color('white')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("Most of the tv shows have a duration which extends only upto one season.",lang)
    plt.close()
    #15
    plt.plot(netflix_df.duration.value_counts().index.to_list()[3: 20],netflix_df.duration.value_counts()[3:20], color='red')
    plt.xticks(rotation='10',fontsize=8)
    plt.title('Movie and TV Show Duration', fontsize=18, fontweight='bold');
    plt.xlabel("Duration")
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("Most of the Movie of TV Show are of duration 90 min found over the Netflix.",lang)
    plt.close()
    """
    Most of the Movie of TV Show are of duration 90 min found over the Netflix.
    """
def on_RatingPopularityplot(event=None):
    #16
    plt.figure(figsize=(8, 10))
    sns.countplot(y='rating', data=netflix_df, order=netflix_df.rating.value_counts().index.to_list(), palette='dark:salmon_r')
    plt.title('Different Ratings', fontsize=24, fontweight='bold')
    plt.ylabel('Rating')
    plt.xlabel('Count')
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("The plot depicts that TV-MA is the most common rating over the Netflix.",lang)
    plt.close()
    """
    So, TV-MA is the most common rating over the Netflix.
    """
    #17
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 10))
    df_movie = pd.DataFrame(netflix_df.groupby('type')['release_year'].value_counts()['Movie'].sort_values(ascending=False)[:20])
    ax1.barh(df_movie.index, df_movie.release_year, color='red')
    ax1.set_ylabel('Years')
    ax1.set_title('Release Year of Movie', fontsize=24, fontweight='bold');
    df_tv = pd.DataFrame(netflix_df.groupby('type')['release_year'].value_counts()['TV Show'].sort_values(ascending=False)[:20])
    ax2.barh(df_tv.index, df_tv.release_year, color='grey')
    ax2.set_ylabel('Years')
    ax2.set_title('Release Year of TV Show', fontsize=24, fontweight='bold');
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("This shows that in the year 2020, TV Show popularity increase over the Movie on Netflix.",lang)
    plt.close()

    """
    This shows that in the year 2020, TV Show popularity increase over the Movie on Netflix.
    """
def on_WordCloudplot(event=None):
    #6. Majority of NetFlix Shows are about -
    #Here we will read the description of all the movies and tv shows. 
    #Then a wordcloud will be made highlighting the frequency of words by size of thjat word
    from wordcloud import WordCloud, STOPWORDS
    #color_list=['#CD853F','#DC143C','#00FF7F','#FF6347','#8B008B','#00FFFF','#0000FF','#8B0000','#FF8C00', '#1E90FF','#00FF00','#FFD700','#008080','#008B8B','#8A2BE2','#228B22','#FA8072','#808080']
    #transfer
    #colormap=colors.ListedColormap(color_list)
    stopwords = set(STOPWORDS)
    text = " ".join(review for review in netflix_df.description).lower()
    wordcloud = WordCloud(background_color='black',stopwords = stopwords,min_font_size = 8).generate(text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.title("Majority of NetFlix Shows are about",weight='bold',fontsize=18)
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("Wordcloud showing the most frequent words in the description of movies and tv shows",lang)
    plt.close()
    
def on_FamousTagplot(event=None):
    """
    Top five artist'swarm1.png
    """

    listed_in = []
    for i in range(len(netflix_df)):
        listed_in.extend(netflix_df.listed_in.iloc[i].split(','))
    listed_dic = {}
    for i in listed_in:
        listed_dic[i] = listed_in.count(i)
    listed_dic = sorted(listed_dic.items(), key=lambda item: item[1], reverse=True)
    listed_dic = dict(listed_dic)

    #13
    plt.figure(figsize=(20, 15),dpi=70)
    plt.bar(listed_dic.keys(),listed_dic.values(),color="red")
    plt.xticks(rotation='80',fontsize=8);
    plt.ylabel("Category list")
    plt.title("Most famous tag for TV Shows/Movies", fontsize=24, fontweight='bold')
    plt.xlabel("frequency")
    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.pause(3)
    read("Most of the Movie with the tag International Movies were found over the Netflix. So, making the Show or Movie famous you must have International Movie tag over your show.",lang)
    read("Conclusions:We have drawn many interesting inferences from the dataset Netflix titles; here’s a summary of the few of them.The most content type on Netflix is movies,"
    "The popular streaming platform started gaining traction after 2014. Since then, the amount of content added has been increasing significantly."
    "The country by the amount of the produces content is the United States."
    "The most popular director on Netflix , with the most titles, is Jan Suter."
    "International Movies is a genre that is mostly in Netflix."
    "The largest count of Netflix content is made with a “TV-14” rating."
    "The most popular actor on Netflix TV Shows based on the number of titles is Takahiro Sakurai."
    "The most popular actor on Netflix movie, based on the number of titles, is Anupam Kher."
    "Netflix’s main revenue is from Movies and main market is of United States and India . However, in United States, Netflix is more focussing on TV shows recently"
    "Netflix has different content strategies for different countries. For instance, longer movie duration content for India, Anime series in Japan, Romantic Shows in South Korea."
    "More than 70% content is for teens and mature audience",lang)
    plt.close()
    
    
lang=""    
netflix_df=""
def on_execute3():
    global lang
    lang = clicked.get()
    global netflix_df
    #Read Datas & Explanation of Features & Information About Datasets
    read("Exploratory Analysis and Visualization of Netflix movies and tv shows dataset",lang)
    root=Toplevel(top)
    root.geometry("700x650")
    #Length and width window :D
    netflix_df = pd.read_csv("netflix_titles.csv")
    netflix_df.sample(10)
    netflix_df.info()
    print('\nColumns with missing value:')
    print(netflix_df.isnull().any())
    netflix_df.director.fillna("No Director", inplace=True)
    netflix_df.cast.fillna("No Cast", inplace=True)
    netflix_df.country.fillna("Country Unavailable", inplace=True)
    netflix_df.dropna(subset=["date_added", "rating"], inplace=True)
    netflix_df.isnull().any()
    root.geometry(('%dx%d+%d+%d' % (950, 650, 100, 0)))
    root.title("Netflix Dashboard")
    root.configure(background="#F75D59")
    lab = Label(root, text = "Welcome to the Netflix Dashboard!",font = ('Veranda',18, 'bold'), borderwidth = 4,bg="white", fg = "black").grid(row = 0, column = 1)
    
    #Button for PIE CHART
    fp1 = open(r"countplot.png","rb")
    img1=PIL.Image.open(fp1)
    img1 = img1.resize((140,120))
    imgbtn1 = ImageTk.PhotoImage(img1)
    lab1 = Label(root, text = 'Graphs with respect to Content & Genre', bg = "#A5D8F3",font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 0)
    b1 = Button(root, image = imgbtn1, compound = TOP, bg = "black",command=on_ContentGenreplot,width=140)
    b1.image = imgbtn1
    b1.grid(row=2,column=0, pady = 10,padx=50)
    #Button for Contributor CHART
    fp2 = open(r"piechart.jpg","rb")
    img2=PIL.Image.open(fp2)
    img2 = img2.resize((130,120))
    imgbtn2 = ImageTk.PhotoImage(img2)
    lab2 = Label(root, text = 'Main Categories of Content', bg = "#E8E500",font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 1)
    b2 = Button(root, image = imgbtn2, compound = TOP, bg = "black",command=on_MainCategoriesplot,width=130)
    b2.image = imgbtn2
    b2.grid(row=2,column=1, pady = 10)
    #Button for Directors CHART
    fp3 = open(r"countplot1.jpg","rb")
    img3=PIL.Image.open(fp3)
    img3 = img3.resize((150,120))
    imgbtn3 = ImageTk.PhotoImage(img3)
    lab3 = Label(root, text = 'Graphs related to directors & artists', bg = "#A5D8F3",font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 2)
    b3 = Button(root, image = imgbtn3, compound = TOP, bg = "black",command=on_DirectorsArtistsplot,width=150)
    b3.image = imgbtn3
    b3.grid(row=2,column=2, pady = 10)
    #Button for Genres CHART
    fp4 = open(r"c.png","rb")
    img4=PIL.Image.open(fp4)
    img4 = img4.resize((150,120))
    imgbtn4 = ImageTk.PhotoImage(img4)
    lab4 = Label(root, text = 'Monthly & day wise  addition of content', bg = "#E8E500",font = ('Veranda', 9), borderwidth = 2).grid(row = 3, column = 0)
    b4 = Button(root, image = imgbtn4, compound = TOP, bg = "black",command=on_Additionplot,width=150)
    b4.image = imgbtn4
    b4.grid(row=4,column=0, pady = 10)
    #Button for Contents CHART
    fp5 = open(r"lineplot.png","rb")
    img5=PIL.Image.open(fp5)
    img5 = img5.resize((150,120))
    imgbtn5 = ImageTk.PhotoImage(img5)
    lab5 = Label(root, text = 'Season & time duration wise divison of shows', bg = "#A5D8F3",font = ('Veranda', 9), borderwidth = 2).grid(row = 3, column = 1)
    b5 = Button(root, image = imgbtn5, compound = TOP, bg = "black",command=on_SeasonTimeplot,width=150)
    b5.image = imgbtn5
    b5.grid(row=4,column=1, pady = 10)
    #Button for Contents CHART
    fp6 = open(r"hist.png","rb")
    img6=PIL.Image.open(fp6)
    img6 = img6.resize((150,120))
    imgbtn6 = ImageTk.PhotoImage(img6)
    lab6 = Label(root, text = 'Graphs with respect to rating & popularity', bg = "#E8E500",font = ('Veranda', 9), borderwidth = 2).grid(row = 3, column = 2)
    b6 = Button(root, image = imgbtn6, compound = TOP, bg = "black",command=on_RatingPopularityplot,width=150)
    b6.image = imgbtn6
    b6.grid(row=4,column=2, pady = 10)
    #Button for Contents CHART
    fp7 = open(r"wordcloud.jpg","rb")
    img7=PIL.Image.open(fp7)
    img7 = img7.resize((150,120))
    imgbtn7 = ImageTk.PhotoImage(img7)
    lab7 = Label(root, text = 'WordCloud of majority of netflix shows', bg = "#A5D8F3",font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 0)
    b7 = Button(root, image = imgbtn7, compound = TOP, bg = "black",command=on_WordCloudplot,width=150)
    b7.image = imgbtn7
    b7.grid(row=6,column=0, pady = 10)
    #Button for Contents CHART
    fp8 = open(r"comp bar.png","rb")
    img8=PIL.Image.open(fp8)
    img8 = img8.resize((130,120))
    imgbtn8 = ImageTk.PhotoImage(img8)
    lab8 = Label(root, text = 'Most famous tag for TV Shows/Movies & Conclusion', bg = "#E8E500",font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 1)
    b8 = Button(root, image = imgbtn8, compound = TOP, bg = "black",command=on_FamousTagplot,width=130)
    b8.image = imgbtn8
    b8.grid(row=6,column=1, pady = 10)
    
#mental health




#Data Cleaning
gender_clean = {
    "female":"Female",
    "male":"Male",
    "Male":"Male",
    "male-ish":"Male",
    "maile":"Male",
    "trans-female":"Female",
    "cis female":"Female",
    "f":"Female",
    "m":"Male",
    "M":"Male",
    "something kinda male?":"Male",
    "cis male":"Male",
    "woman":"Female",
    "mal":"Male",
    "male (cis)":"Male",
    "queer/she/they":"Female",
    "non-binary":"Unspecified",
    "femake":"Female",
    "make":"Male",
    "nah":"Unspecified",
    "all":"Unspecified",
    "enby":"Unspecified",
    "fluid":"Unspecified",
    "genderqueer":"Unspecified",
    "androgyne":"Unspecified",
    "agender":"Unspecified",
    "cis-female/femme":"Female",
    "guy (-ish) ^_^":"Male",
    "male leaning androgynous":"Male",
    "man":"Male",
    "male ":"Male",
    "trans woman":"Female",
    "msle":"Male",
    "neuter":"Unspecified",
    "female (trans)":"Female",
    "queer":"Unspecified",
    "female (cis)":"Female",
    "mail":"Male",
    "a little about you":"Unspecified",
    "malr":"Male",
    "p":"Unspecified",
    "femail":"Female",
    "cis man":"Male",
    "ostensibly male, unsure what that really means":"Male",
    "female ":"Female",
    "Female":"Female",
    "Male-ish":"Male"
}
#factorplots graphs

def on_plot1(event=None):
    #plot1
    treatment_values = data.treatment.value_counts().to_frame()
    family_history_values = data.family_history.value_counts().to_frame()
    plot_frame = pd.DataFrame({'answers': ['No', 'Yes'], 'Treatment': treatment_values['treatment'], 'Family History': family_history_values['family_history']})
    plot_frame = pd.melt(plot_frame, id_vars='answers', var_name="Treatment", value_name="Family History")
    custom_palette = sns.color_palette("Paired", 9)
    sns.factorplot(x='Treatment', y='Family History', hue='answers', data=plot_frame, kind='bar',palette="winter").set(ylabel='Count', xlabel='', title='Answers Count')
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.title("Answer counts vs Family History and Treatment Categories", weight = 'bold', fontsize = 20)
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(3)
    read("The plot represents the answers count with respect to features family history and treatment",lang)
    plt.close()
    
def on_plot2(event=None):
    #plot2
    treatment_values_yes = data.treatment.loc[data.family_history == 'Yes'].value_counts().to_frame()
    treatment_values_no = data.treatment.loc[data.family_history == 'No'].value_counts().to_frame()
    plot_frame = pd.DataFrame({'With Family History': treatment_values_yes['treatment'], 'No Family History': treatment_values_no['treatment']})
    plot_frame.index.name = 'answers'
    plot_frame.reset_index(inplace=True)
    plot_frame = pd.melt(plot_frame, id_vars='answers', var_name="With Family History", value_name="No Family History")
    sns.factorplot(x='With Family History', y='No Family History', hue='answers', data=plot_frame, kind='bar',  palette="plasma").set(ylabel='Count', xlabel='', title='Answers Count wrt Teatment')
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    #mng.attributes('-zoomed', True)
    mng.window.state('zoomed')
    plt.title("Answer counts vs Family History Categories", weight = 'bold', fontsize = 20)
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(3)
    read("The plot represents the answer counts with respect to treatment under categories under having the family history and not",lang)
    plt.close()

    #plot3
    work_interfere_yes = data.work_interfere.loc[data.treatment == 'Yes'].value_counts().to_frame()
    work_interfere_no = data.work_interfere.loc[data.treatment == 'No'].value_counts().to_frame()
    plot_frame = pd.DataFrame({'With Treatment': work_interfere_yes['work_interfere'], 'Without Treatment': work_interfere_no['work_interfere']})
    plot_frame.index.name = 'answers'
    plot_frame.reset_index(inplace=True)
    plot_frame = pd.melt(plot_frame, id_vars='answers', var_name="With Treatment", value_name="Without Treatment")
    sns.factorplot(x='With Treatment', y='Without Treatment', hue='answers', data=plot_frame, kind='bar',  palette="twilight_r").set(ylabel='Count', xlabel='', title='Answers Count wrt Work Interfere')
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.title("Work Interface Answer Counts vs Treatment Categories", weight = 'bold', fontsize = 20)
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(3)
    read("The plot represents the Work Interfere Answer Count under categories taking treatment and not",lang)
    plt.close()

    #plot4
    work_interfere_yes = data.work_interfere.loc[data.family_history == 'Yes'].value_counts().to_frame()
    work_interfere_no = data.work_interfere.loc[data.family_history == 'No'].value_counts().to_frame()
    plot_frame = pd.DataFrame({'With Family History': work_interfere_yes['work_interfere'], 'Without Family History': work_interfere_no['work_interfere']})
    plot_frame.index.name = 'answers'
    plot_frame.reset_index(inplace=True)
    plot_frame = pd.melt(plot_frame, id_vars='answers', var_name="With Family History", value_name="Without Family History")
    sns.factorplot(x='With Family History', y='Without Family History', hue='answers', data=plot_frame, kind='bar',  palette="Set1").set(ylabel='Count', xlabel='', title='Answers Count wrt Work Interfere')
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    #mng.attributes('-zoomed', True)
    mng.window.state('zoomed')
    plt.title("Answer counts vs Family History Categories", weight = 'bold', fontsize = 20)
    plt.tight_layout()
    plt.margins(0.1)
    plt.show(block=False)
    plt.pause(3)
    read("The plot represents the Work Interfere answer count under categories having the family history and not",lang)
    plt.close()
    
def on_plot3(event=None):    
    plt.figure(figsize=(20,20))
    wordcloud = WordCloud(background_color='white', width=1024, height=1024).generate(re.sub(r'[^\w\s]',''," ".join(list(data.comments.unique()[1:]))))
    plt.axis("off")
    plt.imshow(wordcloud)
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    

    plt.show(block=False)
    plt.pause(3)
    read("A word cloud of what the employees have to say in regard to this issue of Mental Health!",lang)
    plt.close()
                                

def on_plot4(event=None):
    sns.set_style("whitegrid")
    plt.figure(figsize=(15,7))
    sns.countplot(x='leave', data=data, order=data.leave.value_counts().index, hue='tech_company', color='cyan')
    plt.xlabel("How East/Difficult is it to take leave?")
    plt.ylabel("No. of Reponses")
    plt.title("How East/Difficult is it to take leave?", weight = 'bold', fontsize = 20)
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(3)
    read("The plot depicts how easy/difficult is it to take a leave? Nearly 40% of the total respondents are unsure about their company's policies on taking leaves. The trend is consistent quite consistent in Tech-NonTech companies, and with both Males & Females.",lang)
    plt.close()
    

def on_plot5(event=None):
    #plot5
    data.Gender = data.Gender.str.lower()
    data.Gender = data.Gender.apply(lambda x: gender_clean[x])

    # ## Some basic employment statistics
    #
    # - Distribution on the basis of **Gender**. (Need more women in tech...surprised,eh?)
    # - How does the age vary in the professional industry?

    plt.figure(figsize=(6,6))
    space = [0.1,0.2,0.4]
    data['Gender'].value_counts().plot(kind='pie', wedgeprops=dict(width=0.5), explode=space, fontsize=10,autopct='%1.1f%%')

    plt.ylabel('Gender', weight = 'bold', fontsize=15)
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.title("Gender Distribution", weight = 'bold', fontsize = 20)
    plt.show(block=False)
    plt.tight_layout()
    plt.pause(3)
    read("The plot depcits gender distribution. Plot indicates the number of women in tech is less. ",lang)
    plt.close()
    
def on_plot6(event=None):
    #Plot6
    f, ax = plt.subplots(1,2, figsize=(15,7))
    ax1 = ax[0].pie(list(data['Gender'].value_counts()),labels=['Male','Female','Unspecified'],autopct='%1.1f%%', shadow=True, startangle=90,colors=['#66b3ff','#ff9999','#99ff99'])
    ax[1].set_title("Distribution of Ages")
    ax2 = sns.distplot(data.Age.clip(15,70), ax=ax[1])
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.title("Age variation", weight = 'bold', fontsize = 20)
    plt.show(block=False)
    plt.tight_layout()
    plt.pause(3)
    read("The plot indicates How the age varies in the professional industry?",lang)
    plt.close()

    
def on_plot7(event=None):
    #Plot7
    # - Donut chart clearly signifies the industry is Male Dominated.**
    # I thought it would also be interesting to extract other basic stats about **Age** here like *mean, standard dev, quartile values* etc. The average age of an IT employee stands at only **32**, quite surprising!
    #Extraction of basic stats from all numeric columns
    pd.DataFrame(data.Age.clip(15,60).describe())

    # ## Participation in the Survery - by Country
    #
    # Although, the United States dominates this category it would've been great if developing nations such as **India**, **Russia** & **Israel** had more participants since little is known about the working conditions in these countries & health issues that working professionals from these countries face.
    #
    # Another thing, due to this extreme domination of the US in this survey, it has kind-of rendered it useless to do a country-wise analysis since there are *<50* participants from a majority of the countries.

    sns.set_style("darkgrid")
    plt.figure(figsize=(15,20))
    sns.countplot(y='Country', data=data, orient='h', order=data.Country.value_counts().index).set(ylabel='Number of Employees per Country', xlabel='', title='Number of Employees per Country')

    mng = plt.get_current_fig_manager()
    mng.window.state('zoomed')
    
    plt.title("Tech employee distribution, Countrywise", weight = 'bold', fontsize = 20)
    plt.show(block=False)
    plt.margins(0.1)

    plt.pause(3)
    read("The plot depcits the number of tech employees per country", lang)
    plt.close()
    
def on_plot8(event=None):
    # ## How big/small is your company?
    # About 75% of the employees belong to the companies with less than 500 employees deeming them as very small ventures. Quite typical of the tech-industry.

    f, ax = plt.subplots(1,2, figsize=(14,7))
    patches, texts, autotexts = ax[0].pie(list(data['no_employees'].value_counts()), labels=['6-25', '26-100', '>1000', '100-500', '1-5', '500-1000'], autopct='%1.1f%%', shadow=True, startangle=90)
    plt.title("Percentage of Employees", weight = 'bold', fontsize = 20)
    new = ax[1].pie(list(data['remote_work'].value_counts()), labels=['Non-Remote', 'Remote Work'], autopct='%1.1f%%', shadow=True, startangle=0, colors=['#66b3ff','#ff9999'])

    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.title("How big/small is your company?")
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(3)
    read("The plot shows that about 75% of the employees belong to the companies with less than 500 employees deeming them as very small ventures. Quite typical of the tech-industry.",lang)
    plt.close()

def on_plot9(event=None):
    company_characs = ["treatment","benefits","care_options","wellness_program"]

    sns.set_style("darkgrid")
    company_chars_corr = data[company_characs].apply(lambda x : pd.factorize(x)[0]).corr(method='pearson', min_periods=1)
    plt.figure(figsize = (8, 6))

    # Heatmap of correlations
    sns.set(font_scale=0.8)
    sns.heatmap(company_chars_corr, cmap = "Oranges", vmin = -0.25, annot = True, vmax = 0.6)
    plt.title("Correlation Heatmap of Company Policies \ntowards employee's wellness", weight = 'bold', fontsize = 20)
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.tight_layout()
    plt.show(block=False)
    plt.pause(3)
    read("Let's explore some Company Policies & their correlation. The features taken into consideration for this heatmap are 1. Treatment, 2. Benefits, 3. Care Options and 4. Wellness Program.",lang)
    plt.close()

    # # Well Being Indicators
    # There are also certain binary attributes in this dataset that help describe the state of well being of an individual, namely --
    # 1. Seeking Help
    # 2. Mental Health Consequences (due to job)
    # 3. Physical Health Consequences (due to job)
    # 4. Observed Consequences
    # 5. Mental Health Interview
    #
    # All of these are also categorical in nature so we simply factorize them as before.
    wellbeing_indicators = ['seek_help','mental_health_consequence','obs_consequence','mental_health_interview','phys_health_consequence']


    wellbeing_indicators_corr = data[wellbeing_indicators].apply(lambda x : pd.factorize(x)[0]).corr(method='pearson', min_periods=1)
    plt.figure(figsize = (12, 9))

    # Heatmap of correlations
    sns.set(font_scale=0.8)
    sns.heatmap(wellbeing_indicators_corr, cmap = "Pastel1", vmin = -0.25, annot = True, vmax = 0.6)
    plt.title("Correlation Heatmap of Well Being\n indicators of Employees", weight = 'bold', fontsize = 20);
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.xticks(rotation  = 10)
    plt.tight_layout()
    plt.pause(3)
    read("This heatmap is with respect to 'seek help','mental health consequence','obs consequence','mental health interview','physical health consequence'",lang)
    plt.close()

    # How do company policies relate to their employee's well-being?

    wellbeing_policy_corr = data[wellbeing_indicators + company_characs].apply(lambda x : pd.factorize(x)[0]).corr(method='pearson',min_periods=1)
    plt.figure(figsize = (12, 9))

    # Heatmap of correlations
    sns.set(font_scale=0.8)
    sns.heatmap(wellbeing_policy_corr, cmap = "PuBuGn", vmin = -0.25, annot = True, vmax = 0.6)
    plt.title("Correlation Heatmap between Employee Well Being \nand Company Policies", weight = 'bold', fontsize = 20);
    mng = plt.get_current_fig_manager()
    #mng.window.state('zoomed')
    mng.window.state('zoomed')
    plt.show(block=False)
    plt.xticks(rotation = 10)
    plt.tight_layout()
    plt.pause(3)
    read("This plot depicts How do company policies relate to their employee's well-being? Here, we simply put together the features indicating company policies with those indicating the overall well-being of the employee.",lang)
    plt.close()

lang=""
def on_execute2():
    
    global lang
    global dataset
    #print(e1.get())
    lang = clicked.get()
    global data
    read("Mental Health Survey in the Tech Industry",lang)
    read("Mental health is a level of psychological well-being or an absence of mental illness. It is the 'psychological state of someone who is functioning at a satisfactory level of emotional and behavioural adjustment'",lang)
    read("The projects is used to explore some relevant stats extracted from the *Mental Health Survey - Tech Industry, 2014. And since the data was found to be extremely messy and largely categorical in nature so therefore data cleaning* was an important part of this analysis.",lang)
    #Read Datas & Explanation of Features & Information About Datasets
    data = pd.read_csv('survey_2014.csv')
    data.sample(10)
    data.info()
    root=Toplevel(top)
    root.configure(background="#FEE12B")
    root.geometry("900x650")
    #Length and width window :D
    
    
    lab = Label(root, text = "Welcome to Mental Health Dashboard!", font = ('Veranda',20, 'bold'), borderwidth = 4,bg="#FEE12B", fg = "darkblue").grid(row = 0, column = 1)

    #Button for PLOT1
    fp1 = open("plot1.png","rb")
    img1=PIL.Image.open(fp1)
    img1 = img1.resize((120,120))
    imgbtn1 = ImageTk.PhotoImage(img1)
    lab1 = Label(root, text = 'Answer Count vs\nFeatures', bg = "salmon", font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 0)
    b1 = Button(root, image = imgbtn1, compound = TOP, bg = "black",command=on_plot1)
    b1.image = imgbtn1
    b1.grid(row=2,column=0, pady = 20, padx = 20)

    #Button for PLOT2
    fp2 = open(r"plot2_1.png","rb")
    img2=PIL.Image.open(fp2)
    img2 = img2.resize((120,120))
    imgbtn2 = ImageTk.PhotoImage(img2)
    lab2 = Label(root, text = 'Answer Count vs\nCategories', bg = "salmon", font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 1)
    b2 = Button(root, image = imgbtn2, compound = TOP, bg = "black",command=on_plot2)
    b2.image = imgbtn2
    b2.grid(row=2,column=1, pady = 20, padx = 20)

    #Button for PLOT3
    fp4= open(r"plot3.png","rb")
    img4=PIL.Image.open(fp4)
    img4 = img4.resize((120,120))
    imgbtn4 = ImageTk.PhotoImage(img4)
    lab4 = Label(root, text = 'Word Cloud', bg = "salmon", font = ('Veranda', 9), borderwidth = 2).grid(row = 1, column = 2)
    b4 = Button(root, image = imgbtn4, compound = TOP, bg = "black",command=on_plot3)
    b4.image = imgbtn4
    b4.grid(row=2,column=2, pady = 20, padx = 20)

    #Button for PLOT4
    fp3= open(r"plot4.png","rb")
    img3=PIL.Image.open(fp3)
    img3 = img3.resize((120,120))
    imgbtn3 = ImageTk.PhotoImage(img3)
    lab3 = Label(root, text = 'Leave Policies', bg = "salmon", font = ('Veranda', 9), borderwidth = 2, padx = 10).grid(row = 3, column = 0)
    b3 = Button(root, image = imgbtn3, compound = TOP, bg = "black",command=on_plot4)
    b3.image = imgbtn3
    b3.grid(row=4,column=0, pady = 20, padx = 20)

    #Button for PLOT5
    fp= open(r"plot5.png","rb")
    img=PIL.Image.open(fp)
    img = img.resize((120,120))
    imgbtn = ImageTk.PhotoImage(img)
    lab = Label(root, text = 'Gender Distribution', font = ('Veranda', 9), bg = "salmon", borderwidth = 2).grid(row = 3, column = 1)
    b = Button(root, image = imgbtn, compound = TOP, bg = "black",command=on_plot5)
    b.image = imgbtn
    b.grid(row=4,column=1, pady = 20, padx = 20)

    #Button for PLOT6
    fp5= open(r"plot6_1.png","rb")
    img5=PIL.Image.open(fp5)
    img5 = img5.resize((120,120))
    imgbtn5 = ImageTk.PhotoImage(img5)
    lab5 = Label(root, text = 'Age Variation', bg = "salmon", font = ('Veranda', 9), borderwidth = 2).grid(row = 3, column = 2)
    b5 = Button(root, image = imgbtn5, compound = TOP, bg = "black",command=on_plot6)
    b5.image = imgbtn5
    b5.grid(row=4,column=2, pady = 20, padx = 20)

    #Button for PLOT7
    fp6= open(r"plot7.png","rb")
    img6=PIL.Image.open(fp6)
    img6 = img6.resize((120,120))
    imgbtn6 = ImageTk.PhotoImage(img6)
    lab6 = Label(root, text = 'Tech Employee\nDistribution', bg = "salmon", font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 0)
    b6 = Button(root, image = imgbtn6, compound = TOP, bg = "black",command=on_plot7)
    b6.image = imgbtn6
    b6.grid(row=6,column=0, pady = 20, padx = 20)

    #Button for JOINT PLOT
    fp7= open(r"plot8.png","rb")
    img7=PIL.Image.open(fp7)
    img7 = img7.resize((120,120))
    imgbtn7 = ImageTk.PhotoImage(img7)
    lab7 = Label(root, text = 'Company insights', bg = "salmon", font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 1)
    b7 = Button(root, image = imgbtn7, compound = TOP, bg = "black",command=on_plot8)
    b7.image = imgbtn7
    b7.grid(row=6,column=1, pady = 20, padx = 20)

    #Button for GROUP 9
    fp9= open(r"plot9_1.png","rb")
    img9=PIL.Image.open(fp9)
    img9 = img9.resize((120,120))
    imgbtn9 = ImageTk.PhotoImage(img9)  
    lab9 = Label(root, text = 'Correlation b/w\nvariables', bg = "salmon", font = ('Veranda', 9), borderwidth = 2).grid(row = 5, column = 2)
    b9 = Button(root, image = imgbtn9, compound = TOP, bg = "black", command = on_plot9)
    b9.image = imgbtn9
    b9.grid(row=6, column=2, padx = 20, pady = 20)
    #root.mainloop()
    


    
    
from tkinter import Tk, Button, Entry, Label
top = Tk()
top.title("Data Demystifier")
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



#emp_id = Label(top, text = "Enter video path").place(x = 30, y = 90)   
e1 = Entry(top)
e1.place(x = 150, y = 50)
def on_click():
    if e1.get()=="StudentsPerformance.csv":
        print("name",e1.get())
        on_execute1()
    elif e1.get()=="survey_2014.csv":
        print("name",e1.get())
        on_execute2()
    else:
        print("name",e1.get())
        on_execute3()

sbmitbtn = Button(top, text = "Demystify ",activebackground = "pink", activeforeground = "blue",command=on_click).place(x = 140, y = 130)
#sbmitbtn.pack()
#close()
top.mainloop()
top.destroy()


