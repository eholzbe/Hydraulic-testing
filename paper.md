---
title: 'Instructing Pump Test Evaluation using Jupyter'
tags:
  - Python
  - hydrogeology
  - ground water
  - pump test
  - parameter estimation
authors:
  - name: Ekkehard Holzbecher
    orcid: 0000-0002-1350-9223
    affiliation: German University of Technology in Oman (GUtech)
date: 5 January 2021
bibliography: paper.bib

---

# Summary

A Jupyter notebook is presented that introduces methods for pumping test evaluation. Pumping tests are used for characterizing aquifers and thus provide means for evaluating the potential productivity of groundwater wells. Based on ’classical’ data the notebook demonstrates the use of several graphical and numerical evaluation methods and lets the user explore the use of the methods in given tasks. The notebook was created as accompanying material for a lecture on the topic. In a questionnaire the vast majority of the students were positive about the new way of online
learning, presented in this notebook. 

# Introduction

Pumping tests are a common content in the toolbox of a hydro-geologist. In a pumping test the drawdown of the water table due to pumping is recorded. The observed data are evaluated to obtain basic properties of the aquifer, the permeable geological layer containing groundwater (Figure 1). 

In the past decades several methods have been developed to perform the evaluation task in practice. Mathematically one may describe them as inverse modelling procedures. Most of these are based on analytical solutions of the differential equation in 1D. The approach is valid only under highly idealized conditions: homogeneity, isotropy, ideal well, infinite extend, etc.

In the past graphical methods have been favoured, derived from the solutions of @thiem for the stationary case, and @theis:1935, if time-dependent drawdown has been recorded. Extensions for the leaky aquifer that is overlain by a semi-permeable layer, were presented by @deglee:1930 for the steady state and by @HJ:1955 as well as @hantush:1956 for the time dependent case. Numerous further extensions have been developed for special cases [@renard:2005]. Nowadays the evaluation is mostly done on a computer. 

# Statement of Need

@cleveland:1996 presented an evaluation method that can be operated on an EXCEL spreadsheet, mimicking the graphical method for matching the Theis typecurve. @LP:2013 described how this method can be applied to student teaching. 

The Hytool package [@renard:2017] was developed for MATLAB® users. There is a large palette of special cases included, concerning large diameter wells, fractured aquifers, slug tests, etc. The package is open source and can be accessed via GitHub [@renard:2020]. Parts of the functionality of the Hytool package is available in R [@bertone], or in Python [@pianaro]. 

There are commercial programs also. The most important one, @aqtesolv works on WINDOWS operating systems, which covers many more special evaluation methods.
For instructions in the classroom none of these installations is really satisfactory. In all freely available methods previous knowledge on operating the software is required: either EXCEL, MATLAB®, R or Python. Aside from the financial side the commercial software has the disadvantage that it is available only on WINDOWS. 
    
A notebook using the Oude Korendijk pump test as example was presented by @olsthoorn. However this concerned evaluation based on Theis, and did not include methods based on stationary data, neither parameter estimation, nor methods for leaky aquifers. Moreover, the graphical methods were pre-defined and did not give the user options for own explorations. 

# The Jupyter Implementation

An introduction into the topic on a Jupiter notebook was put on the web by @olsthoorn. This implementation was the starting point for the implementation that is presented here. In the Olsthoorn notebook field data from a real test were utilized to demonstrate several evaluation methods. The Oude Korendijk test [@wit:1963], performed in the Netherlands in 1962, was selected as a reference in many publications and in the popular textbook of @KdR:1994. The described implementation followed in this respect. The Olthoorn notebook was completely redesigned and extended.  

The notebook introduces several evaluation methods. First the methods are presented that utilize only the steady state or steady shape data: Thiem for confined and unconfined aquifers, as well as de Glee for a leaky aquifer. In what follows the notebook focuses on the more common task that is based on time series of drawdown values. There are options to visualize the data on linear or logarithmic axes. The method of @CJ:1946 utilizes the fact that in the semi-logarithmic coordinate system the data roughly follow a straight line. The aquifer characteristics can be obtained from the slope and zero of the line. The notebook demonstrates this for the example dataset of the Oude Korendijk pump test. 

The classical graphical method is to match the data with the Theis type curve. Instead of using a printout of the data and transparent paper the user can explore the procedure in the notebook. Moreover, the user has the possibility to obtain a measure of the fit, either by the residual or by the standard deviation. In the final part of the notebook the user can run numerical parameter estimation algorithms, either for the confined or for the leaky aquifer, based on the solutions of @theis:1935 or @hantush:1956.           

The notebook not only explains the various methods, but also gives the user options to explore the methods. Buttons initiate different graphical representations of data, the computation of goodness of fit, and the run of parameter optimization algorithms. The classical graphical method of curve matching is mimicked by sliders that the user can operate to shift the observation data set horizontally and vertically (Figure 3). For parameter estimation there are input fields in which initial guesses have to be entered. This allows the user to explore if and how results depend on the starting points. In addition the user has the option to choose between the two time series of the Oude Korendijk pump test. Thus one can obtain an idea about the variability and the uncertainty of the results. 

Parameter estimation is used for the de Glee solution in case of stationary data, and for Theis and Hantush solutions in case of time series. Internally the ’fmin’-function of the scipy.optimize library is implemented to perform the optimization task. Bessel functions and the exponential integral are imported from scipy.special. The Hantush well function is evaluated following @VM:2010.

# Lecturing Pump Test Evaluations

The notebook was written for an online lecture on hydraulic testing,  more specifically for the topic of pumping test evaluations. It was deployed in the lectures for undergraduates at German University of Technology in Oman in 2020. The notebook was made available and operable to the students by myBinder [@binder]. Using the link, no special software installations from side of the students are required.
The students were instructed to hide the code and to run all cells at start. Thus the initialization (library import, data reading and the creation of the user interface elements) is performed first. The notebook is written in a manner to allow the examination of the different evaluation methods by clicking the corresponding buttons.
 
![Figure 2: Visualization of pump test input data in semi-log coordinates](Figure2.png) 
 
Figure 2 is a visualization of the input data in semi-log coordinates. Figure 3 demonstrates curve matching by the operation of sliders. The data curve (dots) is shifted in the direction of the coordinate axes in dependence of the operation of the sliders. The aim is to match the dots with the type curve (blue). Former positions of the dots are depicted in grey. The positions corresponding to the actual values of the sliders are shown in orange.  Figure 4 shows the outcome of a parameter estimation run. Observed values and type curve are plotted as in the previous figure. The resulting parameter values (T for transmissivity, S for storativity) are given in the plot, as well as the measures of fit.  

![Figure 4: Example output from a parameter estimation run](Figure4.png)

The notebook contains tasks that the students are to do.  The tasks let them explore the different evaluation methods.  A task sheet was distributed to the students to note and compare the results that they obtain with the different methods. Evaluations of stationary data are based on two measurements at different locations.  As four positions have been observed in the example test, the students were instructed to perform the evaluations using different pairs of locations. Thus they can obtain an understanding of the sensitivity of the method on the measurements. 

Concerning the time-dependent case the students were required to apply the graphical method and parameter estimations (Theis and Hantush) and check their goodness of fit. They were instructed to note all their results in tabular form and draw conclusions from the comparison. Based on their work they were asked which parameter values for the aquifer characteristics, transmissivity and storativity, they would write as final result in a report. They were also asked about what the evaluation reveals about the type of the aquifer (confined, unconfined, leaky). 

In a questionnaire at the end of the lecture 82 % of the 52 students found the notebook easy to understand, 92% found it easy to operate and 58% would recommend use of notebooks in future lectures.

# Figures

Figures can be included like this:
![Caption for example figure.\label{fig:example}](figure.png)
and referenced from text using \autoref{fig:example}.

Figure sizes can be customized by adding an optional second parameter:
![Caption for example figure.](figure.png){ width=20% }

# References