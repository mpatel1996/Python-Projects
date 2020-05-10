import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import operator
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import RandomizedSearchCV, train_test_split
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, mean_absolute_error
plt.style.use('seaborn')

global adjust_dates
global total_cases
global future_forecast
global days_in_future
global future_forecast_dates
global dates_var

def plot_graph(x_train, x_test, y_train, y_test):
	
	linear_model = LinearRegression(normalize=True, fit_intercept=True)
	linear_model.fit(x_train, y_train)
	test_linear_pred = linear_model.predict(x_test)
	linear_pred = linear_model.predict(future_forecast)
	print('MAE: ', mean_absolute_error(test_linear_pred, y_test))
	print('MSE: ', mean_squared_error(test_linear_pred, y_test))
	
	kernel = ['poly']
	c = [0.01]
	gamma = [0.1]
	epsilon = [0.01]
	shrinking = [True, False]
	svm_grid = {'kernel': kernel, 'C': c, 'gamma': gamma, 'epsilon': epsilon, 'shrinking': shrinking}
	
	svm_model = SVR()
	svm_search = RandomizedSearchCV(svm_model, svm_grid, scoring='neg_mean_squared_error', cv=3, return_train_score=True, n_jobs=-1, n_iter=30, verbose=1)
	svm_search.fit(x_train, y_train)
	
	svm_search.best_params_
	svm_cases = svm_search.best_estimator_
	svm_pred = svm_cases.predict(future_forecast)
	predicted_values = []
	for i in range(len(svm_pred)):
		predicted_values.append(round((svm_pred[i]), 4))
	
	# print("LR Predicted values: \n", linear_pred[-days_in_future:])
	print("SVM future predictions: \n")
	print(sorted(set(zip(future_forecast_dates[-days_in_future:], svm_pred[-days_in_future:])), reverse=False))
	
	plt.figure()
	plt.plot(adjust_dates, total_cases)
	plt.plot(linear_pred, linestyle='dashed', color='red')
	plt.plot(predicted_values, linestyle='dashed', color='orange')
	plt.title("COVID-19 Cases over time", size=30)
	plt.xlabel("Days since 2/1/2020", size=30)
	plt.ylabel("Number of Cases", size=30)
	plt.legend(['Confirmed Cases', 'Linear Prediction', 'SVM Predictions'])
	plt.xticks(size=15)
	plt.yticks(size=15)
	plt.show()
	

if __name__ == "__main__":
	
	ca_data = pd.read_csv("CA_COVID.csv")
	cols = ca_data.keys()
	confirmed = ca_data.loc[:, cols[4]:cols[-1]]
	dates = confirmed.keys()
	total_cases = []
	# dates_var = []
	
	for i in dates:
		confirmed_sum = int(confirmed[i].sum())
		total_cases.append(confirmed_sum)
	
	day_since = np.array([i for i in range(len(dates))]).reshape(-1, 1)
	total_cases = np.array(total_cases).reshape(-1, 1)
	
	days_in_future = int(input("How many days in future would you like to predict: "))
	future_forecast = np.array([i for i in range(len(dates) + days_in_future)]).reshape(-1, 1)
	adjust_dates = future_forecast[:-days_in_future]
	
	x_train, x_test, y_train, y_test = train_test_split(day_since, total_cases, test_size=0.90, shuffle=False)
	
	start_at = '1/26/2020'
	start_date = datetime.datetime.strptime(start_at, '%m/%d/%Y')
	future_forecast_dates = []
	for i in range(len(future_forecast)+1):
		future_forecast_dates.append((start_date + datetime.timedelta(days=i)).strftime('%m/%d/%Y'))
	
	# print("Forecast Dates: \n", future_forecast_dates)
	
	latest_case = ca_data[dates[-1]]
	
	unique_county = list(ca_data['County Name'].unique())
	
	cases_in_county = []
	no_cases = []
	for i in unique_county:
		cases = latest_case[ca_data['County Name'] == i].sum()
		if cases > 0:
			cases_in_county.append(cases)
		else:
			no_cases.append(i)
	
	for i in no_cases:
		unique_county.remove(i)
	
	unique_county = [k for k, v in sorted(zip(unique_county, cases_in_county), key=operator.itemgetter(1), reverse=True)]
	for i in range(len(unique_county)):
		cases_in_county[i] = latest_case[ca_data['County Name'] == unique_county[i]].sum()
	x_train, x_test, y_train, y_test = train_test_split(day_since, total_cases, test_size=0.10, shuffle=False)
	
	print("Confirmed cases by County")
	for i in range(len(unique_county)):
		print(f'{unique_county[i]}: {cases_in_county[i]} cases')
	#
	# plt.figure()
	# plt.barh(unique_county, cases_in_county)
	# plt.title("COVID-19 Cases in CA")
	# plt.xlabel("Number of cases")
	# plt.show()
	plot_graph(x_train, x_test, y_train, y_test)
	