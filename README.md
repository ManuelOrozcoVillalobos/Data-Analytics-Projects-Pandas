# Data-Analytics-Projects-Pandas

The app downloads 3 XML files in order to store them in the system and analyze them.
  Data of office A: https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
  Data of office B: "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
  Data of HR: "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
  
After that, the XML files are converted into usable data, with pandas(dataframes) and then the 3 dataframes are merged and edited into one final dataset, 
to be stored in a variable called office_hr.

Base on that data, the visualization and analysis menu is displayed:
  Visualization Menu:
  Choose your option to visualize
    1.Top employees by department
    2.Number of projects worked by low paid employees
    3.Evaluation of productivity and satisfaction of employees
    4.Visualize the structure of the dataset
    Exit the app
    
Option 1: Display the top n employees with more hours worked and their respective departments in the company.
Option 2: Display the number of projects worked by employees with a low salary in a specific department.
Option 3: Display measurements of selected employees. The measurements are the productivity evaluation of the employee and the satisfaction level in the company.
Option 4: Display the structure of the analyzed dataset.
Exit: Finish the program.
