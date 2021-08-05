# pyladies-mlops-bootcamp

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── baseline_predictions.csv    <- Baseline predictions from hourly model.
    │   ├── capstome_15_min_data.csv    <- Processed data to be used for 15 min model training and testing.
    │   ├── load_actuals.csv            <- Actual Demand data.
    │   ├── load_data_processed.csv     <- Processed data to be used for daily model training and testing.   
    │   ├── weather.csv                 <- Weather forecast data, to be used for daily model training.       
    │   └── mean_daily_predictions.csv  <- Predictions generated by the first(daily) model + wind and solar predictions.  
    │
    │
    ├── capstone-batch-data(folder)     <- Daily model.    #1
    ├── capstone-15-min-data(folder)    <- 15 min model.   #2
    │
    ├── linear_regression_daily.pkl     <- Daily model.    #1
    ├── 15_min_model.pkl                <- 15 min model.   #2
    │
    │
    ├── evaluate_model_daily_1.ipynb    <- Evaluate Daily model.              #1
    ├── trai_daily_model.ipynb          <- Train Daily model.                 #1    
    ├── evaluate_model_15_min.ipynb     <- Evaluate and train 15 min model.   #2
    │
    │
    ├── generate_batch_daily_data.ipynb    <- Daily model.    #1
    ├── generate_15_min_data.ipynb         <- 15 min model.   #2
    │
    ├── create_batch_pipeline.ipynb        <- Batch pipeline - Daily model.            #1
    ├── blob_function (folder)             <- Blob Trigger functions - 15 min model.   #2    
    │
    └── capstone.md                     <- Capstone project tasks.

--------