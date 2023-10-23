import streamlit as st
import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from scipy.stats import zscore
import statsmodels.api as sm

# Define the Streamlit app
def main():
    st.title("ARIMA Time Series Forecasting App")

    # Upload the CSV file
    uploaded_file = st.file_uploader("ADANIPORTS.csv", type=['csv'])

    if uploaded_file is not None:
        df1 = pd.read_csv(uploaded_file)
        ndf = df1[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
        ndf['Date'] = pd.to_datetime(ndf['Date'])
        ndf.set_index('Date', inplace=True)
        ndf.fillna(method='ffill', inplace=True)
        scaler = MinMaxScaler()
        data_scaled = scaler.fit_transform(ndf)
        df2 = pd.DataFrame(data_scaled, columns=ndf.columns, index=ndf.index)
        z_scores = zscore(df2)
        abs_z_scores = np.abs(z_scores)
        outliers = (abs_z_scores > 3).all(axis=1)
        df3 = df2[~outliers]
        x = df3['Close']
        train_size = int(len(x) * 0.8)
        train, test = x[0:train_size], x[train_size:len(x)]
        model = sm.tsa.arima.ARIMA(train , order=(1,1,2))
        result = model.fit()
        forecast = result.forecast(len(test))
        mse = mean_squared_error(test, forecast)
        rmse = np.sqrt(mse)

        # Display RMSE
        st.write(f'Root Mean Squared Error (RMSE): {rmse}')

        # Plot actual vs. forecasted
        st.subheader("Actual vs. Forecasted Prices")
        fig, ax = plt.subplots()
        ax.plot(test.index, test.values, label='Actual')
        ax.plot(test.index, forecast, label='Forecast', color='red')
        ax.legend()
        st.pyplot(fig)

        # User input for future dates
        st.subheader("Enter Dates for Future Predictions")
        user_dates = st.text_area("Enter dates (YYYY-MM-DD) separated by commas")

        if user_dates:
            user_dates = user_dates.split(",")
            user_dates = [date.strip() for date in user_dates]
            user_dates = pd.to_datetime(user_dates)

            # Forecast for user-defined dates
            future_forecast = result.forecast(len(user_dates))

            # Plot user-defined future predictions
            st.subheader("User-Defined Future Predictions")
            fig, ax = plt.subplots()
            ax.plot(user_dates, future_forecast, color='green')
            ax.set_title('User-Defined Future Predictions')
            st.pyplot(fig)

        # Additional Visualizations
        st.subheader("Additional Visualizations")

        # Line plot of Close prices
        st.write("Line Plot of Close Prices")
        fig, ax = plt.subplots()
        ax.plot(df3.index, df3['Close'], label='Close Prices')
        ax.set_xlabel('Date')
        ax.set_ylabel('Close Price')
        ax.legend()
        st.pyplot(fig)

        # Histogram of Close prices
        st.write("Histogram of Close Prices")
        fig, ax = plt.subplots()
        ax.hist(df3['Close'], bins=30, color='skyblue', edgecolor='black')
        ax.set_xlabel('Close Price')
        ax.set_ylabel('Frequency')
        st.pyplot(fig)

if __name__ == "__main__":
    main()


