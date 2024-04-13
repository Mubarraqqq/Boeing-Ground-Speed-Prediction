<div align="center">
    <h1>Ground Speed Prediction of a Boeing Airplane</h1>
    <img src="deploy.png" width='650' /> 
</div>

<br>


End to End Machine Learning project which consists of data cleaning, augmenting, wrangling, modeling, deploying and evaluating my solutions to bring about a working system

Data was gotten from a live API, [AviationAPI](https://docs.aviationapi.com/#tag/VATSIM), which was created to pull applicable information like charts, chart changes, weather, etc. at every 28 days interval.

I carried out data cleaning and analysis and visualization process using python libraries such as, pandas, missingno, matplotlib and seaborn.

I built a Linear Regression model using the Scikit-learn library to predict the Ground speed of Boeing Aircrafts. With an accuracy of 83.3% and MSE of 5013 units, I am looking at implementing a much better model to give me more accurate prediction and a lower error

The model was deployed on the Hugging face platform using Gradio

I wrote an article here showing my thought process of how I got the data via API to build an AI system for predicting Ground speed in a Boeing Aircraft.




Please send a message if you have a contribution and find it useful.
